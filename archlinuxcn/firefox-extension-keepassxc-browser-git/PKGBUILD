# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Forked from aur/firefox-extension-keepassxc-browser. Original contributors:
# Contributor: Hezekiah Michael <spiritomb at protonmail dot com>

pkgname=firefox-extension-keepassxc-browser-git
pkgdesc="Official browser plugin for the KeePassXC password manager."
pkgver=1.7.8.1.r21.g3db23e9
pkgrel=1
arch=('any')
url="https://addons.mozilla.org/en-US/firefox/addon/keepassxc-browser/"
license=('GPL')
depends=("firefox>=67" "keepassxc")
makedepends=('npm' 'git')
source=('git+https://github.com/keepassxreboot/keepassxc-browser')
md5sums=('SKIP')

pkgver() {
  cd keepassxc-browser
  ( set -o pipefail
    git describe --long --tag 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//'
  )
}

prepare() {
  cd keepassxc-browser
  # updateTranslations() pulls the latest translations from Transifex, and it
  # requires a Transifex API token
  sed -i '/await updateTranslations/d' build.js
}

build() {
  cd keepassxc-browser
  npm ci
  npm run build
}

package() {
  cd "${srcdir}"
  _extension_id="keepassxc-browser@keepassxc.org"
  _extension_dest="${pkgdir}/usr/lib/firefox/browser/extensions/${_extension_id}"
  install -Dm644 keepassxc-browser/keepassxc-browser_*_firefox.zip "${_extension_dest}.xpi"
}
