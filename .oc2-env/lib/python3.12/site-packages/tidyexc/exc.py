#!/usr/bin/env python3

import textwrap
from shutil import get_terminal_size
from contextlib import contextmanager
from collections import ChainMap
from traceback import format_exc
from .views import data_view, nested_data_view, info_view
from .utils import list_iadd, property_iadd, eval_template, flatten

_info_stack = []

class Error(Exception):
    """
    A base class for making exceptions that:

    - Provide direct access to any parameters that are relevant to the error.
    - Use bullet-points to clearly and comprehensively describe the error.

    Example:

    .. code-block:: pycon

        >>> from tidyexc import Error
        >>> class CheeseShopError(Error):
        ...     pass
        ...
        >>> err = CheeseShopError(
        ...         product_name="Red Leicester",
        ...         num_requested=1,
        ...         num_available=0,
        ... )
        >>> err.brief = "insufficient inventory to process request"
        >>> err.info += "{num_requested} {product_name} requested"
        >>> err.blame += "{num_available} available"
        >>> raise err
        Traceback (most recent call last):
          ...
        tidyexc.exc.CheeseShopError: insufficient inventory to process request
        • 1 Red Leicester requested
        ✖ 0 available
    """

    info_bullet = '• '
    "The prefix to use for each `info` message in the formatted error."
    blame_bullet = '✖ '
    "The prefix to use for each `blame` message in the formatted error."
    hint_bullet = '• '
    "The prefix to use for each `hints` message in the formatted error."

    @classmethod
    @contextmanager
    def add_info(cls, *messages, **kwargs):
        """
        Add the given `info` to any exceptions derived from this class that are 
        instantiated inside a with-block.

        A simple example:

        .. code-block:: pycon

            >>> from tidyexc import Error
            >>> with Error.add_info('a: {a}', a=1):
            ...     raise Error()
            ...
            Traceback (most recent call last):
              ...
            tidyexc.exc.Error:
            • a: 1

        The purpose of this function is to make it easier to add contextual 
        information to exceptions.  This is easiest to illustrate with an 
        example.  The following function parses a list of (x, y) coordinates 
        from a file.  Each coordinate appears on its own line and must consist 
        of exactly two whitespace-separated numbers.  There are several 
        different errors this function should detect, but all of the error 
        messages should include the file path, and most should also include the 
        offending line number:

        .. literalinclude:: /parse_xy_coords.py
            :language: python
            :end-before: ##################################### >8 #####################################

        Using `add_info()` simplifies the above code in two major ways:

        - Each piece of contextual information is specified just once and used 
          by multiple exceptions.  There's no way to accidentally raise an 
          exception without this information.

        - The helper functions that actually raise the exceptions don't need to 
          have access to any of the contextual information.  Without 
          `add_info()`, it would either be necessary to pass extra arguments 
          around or to catch and re-raise the exceptions.

        It is possible to nest any number of these context managers.  The 
        `info` bullet points will appear in the order the context managers were 
        invoked.  It is considered good practice for the message templates to 
        only make use of the *kwargs* parameters provided to the same context 
        manager, but templates can access all previously defined parameters.  
        They cannot access any subsequently defined parameters.  If a parameter 
        is defined multiple times, the most recent previous value will be used. 
        For example:

        .. code-block:: pycon

            >>> # This template cannot use the `c` parameter, because it has
            >>> # not been defined yet.  Note that the `b` parameter keeps its 
            >>> # value, even though it is subsequently redefined.
            >>> with Error.add_info('a={a} b={b}', a=1, b=2):
            ...
            ...     # The `a` parameter can be used in this template because 
            ...     # it was defined previously.  The `b` parameter shadows the
            ...     # previous value.
            ...     raise Error('a={a} b={b} c={c}', b=3, c=4)
            ...
            Traceback (most recent call last):
              ...
            tidyexc.exc.Error: a=1 b=3 c=4
            • a=1 b=2

        Because templates cannot be affected by subsequent parameters, it is 
        safe to use `add_info()` in recursive functions, where the same exact 
        parameters might be specified multiple times with different values.  
        The `data` attribute provides access to the current value of each 
        parameter.  The `nested_data` attribute, in contrast, provides access 
        to all values for each parameter.
        """
        try:
            cls.push_info(*messages, **kwargs)
            yield
        finally:
            cls.pop_info()

    @classmethod
    def push_info(cls, *messages, **kwargs):
        """
        Add the given `info` to any exceptions derived from this class that are 
        subsequently instantiated.

        See `add_info()` for more information.  This function is similar, 
        except that it is not a context manager.  That means that you must 
        manually call `pop_info()` or `clear_info()` after calling this 
        function.

        Example:

        .. code-block:: pycon

            >>> from tidyexc import Error
            >>> Error.push_info('a: {a}', a=1)
            >>> try:
            ...     raise Error()
            ... finally:
            ...     Error.pop_info()
            ...
            Traceback (most recent call last):
              ...
            tidyexc.exc.Error:
            • a: 1
        """

        _info_stack.append((cls, messages, kwargs))

    @classmethod
    def pop_info(cls):
        """
        Stop adding the `info` that was most-recently "pushed" to exceptions 
        derived from this class.

        This is the opposite of `push_info()`.
        """
        for i, (cls_i, _, _) in reversed(list(enumerate(_info_stack))):
            if cls_i is cls:
                break
        else:
            raise IndexError(f"no info to pop for {cls}")

        del _info_stack[i]

    @classmethod
    def clear_info(cls):
        """
        Stop adding any `info` that was "pushed" to exceptions derived from 
        this class.
        """
        global _info_stack
        _info_stack = [x for x in _info_stack if x[0] is not cls]

    def put_info(self, *messages, **kwargs):
        i = len(self._data)
        self._info += [(i, m) for m in messages]
        self._data.append(kwargs)


    def __init__(self, brief="", **kwargs):
        """
        Create a new exception.

        You can specify a `brief` message template and any number of parameters 
        (via keyword arguments) when constructing an `Error` instance.  This 
        may be enough for simple exceptions, but most of the time you would 
        subsequently add `info` and `blame` message templates (which cannot be 
        directly specified in the constructor).
        
        Any class-wide parameters and/or message templates specified using 
        `add_info()` or `push_info()` are read and applied during the 
        constructor.  This means that these class-wide functions have no effect 
        on exceptions that have already been instantiated.

        Example:

        .. code-block:: pycon

            >>> raise Error("a: {a}", a=1)
            Traceback (most recent call last):
              ...
            tidyexc.exc.Error: a: 1

        """

        # `info_stack` is in the order that the messages will appear in, i.e.  
        # oldest first.  This is a little inconvenient for `data_view`, because 
        # it means that `ChainMap` naturally reads in the wrong direction, but 
        # `data_view` handles this internally using `reverse_view`.

        self._brief = brief
        self._info = []
        self._blame = list_iadd()
        self._hints = list_iadd()
        self._data = []

        for cls, msgs, kws in _info_stack:
            if isinstance(self, cls):
                self.put_info(*msgs, **kws)

        self._data.append(kwargs)
        self._ctor_data = kwargs

        self._info_view = info_view(self._info)
        self._data_view = data_view(self._data)
        self._nested_data_view = nested_data_view(self._data)

    def __str__(self):
        """
        Return the formatted error message.

        All parameter substitutions are performed at this point, so any changes 
        made to either the message templates or the data themselves will be 
        reflected in the resulting error message.
        """

        # By default, exceptions that occur while printing an exception are 
        # totally sequestered; you just get a message saying "<exception str() 
        # failed>".  This isn't very helpful, so here we manually format the 
        # stack trace and display it to the user.
        try:
            message = ""
            parts = [
                    ('',  [self.brief_str]),
                    (self.info_bullet, self.info_strs),
                    (self.blame_bullet, self.blame_strs),
                    (self.hint_bullet, self.hint_strs),
            ]

            for bullet, strs in parts:
                b = len(bullet)

                for s in strs:
                    s = textwrap.indent(s, b*' ')
                    s = bullet + s[b:]
                    message += s + '\n'

            return message

        except Exception as err:
            # Using format_exc() seems to sometimes trigger stack overflows 
            # within the python interpreter.
            return f"\n\nError occurred while formatting {self.__class__.__name__}:\n\n{err.__class__.__name__}: {err}\n\n"

    @property
    def brief(self):
        """
        A message template briefly describing the error.

        The `tidyverse style guide`__ recommends using the verb "must" when the 
        cause of the problem is pretty clear, and the verb "can't" when it's 
        not.  It's common for this template to be a fixed string (i.e. no 
        parameter substitution), and for the `info` and `blame` templates to 
        reference the parameters of the exception.

        __ https://style.tidyverse.org/error-messages.html

        See `info` for a description of message templates in general.  Unlike 
        `info`, `blame`, and `hints`, there can only be a single `brief` 
        message template.  For this reason, use the assignment operator the set 
        this template (as opposed to the in-place addition operator).

        Example:

        .. code-block:: pycon

            >>> err = Error(a=1)
            >>> err.brief = "a: {a}"
            >>> raise err
            Traceback (most recent call last):
              ...
            tidyexc.exc.Error: a: 1

        """
        return self._brief

    @brief.setter
    def brief(self, value):
        self._brief = value
    
    @property
    def brief_str(self):
        """
        The `brief` message, with all parameter substitution performed.
        """
        return eval_template(self.brief, self.data)

    @property_iadd
    def info(self):
        """
        Message templates describing the context in which the error occurred.

        For example, imagine an error that was triggered because an unmatched 
        brace was encountered when parsing a file.  A good `info` message for 
        this exception might specify the file name and line number where the 
        error occurred.

        A message template can either be a string or a callable:

        - *str*: When the error message is generated, the `str.format` method 
          will be called on the string as follows: ``s.format(**self.data)``.  
          This means that any parameters associated with the exception can be 
          substituted into the message.

        - *callable*: When the error message is generated, the callable will be 
          invoked with `data` as the only argument.  It should return a string 
          or a list of strings, which will be taken as the message(s).  A 
          common use-case for callable template is to specify f-strings via 
          lambda functions.  This is a succinct way to format parameters using 
          arbitrary expressions (see example below).
          
        The `info`, `blame`, and `hints` attributes are all list-like objects 
        containing message templates.  Special syntax is added such that you 
        can use the ``+=`` operator to add message templates to any of these 
        lists.  You can also use any of the usual list methods to modify the 
        list in-place, although you cannot overwrite these attributes 
        altogether.

        The `info` attribute alone has an additional method called ``layers()`` 
        that returns each info template paired with the index that can be 
        passed to ``nested_data.flatten()`` to get the parameters associated 
        with that particular template.
        
        Example:

        .. code-block:: pycon

            >>> err = Error(a=1, b=[2,3])
            >>> err.info += "a: {a}"
            >>> err.info += lambda e: f"b: {','.join(map(str, e.b))}"
            >>> raise err
            Traceback (most recent call last):
              ...
            tidyexc.exc.Error:
            • a: 1
            • b: 2,3

        """
        return self._info_view

    @property
    def info_strs(self):
        """
        The `info` messages, with all parameter substitution performed.
        """
        return flatten(
                eval_template(x, self.nested_data.flatten(i))
                for i, x in self._info
        )

    @property_iadd
    def blame(self):
        """
        Message templates describing the specific cause of the error.

        For example, imagine an error that was triggered because an unmatched 
        brace was encountered when parsing a file.  A good `blame` message for 
        this exception would clearly state that an unmatched brace was the 
        cause of the problem.

        See `info` for a description of message templates in general.

        Example:

        .. code-block:: pycon

            >>> from tidyexc import Error
            >>> err = Error(a=1)
            >>> err.blame += "a: {a}"
            >>> raise err
            Traceback (most recent call last):
              ...
            tidyexc.exc.Error:
            ✖ a: 1

        """
        return self._blame

    @property
    def blame_strs(self):
        """
        The `blame` messages, with all parameter substitution performed.
        """
        return flatten(eval_template(x, self.data) for x in self.blame)

    @property_iadd
    def hints(self):
        """
        Message templates suggesting how to fix the error.

        For example, imagine an error that was triggered because some user 
        input didn't match any of the expected keywords.  A good hint for this 
        exception might suggest the expected keyword that was most similar to 
        what the user inputted.

        See `info` for a description of message templates in general.

        Example:

        .. code-block:: pycon

            >>> from tidyexc import Error
            >>> err = Error(a=1)
            >>> err.hints += "a: {a}"
            >>> raise err
            Traceback (most recent call last):
              ...
            tidyexc.exc.Error:
            • a: 1

        """
        return self._hints

    @property
    def hint_strs(self):
        """
        The `hints` messages, with all parameter substitution performed.
        """
        return flatten(eval_template(x, self.data) for x in self.hints)

    @property
    def data(self):
        """
        Parameters relevant to the error.

        This attribute is a dictionary-like object that allows parameters to be 
        accessed either as attributes or as dictionary elements:

        .. code-block:: pycon

            >>> e = Error(a=1)
            >>> e.data.a
            1
            >>> e.data['a']
            1

        If a parameter has been defined multiple times (e.g. with 
        `add_info()`), the most recent value is the one that will be used:

        .. code-block:: pycon

            >>> with Error.add_info(a=1):
            ...     e = Error(a=2)
            ...     e.data.a
            2

        """
        return self._data_view

    @data.setter
    def data(self, values):
        self._ctor_data.clear()
        self._ctor_data.update(values)

    @property
    def nested_data(self):
        """
        A view providing access to *all* values defined for each parameter.

        This is useful when trying to extract information from an exception 
        where some parameters may have been defined multiple times, e.g. if 
        `add_info()` was used in a recursive function.  

        The simplest way to use this view is to access a parameter name either 
        as an attribute or a dictionary element.  This will return a list of 
        all the values associated with that parameter:

        .. code-block:: pycon

            >>> with Error.add_info(a=1):
            ...     e = Error(a=2)
            ...     e.nested_data.a
            [1, 2]

        The ``[]`` operator will also accept a tuple of parameter names, in 
        which case it will return a list of those parameters in every context 
        in which at least one of those parameters was defined.  This is useful 
        if you're interested in parameters that are logically connected (e.g. 
        line and column number) and you want to avoid the possibility of them 
        getting out of sync:

        .. code-block:: pycon

            >>> with Error.add_info(a=1, b=2):
            ...     with Error.add_info(a=3, b=4):
            ...         e = Error(c=5)
            ...         e.nested_data['a','b']
            [(1, 2), (3, 4)]

        Finally, the view also has a ``flatten()`` method that can be used to 
        get all the values for each parameter defined at a particular point in 
        time.  The method accepts a single argument which will be used as an 
        index into the internal list of contexts.  The ``data.layers()`` method 
        can be used to get the index corresponding to any info message 
        template.
        """
        return self._nested_data_view


