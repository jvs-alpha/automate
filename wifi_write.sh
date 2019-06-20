#!/bin/bash
echo """ network={
        ssid="$1"
        psk="$2"
        key_mgmt=WPA-PSK
}
""" >> txt
