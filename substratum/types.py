from typing import (
    Any,
    List,
    Literal,
    NewType,
    Tuple,
    TypedDict,
)


HexStr = NewType('HexStr', str)


BlockHash = NewType('BlockHash', HexStr)


BlockNumber = NewType('BlockNumber', int)


TrieRoot = NewType('TrieRoot', HexStr)


BlockHeader = TypedDict('BlockHeader', {
    "digest": Any,  # TODO Fix this
    "extrinsicsRoot": TrieRoot,
    "number": BlockNumber,
    "parentHash": BlockHash,
    "stateRoot": TrieRoot,
})


Block = TypedDict("Block", {
    "extrinsics": List[HexStr],  # TODO Create Extrinsics type
    "header": BlockHeader,
    "justification": Any,  # TODO Find out what this is supposed to be
})


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


RPCMethods = TypedDict("RPCMethods", {
    "methods": List[RPCEndpoint],
    "version": int,
})


# Encoded via SCALE encoding
Metadata = NewType("Metadata", HexStr)


RuntimeVersion = TypedDict("RuntimeVersion", {
    "apis": List[Tuple[HexStr, int]],  # TODO Figure out whaty this is
    "authoringVersion": int,
    "implName": str,
    "implVersion": int,
    "specName": str,
    "specVersion": int,
})


URI = NewType('URI', str)
