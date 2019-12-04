import json
import itertools
from typing import (
    Any,
)

from substratum.types import (
    RPCEndpoint,
    RPCResponse,
)
from substratum.utils import (
    to_bytes,
    to_text,
)


class BaseProvider:
    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        raise NotImplementedError("Providers must implement this method")


class JSONBaseProvider(BaseProvider):
    def __init__(self) -> None:
        self.request_counter = itertools.count()

    def decode_rpc_response(self, raw_response: bytes) -> RPCResponse:
        text_response = to_text(raw_response)
        return json.loads(text_response)

    def encode_rpc_request(self, method: RPCEndpoint, params: Any) -> bytes:
        rpc_dict = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params or [],
            "id": next(self.request_counter),
        }
        encoded = json.dumps(rpc_dict)
        return to_bytes(text=encoded)
