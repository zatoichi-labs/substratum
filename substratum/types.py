from typing import (
    Any,
    Literal,
    NewType,
    TypedDict,
)


RPCError = TypedDict("RPCError", {
    "code": int,
    "message": str,
})


RPCResponse = TypedDict("RPCResponse", {
    "id": int,
    "jsonrpc": Literal["2.0"],
    "result": Any,
    "error": RPCError,
}, total=False)


RPCEndpoint = NewType("RPCEndpoint", str)


URI = NewType('URI', str)
