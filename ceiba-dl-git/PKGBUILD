# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

_pkgname=ceiba-dl
pkgname=$_pkgname-git
pkgver=0.5.r1.ga977f8d
pkgrel=2
pkgdesc='NTU CEIBA data downloader /  NTU CEIBA 資料下載工具'
arch=(i686 x86_64)
license=(LGPL3)
url='https://github.com/lantw44/ceiba-dl'
depends=('python-lxml' 'python-pycurl' 'python-xdg' 'webkit2gtk>=2.20')
makedepends=('autoconf-archive' 'git')
conflicts=("$_pkgname")
provides=("$_pkgname=$pkgver")
source=('git+https://github.com/lantw44/ceiba-dl')
sha256sums=('SKIP')

pkgver() {
  cd $_pkgname
  ( set -o pipefail
    git describe --long --tag 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g;s/^v//'
  )
}

prepare() {
  cd $_pkgname

  autoreconf -ifv
}

build() {
  cd $_pkgname

  # The default is --enable-compile-warnings=error, which breaks the build
  ./configure \
    --prefix=/usr \
    --enable-compile-warnings=yes

  make
}

package() {
  cd $_pkgname

  make DESTDIR="$pkgdir" install
}
