#!/bin/bash

VER=$(uname -a)
UBNT="Ubuntu"

if grep -q "$UBNT" <<< "$VER"; then
    sudo apt-get install iperf3
else
    sudo yum install -y iperf3
fi

pip install iperf3 icmplib requests