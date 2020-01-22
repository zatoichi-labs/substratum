import base58
from hashlib import (
    blake2b as blake2b_hashlib,
)
from typing import (
    Any,
    Union,
)
import requests

from eth_utils import (
    to_dict,
    to_hex,
    to_int,
    to_bytes,
    to_text,
)

from scalecodec import (
    ScaleBytes,
)
from scalecodec.metadata import (
    MetadataDecoder,
)

from substratum.types import (
    AccountId,
    Address,
    HexStr,
    Metadata,
    URI,
)

def blake2b(
    primitive: Union[bytes, int, bool] = None,
    hexstr: str = None,
    text: str = None,
) -> bytes:
    return blake2b_hashlib(to_bytes(primitive, hexstr, text)).digest()


class SS58:
    CHECKSUM_PREFIX = b'SS58PRE'
    CHECKSUM_LENGTH = 2

    @classmethod
    def encode(cls, account_id: AccountId, address_format: int = 42) -> Address:
        if len(account_id) != 32:
            raise ValueError(f"Cannot encode {account_id}")
        encoded_address = to_bytes(address_format) + account_id
        checksum = blake2b(cls.CHECKSUM_PREFIX + encoded_address)
        return base58.b58encode(encoded_address + checksum[:cls.CHECKSUM_LENGTH]).decode("utf-8")

    @classmethod
    def decode(cls, address: Address, address_format: int = 42) -> AccountId:
        decoded_address = base58.b58decode(str.encode(address, "utf-8"))
        if decoded_address[0] != address_format:
            raise ValueError("Invalid address format")

        # TODO: Temporary, decode all valid SS58 address types
        assert len(decoded_address) == 35, f"cannot decode {address}"
        raw_account_id = decoded_address[1:-cls.CHECKSUM_LENGTH]
        checksum = blake2b(cls.CHECKSUM_PREFIX + raw_account_id)

        if checksum[:cls.CHECKSUM_LENGTH] != decoded_address[-cls.CHECKSUM_LENGTH:]:
            raise ValueError("Invalid Checksum")

        return raw_account_id


def construct_user_agent(class_name):
    from substratum import __version__ as version

    user_agent = 'Substratum/{version}/{class_name}'.format(
        version=version,
        class_name=class_name,
    )
    return user_agent


def make_post_request(endpoint_uri: URI, data: bytes, *args: Any, **kwargs: Any) -> bytes:
    kwargs.setdefault('timeout', 10)
    session = requests.Session()
    # https://github.com/python/mypy/issues/2582
    response = session.post(endpoint_uri, data=data, *args, **kwargs)  # type: ignore
    response.raise_for_status()

    return response.content


def decode_metadata(raw_metadata: HexStr) -> Metadata:
    return MetadataDecoder(ScaleBytes(raw_metadata)).decode()
