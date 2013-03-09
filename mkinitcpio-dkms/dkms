#!/bin/bash

build() {
    $(which dkms) autoinstall -k $KERNELVERSION
}

help() {
    cat <<HELPEOF
This hook simply utilize the autoinstall function of dkms. It does nothing to the initrd image.
HELPEOF
}

