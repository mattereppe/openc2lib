from . import models
from . import renderers
from . import repositories
from . import translators
from . import types

cases: repositories.Cases = repositories.Cases()

@cases
class Lower(models.Case):
    prepare: types.Translator = translators.lower
    render:  types.Renderer   = renderers.space

@cases
class Upper(models.Case):
    prepare: types.Translator = translators.upper
    render:  types.Renderer   = renderers.space

@cases
class Title(models.Case):
    prepare: types.Translator = translators.title
    render:  types.Renderer   = renderers.space

@cases
class Sentence(models.Case):
    prepare: types.Translator = translators.capitalize
    render:  types.Renderer   = renderers.space

@cases
class Snake(models.Case):
    prepare: types.Translator = translators.lower
    render:  types.Renderer   = renderers.underscore

@cases
class Helter(models.Case):
    prepare: types.Translator = translators.title
    render:  types.Renderer   = renderers.underscore

@cases
class Macro(models.Case):
    prepare: types.Translator = translators.upper
    render:  types.Renderer   = renderers.underscore

@cases
class Kebab(models.Case):
    prepare: types.Translator = translators.lower
    render:  types.Renderer   = renderers.hyphen

@cases
class Train(models.Case):
    prepare: types.Translator = translators.title
    render:  types.Renderer   = renderers.hyphen

@cases
class Cobol(models.Case):
    prepare: types.Translator = translators.upper
    render:  types.Renderer   = renderers.hyphen

@cases
class Flat(models.Case):
    prepare: types.Translator = translators.lower
    render:  types.Renderer   = renderers.concatenate

@cases
class Flush(models.Case):
    prepare: types.Translator = translators.upper
    render:  types.Renderer   = renderers.concatenate

@cases
class Pascal(models.Case):
    prepare: types.Translator = translators.title
    render:  types.Renderer   = renderers.concatenate

@cases
class Camel(models.Case):
    prepare: types.Translator = translators.dromedary
    render:  types.Renderer   = renderers.concatenate

@cases
class Dot(models.Case):
    prepare: types.Translator = translators.lower
    render:  types.Renderer   = renderers.period

@cases
class Path(models.Case):
    prepare: types.Translator = translators.lower
    render:  types.Renderer   = renderers.slash
