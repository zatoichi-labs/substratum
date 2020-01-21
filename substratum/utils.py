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
