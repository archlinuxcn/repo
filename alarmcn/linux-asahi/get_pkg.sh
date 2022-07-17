#!/bin/sh

pkg=$1

git clone --depth 1 https://github.com/AsahiLinux/PKGBUILDs
mv PKGBUILDs/$pkg/* .
rm -rf PKGBUILDs/
updpkgsums || true
