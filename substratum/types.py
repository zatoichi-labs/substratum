from typing import (
    Any,
    Dict,
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


URI = NewType('URI', str)
