from substratum.providers import (
    BaseProvider,
)
from substratum.api import (
    System,
)


class Substratum:
    def __init__(self, provider: BaseProvider) -> None:
        self.provider = provider
        self.system = System(self.provider)
