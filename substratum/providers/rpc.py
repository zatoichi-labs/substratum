from typing import (
    Any,
    Dict,
    Iterable,
    Tuple,
)

from substratum.types import (
    RPCEndpoint,
    RPCResponse,
    URI,
)
from substratum.utils import (
    construct_user_agent,
    make_post_request,
    to_dict,
)

from .base import (
    JSONBaseProvider,
)


class HTTPProvider(JSONBaseProvider):
    endpoint_uri = None
    _request_kwargs = None

    def __init__(self, endpoint_uri: URI, request_kwargs: Any=None) -> None:
        self.endpoint_uri = endpoint_uri
        self._request_kwargs = request_kwargs or {}
        super().__init__()

    @to_dict
    def get_request_kwargs(self) -> Iterable[Tuple[str, Any]]:
        if 'headers' not in self._request_kwargs:
            yield 'headers', self.get_request_headers()
        for key, value in self._request_kwargs.items():
            yield key, value

    def get_request_headers(self) -> Dict[str, str]:
        return {
            'Content-Type': 'application/json',
            'User-Agent': construct_user_agent(str(type(self))),
        }

    def make_request(self, method: RPCEndpoint, params: Any) -> RPCResponse:
        request_data = self.encode_rpc_request(method, params)
        raw_response = make_post_request(
            self.endpoint_uri,
            request_data,
            **self.get_request_kwargs()
        )
        response = self.decode_rpc_response(raw_response)
        return response['result']
