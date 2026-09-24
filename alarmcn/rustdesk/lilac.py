#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['severach'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('arch='):
            line = 'arch=(aarch64 x86_64)'
        if line.startswith('depends='):
            line = line.replace('pulseaudio', 'pulse-native-provider')
        if line == '  _mod_py':
            # The flutter release tarball ships x86_64 prebuilt binaries
            # (dart-sdk, etc) in bin/cache. Remove them so that flutter
            # bootstraps the ones for the native architecture.
            line += '''
  if [ "${CARCH}" = 'aarch64' ]; then
    rm -rf "${srcdir}/flutter/bin/cache"
    sed -e 's:build/linux/x64/:build/linux/arm64/:g' -i 'build.py'
  fi'''
        if 'flutter/build/linux/x64/release/bundle' in line:
            line = line.replace("'flutter/build/linux/x64/release/bundle'",
                                '"flutter/build/linux/${_flarch}/release/bundle"')
            line = '''    local _flarch=x64
    if [ "${CARCH}" = 'aarch64' ]; then
      _flarch=arm64
    fi
''' + line
        print(line)
