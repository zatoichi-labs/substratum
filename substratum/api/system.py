from substratum.providers import (
    BaseProvider,
)


class System:
    def __init__(self, provider: BaseProvider):
        self.provider = provider

    @property
    def version(self) -> str:
        return self.provider.make_request("system_version", [])

    @property
    def name(self) -> str:
        return self.provider.make_request("system_name", [])
