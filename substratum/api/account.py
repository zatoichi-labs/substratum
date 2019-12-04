from substratum.providers import (
    BaseProvider,
)

from .module import (
    Module,
)


class Account(Module):
    _provider: BaseProvider
