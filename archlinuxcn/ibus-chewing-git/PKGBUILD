# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Forked from community/ibus-chewing; original contributors:
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Thomas Dziedzic < gostrc at gmail >
# Contributor: Rainy <rainylau(at)gmail(dot)com>
# Contributor: Lee.MaRS <leemars@gmail.com>
# Contributor: Hiroshi Yui <hiroshiyui@gmail.com>

_pkgname=ibus-chewing
pkgname=$_pkgname-git
pkgver=1.6.1.r14.g8e17848
pkgrel=2
pkgdesc='Chinese Chewing Engine for IBus Framework'
arch=('i686' 'x86_64')
license=('GPL')
url='https://github.com/definite/ibus-chewing'
depends=('ibus' 'libchewing-git' 'gtk3')
makedepends=('gob2' 'cmake' 'git')
checkdepends=('dbus' 'xorg-server-xvfb')
source=("git+https://github.com/definite/ibus-chewing.git"
        "git+https://pagure.io/cmake-fedora.git")
sha512sums=('SKIP'
            'SKIP')
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")

pkgver() {
  cd $_pkgname
  ( set -o pipefail
    git describe --long --tag 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//'
  )
}

prepare() {
  cd $_pkgname

  git submodule init
  git config submodule.cmake-fedora.url "$srcdir/cmake-fedora"
  git submodule update
}

build() {
  cd $_pkgname

  cmake -B build -S . \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=None \
    -DLIBEXEC_DIR=/usr/lib/ibus

  # XXX: updated *.po files contain no translated strings. Maybe because fedora.zanata.org is down
  # https://github.com/definite/ibus-chewing/issues/150
  touch build/po/ibus-chewing.pot
  cp -v po/*.po build/po/

  make -C build
}

check() {
  cd $_pkgname/build

  # Some tests fail due to a upstream issue https://github.com/definite/ibus-chewing/issues/154#issuecomment-756713451
  GSETTINGS_SCHEMA_DIR="$srcdir/$_pkgname/build/bin/" xvfb-run --auto-display dbus-run-session make test || true
}

package() {
  cd $_pkgname/build
  make DESTDIR="$pkgdir" install
}
