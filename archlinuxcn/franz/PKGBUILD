# Maintainer:  Giovanni 'ItachiSan' Santini <giovannisantini93@yahoo.it>
# Contributor: Filipe Laíns (FFY00) <lains@archlinux.org>
# Contributor: Pieter Goetschalckx <3.14.e.ter <at> gmail <dot> com>

pkgname=franz
#pkgver=${_pkgver//-/_} # Leaving it here for possible dev/beta package :)
pkgver=5.5.0
pkgrel=1
# Due to the previous "_beta" naming
epoch=1
pkgdesc='Free messaging app for services like WhatsApp, Slack, Messenger and many more.'
arch=(x86_64 i686)
url='https://meetfranz.com'
license=(Apache)
# Allow to easily switch between Electron versions.
# Expected one is 'electron' (Electron 8). May change soon.
# Remember to replace it also in `franz.sh`.
_electron='electron'
depends=($_electron)
makedepends=(expac git npm python)
source=("git+https://github.com/meetfranz/$pkgname#tag=v$pkgver"
        'franz.desktop'
        'franz.sh')
sha512sums=('SKIP'
            '049c4bf2e0f362f892e8eef28dd18a6c321251c686a9c9e49e4abfb778057de2fc68b95b4ff7bb8030a828a48b58554a56b810aba078c220cb01d5837083992e'
            '8584507cfc2736f4736637925536b2c06063c59cd943346717633564ae88b64c5eea294c8897f1250812478ed493f54a470501e98e99d084a2ff012dff9671f8')

prepare() {
  # Small patching
  cd $pkgname

  # Prevent franz from being launched in dev mode
  sed -i \
    "s|export const isDevMode = .*|export const isDevMode = false;|g" \
    src/environment.js
  sed -i \
    "s|import isDevMode from 'electron-is-dev'|export const isDevMode = false|g" \
    src/index.js

  # Adjust the electron version to use when building
  electron_version="`expac %v $_electron | cut -d'-' -f1`"
  sed -i "s|\(\s\+\"electron\":\).*,|\1 \"$electron_version\",|" package.json

  # Better configuration for npm cache and calling installed binaries
  export npm_config_cache="$srcdir"/npm_cache

  # Install tricky dependencies before-hand
  node_sass_version="4.14.1"
  sed -i "s|\(\s\+\"node-sass\":\).*,|\1 \"$node_sass_version\",|" package.json

  # Prepare the packages for building
  npx lerna bootstrap
}

build() {
  cd $pkgname

  # Better configuration for npm cache and calling installed binaries
  export npm_config_cache="$srcdir"/npm_cache

  # Actually build the package
  npx gulp build
  npx electron-builder --linux dir
}

package() {
  cd $pkgname

  # Install the .asar files
  install -dm 755 "$pkgdir"/usr/lib/$pkgname
  cp -r --no-preserve=ownership --preserve=mode out/linux-unpacked/resources "$pkgdir"/usr/lib/$pkgname/

  # Install icon
  install -Dm 644 "$srcdir"/franz.desktop "$pkgdir"/usr/share/applications/franz.desktop
  install -Dm 644 build-helpers/images/icon.png "$pkgdir"/usr/share/icons/franz.png

  # Install run script
  install -Dm 755 "$srcdir"/franz.sh "$pkgdir"/usr/bin/franz
}
