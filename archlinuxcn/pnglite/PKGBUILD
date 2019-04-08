# Maintainer: heinrich5991 <heinrich5991@gmail.com>
# system-zlib.patch taken from the Debian package
pkgname=pnglite
pkgver=0.1.17
pkgrel=1
pkgdesc="Lightweight PNG C library"
arch=('x86' 'x86_64')
url="https://sourceforge.net/projects/pnglite/"
license=('BSD')
depends=()
options=()
source=(
  "https://downloads.sourceforge.net/project/pnglite/pnglite/0.1.17/pnglite-0.1.17.zip"
  "system-zlib.patch"
)
sha256sums=('6444b13b9ec5b6f9de8f72513a00870325779e3b05bfcf554edb1ab0c90f5962'
            '70aea0718f90a35df50ff33dd85032be72b3fddfe539382f93d4796df1b7c5b9')

prepare() {
  patch -p1 < system-zlib.patch
}

build() {
  gcc -shared -fPIC -Wall -o libpnglite.so -lz pnglite.c
}

package() {
  install -Dm644 pnglite.h "${pkgdir}"/usr/include/pnglite.h
  install -Dm755 libpnglite.so "${pkgdir}"/usr/lib/libpnglite.so
}
