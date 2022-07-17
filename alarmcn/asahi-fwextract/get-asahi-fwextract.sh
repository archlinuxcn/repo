#/bin/bash

sh get_pkg.sh asahi-fwextract

echo "makedepends+=(python-setuptools)" >> PKGBUILD
