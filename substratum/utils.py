from typing import (
    Any,
)
import requests

from eth_utils import (
    to_dict,
    to_hex,
    to_int,
    to_bytes,
    to_text,
)

from substratum.types import (
    URI,
)

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
