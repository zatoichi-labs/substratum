from substratum.providers import (
    BaseProvider,
)


class Module:
    provider: BaseProvider

    def __init__(self, provider: BaseProvider) -> None:
        self.provider = provider
