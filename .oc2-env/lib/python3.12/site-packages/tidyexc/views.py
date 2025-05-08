#!/usr/bin/env python3

from collections import ChainMap
from collections.abc import Sequence, MutableSequence, MutableMapping
from .utils import iadd_mixin

class data_view(MutableMapping):

    def __init__(self, data_stack):
        # Don't trigger `__setattr__()`, and use name-mangling to avoid 
        # clashing with user-set attributes.
        self.__dict__['_data_view__data'] = ChainMap()
        self.__data.maps = reverse_view(data_stack)

    def __repr__(self):
        return f'data_view({self.__data.maps.items!r})'

    def __eq__(self, other):
        return self.__data == other

    def __len__(self):
        return len(self.__data)

    def __iter__(self):
        return iter(self.__data)

    def __contains__(self, key):
        return key in self.__data

    def __getitem__(self, key):
        return self.__data[key]

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __delitem__(self, key):
        del self.__data[key]

    def __getattr__(self, key):
        try:
            return self.__data[key]
        except KeyError:
            pass

        # Raise the standard exception.
        return super().__getattr__(key)

    def __setattr__(self, key, value):
        self.__data[key] = value

    def __delattr__(self, key):
        try:
            del self.__data[key]
            return
        except KeyError:
            pass

        # Raise the standard exception.
        return super().__delattr__(key)

class nested_data_view:

    def __init__(self, data_stack):
        self._data_stack = data_stack

    def __repr__(self):
        return f'nested_data_view({self._data_stack})'

    def __getitem__(self, key):
        if isinstance(key, tuple):
            hits = []

            for i, d in enumerate(self._data_stack):
                if any(k in d for k in key):
                    v = self.flatten(i)

                    try:
                        hit = tuple(v[k] for k in key)
                        hits.append(hit)
                    except KeyError:
                        pass

        else:
            hits = [
                    d[key]
                    for d in self._data_stack
                    if key in d
            ]

        if not hits:
            raise KeyError(key)

        return hits

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(key) from None

    def flatten(self, layer):
        if layer < 0:
            layer += len(self._data_stack)
        return data_view(self._data_stack[:layer+1])

class info_view(iadd_mixin, MutableSequence):

    def __init__(self, info_pairs):
        self._info_pairs = info_pairs  # list of (index, template) pairs

    def __repr__(self):
        return f'info_view({self._info_pairs})'

    def __eq__(self, other):
        return list(self) == other

    def __getitem__(self, i):
        return self._info_pairs[i][1]

    def __setitem__(self, i, value):
        if isinstance(i, slice):
            self._info_pairs[i] = [(-1, v) for v in value]
        else:
            self._info_pairs[i] = -1, value

    def __delitem__(self, i):
        del self._info_pairs[i]

    def __len__(self):
        return len(self._info_pairs)

    def insert(self, i, value):
        self._info_pairs.insert(i, (-1, value))

    def layers(self):
        return self._info_pairs

class reverse_view(Sequence):

    def __init__(self, items):
        self.items = items

    def __repr__(self):
        items_str = ', '.join(repr(x) for x in self)
        return f'[{items_str}]'

    def __getitem__(self, i):
        return self.items[-i - 1]

    def __len__(self):
        return len(self.items)


