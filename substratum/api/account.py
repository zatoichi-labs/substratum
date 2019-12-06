from typing import (
    List,
)

from subkey import (
    Keyring,
    KeyringPair,
)
from substratum.providers import (
    BaseProvider,
)
from substratum.types import (
    AccountId,
)

from .module import (
    Module,
)


class Account(Module):
    _provider: BaseProvider
    _keyring: Keyring = Keyring()

    def generate(self) -> AccountId:
        """
        Generate a new local account and store it
        :returns: AccountId of newly generated account
        """
        pair = self._keyring.generate()
        return AccountId(pair.public)

    def add_from_uri(self, uri, key_type=None) -> AccountId:
        if not key_type:
            key_type = self._keyring.default_key_type
        a = self._keyring.add_from_uri(uri, key_type=key_type)
        return AccountId(a)

    def getAccounts(self) -> List[AccountId]:
        return [AccountId(a.public) for a in self._keyring.pairs]
