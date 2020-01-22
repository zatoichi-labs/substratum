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
    Address,
    AccountId,
)
from substratum.utils import (
    SS58,
    blake2b,
)

from .module import (
    Module,
)

def pair_to_account_id(pair: KeyringPair) -> AccountId:
    return pair.public if pair.key_type != 'secp256k1' else blake2b(pair.public)


def pair_to_address(pair: KeyringPair) -> Address:
    return SS58.encode(pair_to_account_id(pair))


class Account(Module):
    _provider: BaseProvider
    _keyring: Keyring = Keyring()

    def generate(self) -> Address:
        """
        Generate a new local account and store it
        :returns: AccountId of newly generated account
        """
        self._keyring.generate()
        pair = self._keyring.pairs[-1]
        return pair_to_address(pair)

    def add_from_uri(self, uri, key_type=None) -> Address:
        if not key_type:
            key_type = self._keyring.default_key_type
        self._keyring.add_from_uri(uri, key_type=key_type)
        a = self._keyring.pairs[-1]
        return pair_to_address(a)

    def getAccounts(self) -> List[Address]:
        # TODO: Remote accounts (in addition to local ones)
        return [pair_to_address(a) for a in self._keyring.pairs]
