from typing import (
    Any,
    Dict,
    List,
    Literal,
    NewType,
    Optional,
    Tuple,
    TypedDict,
    Union,
)


HexStr = NewType('HexStr', str)


Address = NewType('Address', str)


AccountId = NewType('AccountId', bytes)


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


DocStr = NewType("DocStr", List[str])


IntegerType = Literal['u32', 'u64']
SubstrateType = Literal['Address', 'Bytes', 'Key', 'Balance', 'BalanceOf', 'Moment']

ArgType = Union[SubstrateType, IntegerType, str]


Arg = TypedDict("Arg", {
    "name": str,
    "type": ArgType,
})


Call = TypedDict("Call", {
    "name": str,
    "args": List[Arg],
    "docs": DocStr,
})


Constant = TypedDict("Constant", {
    "name": str,
    "type": ArgType,
    "value": HexStr,
    "docs": DocStr,
})


StorageType = NewType("StorageType", Dict)


StorageItem = TypedDict("StorageItem", {
    "name": str,
    "modifier": Any,
    "type": StorageType,
    "fallback": HexStr,
    "docs": DocStr,
})


Storage = TypedDict("Storage", {
    "prefix": str,
    "items": List[StorageItem],
})


Event = TypedDict("Event", {
    "name": str,
    "args": List[str],
    "docs": List[str],
})


Error = TypedDict("Error", {
    "name": str,
    "docs": DocStr,
})


Module = TypedDict("Module", {
    "name": str,
    "prefix": Optional[str],
    "storage": Optional[Storage],
    "calls": Optional[List[Call]],
    "events": Optional[List[Event]],
    "constants": List[Constant],
    "errors": List[Error],
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


Metadata = TypedDict("Metadata", {
    # TODO Fill this in
})


RuntimeVersion = TypedDict("RuntimeVersion", {
    "apis": List[Tuple[HexStr, int]],  # TODO Figure out what this is
    "authoringVersion": int,
    "implName": str,
    "implVersion": int,
    "specName": str,
    "specVersion": int,
})


ChainProperties = TypedDict("ChainProperties", {
})


Health = TypedDict("Health", {
    'isSyncing': bool,
    'peers': int,
    'shouldHavePeers': bool,
})


PeerInfo = TypedDict("PeerInfo", {
})


LibP2PURI = NewType('LibP2PURI', str)


PeerId = NewType("PeerId", str)

PeerSet = TypedDict("PeerSet", {
    'message_queue': int,
    'nodes': Dict[PeerId, PeerInfo],
    'reserved_only': bool,
})

NetworkState = TypedDict("NetworkState", {
    'averageDownloadPerSec': int,
    'averageUploadPerSec': int,
    'connectedPeers': Dict[PeerId, PeerInfo],
    'externalAddresses': List[LibP2PURI],
    'listenedAddresses': List[LibP2PURI],
    'notConnectedPeers': Dict[PeerId, PeerInfo],
    'peerId': PeerId,
    'peerset': PeerSet,
})


NodeRole = Literal['Authority']  # TODO What other roles?


URI = NewType('URI', str)
