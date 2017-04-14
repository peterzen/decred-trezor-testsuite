#!/usr/bin/env python

from trezorlib.client import TrezorClient
from trezorlib.transport_hid import HidTransport

def main():
    # List all connected TREZORs on USB
    devices = HidTransport.enumerate()

    # Check whether we found any
    if len(devices) == 0:
        print('No TREZOR found')
        return

    # Use first connected device
    transport = HidTransport(devices[0])

    # Creates object for manipulating TREZOR
    client = TrezorClient(transport)

    # Print out TREZOR's features and settings
    print(client.features)

    # Get the first address of first BIP44 account
    # (should be the same address as shown in wallet.trezor.io)
    bip32_path = client.expand_path("44'/42'/0'/0/0")
    address = client.get_address('Decred', bip32_path)
    print('Decred address:', address)
    
    address_n = client.expand_path("0")
    xpub = client.get_public_node('Decred', address_n)
    print('xpub: ', xpub)

    client.close()

if __name__ == '__main__':
    main()
    
    