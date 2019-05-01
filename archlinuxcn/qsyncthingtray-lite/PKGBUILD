# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>
# Contributor: xduugu
# Contributor: MrSerenity
# Contributor: derlafff (aur@2-47.ru)
# Contributor: Doron Behar <doron.behar@gmail.com>

pkgname=qsyncthingtray-lite
_pkgname=QSyncthingTray
pkgver=0.5.8.r13.g3168f48
_commit=3168f48188591624c4972881889249a715981ea2
pkgrel=1
pkgdesc="tray app for syncthing - without the default embedded web interface"
arch=('i686' 'x86_64')
url="https://github.com/sieren/QSyncthingTray"
license=('LGPL3')
depends=('qt5-base')
provides=("qsyncthingtray=$pkgver")
conflicts=('qsyncthingtray')
makedepends=('cmake' 'git')
source=("git+https://github.com/sieren/$_pkgname#commit=$_commit"
        "$pkgname.desktop")
sha256sums=('SKIP'
            '36227ff042cd290c5a5165e63aefa759b08524d508fb5d81558ea2e88f7c731d')

pkgver() {
  cd $_pkgname
  ( set -o pipefail
    git describe --long --tag 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//'
  )
}

prepare() {
  cd $_pkgname
  mkdir build
}

build() {
  cd $_pkgname/build
  cmake -DQST_BUILD_NATIVEBROWSER=1 ..
  make
}

package() {
  cd $_pkgname
  install -Dm755 "build/$_pkgname" "$pkgdir/usr/bin/$_pkgname"

  # install .desktop file
  install -Dm755 "$srcdir/$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
  install -Dm644 "resources/images/Icon1024.png" "$pkgdir/usr/share/pixmaps/qsyncthingtray.png"
}
