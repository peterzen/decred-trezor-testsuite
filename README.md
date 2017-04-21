# decred-trezor-testsuite (WIP)

Work in progress test suite for Decred integrations with the TREZOR wallet.  

## Install python-trezor

#### Install dependencies
```
  sudo apt-get install -y python-dev cython libusb-1.0-0-dev libudev-dev git virtualenv
```

#### Create virtualenv to keep things contained

```
  virtualenv .virtualenv && source .virtualenv/bin/activate
```

#### Install python-trezor

```
  git clone -b decred-integration https://github.com/peterzen/python-trezor
  pip install ./python-trezor  
```

## Flash Trezor firmware

**WARNING:** This step involves flashing unofficial and untested code onto your TREZOR – DO NOT run it on a production device with real funds on it.

Get the modified Trezor firmware from [source](https://github.com/peterzen/trezor-mcu/tree/decred-integration) or grab the [compiled binary](https://github.com/peterzen/decred-trezor-testsuite/blob/master/firmware-trezor-decred-1.4.2.bin)

```
  wget https://github.com/peterzen/decred-trezor-testsuite/blob/master/firmware-trezor-decred-1.4.2.bin
```
Enable bootloader mode on the TREZOR: unplug the device, and plug it back in while holding both buttons pressed. 

```  
  trezorctl firmware_update -f firmware-trezor-decred-1.4.2.bin
```

Confirm the prompts on the device.  Once the installation is complete, unplug and re-plug the device and press the button twice to confirm that it's OK to run the unsigned firmware binary.

Next, initialize the device – this will involve exporting the 24 word mnemonic so you'll need to press the button 2 * 24 times. 

```
  trezorctl reset_device
```
Once this is completed, your TREZOR runs the Decred enabled firmware.

#### Run python-trezor tests

1. Get list of supported coins: ```trezorctl list_coins```

2. Generate address: ```trezorctl get_address -c Decred ```

3. Generate xpub key: ```trezorctl get_public_node -c Decred -n 1 ``` 

4. Sign message: ```trezorctl sign_message -c Decred -n 1 message```


#### Tests - trezor.js-node (WIP, not functional yet)

There are pending PRs, once merged `trezord` will accept custom coin version and `trezor.js` will support DCR

https://github.com/trezor/trezor-mcu/pull/161
https://github.com/trezor/trezor-mcu/pull/160

https://github.com/trezor/trezor-common/pull/26
https://github.com/trezor/trezor-common/pull/27

https://github.com/trezor/python-trezor/pull/108
https://github.com/trezor/python-trezor/pull/109

https://github.com/trezor/trezor-crypto/pull/90

```
git clone https://github.com/peterzen/decred-trezor-testsuite && cd decred-trezor-testsuite
npm install
npm start

```
