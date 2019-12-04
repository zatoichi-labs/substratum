from typing import (
    Any,
)

from substratum.types import (
    RPCEndpoint,
    RPCResponse,
)


class BaseProvider:
    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        raise NotImplementedError("Providers must implement this method")
