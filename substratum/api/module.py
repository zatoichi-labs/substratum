from substratum.providers import (
    BaseProvider,
)


class Module:
    _provider: BaseProvider

    def __init__(self, provider: BaseProvider) -> None:
        self._provider = provider
