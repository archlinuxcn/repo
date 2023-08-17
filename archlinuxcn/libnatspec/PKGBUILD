# Maintainer: Natrio <natrio@list.ru>
# Contributor: Aliaksandr Stelmachonak <mail.avatar@gmail.com>
# Contributor: Evgeny Kurnevsky <kurnevsky@gmail.com>

pkgname=libnatspec
pkgver=0.3.3
_altver="$pkgver-alt1"
pkgrel=1
pkgdesc="A collection of functions for request various charsets and locales for host system and for other system."
arch=('i686' 'x86_64' 'armv7h' 'armv6h')
url="https://github.com/Etersoft/libnatspec"
license=('LGPL')
makedepends=('popt')
optdepends=('popt: natspec tool')
source=(
"https://github.com/Etersoft/libnatspec/archive/refs/tags/${_altver}.tar.gz"
)
sha512sums=(
'8313fffe93b54f7613937216bd46065f545d36c4d93ecd1cfa66dd6de027eb6dbd0eae734f449e0fc66421a783f3a82d16631c10bd233bb94dcbea048aeacfb6'
)

build() {
 cd ${srcdir}/${pkgname}-${_altver}
 autoreconf -fiv
 ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var
 make
}

package() {
 cd ${srcdir}/${pkgname}-${_altver}
 make DESTDIR="${pkgdir}" install
}
