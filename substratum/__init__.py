import pkg_resources

from substratum.main import (
    Substratum,
)
from substratum.providers.rpc import (
    HTTPProvider,
)

__version__ = pkg_resources.get_distribution("substratum").version

__all__ = [
    "__version__",
    "Substratum",
    "HTTPProvider",
]
