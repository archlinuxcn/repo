# Maintainer: Doug Newgard <scimmia at archlinux dot info>
# Contributor: Jameson Pugh <imntreal@gmail.com>

_pkgname=onedrive
pkgname=$_pkgname-git
pkgver=1.1.3.r0.g945251f
pkgrel=1
epoch=1
pkgdesc='Free OneDrive client written in D'
arch=('i686' 'x86_64')
url='https://github.com/skilion/onedrive'
license=('GPL3')
depends=('curl' 'gcc-libs' 'glibc' 'sqlite')
makedepends=('dmd' 'git')
provides=("onedrive=$pkgver")
conflicts=('onedrive')
source=('git+https://github.com/skilion/onedrive.git')
sha256sums=('SKIP')

pkgver() {
  cd $_pkgname

  git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  make PREFIX=/usr -C $_pkgname
}

package() {
  make PREFIX=/usr DESTDIR="$pkgdir" -C $_pkgname install
  install -Dm644 $_pkgname/config "$pkgdir/usr/share/onedrive/config.default"
}
