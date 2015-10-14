# Maintainer: Natrio <natrio@list.ru>
# Contributor: Aliaksandr Stelmachonak <mail.avatar@gmail.com>
# Contributor: Evgeny Kurnevsky <kurnevsky@gmail.com>

pkgname=libnatspec
pkgver=0.3.0
pkgrel=1
pkgdesc="A collection of functions for request various charsets and locales for host system and for other 
system."
arch=('i686' 'x86_64' 'armv7h' 'armv6h')
url="http://sourceforge.net/projects/natspec/"
license=('LGPL')
source=(
"http://sourceforge.net/projects/natspec/files/natspec/${pkgver}/libnatspec-${pkgver}.tar.bz2"
)
sha512sums=(
'5c04358d20be5b6ffc7038bddd4514c4b5b4e9940fb6247070b832da9d059b31fd1306cf29f54e4a1b8be1d909176bd72e6ffa98e4b750840764f9b2c250d31c'
)

build() {
 cd ${srcdir}/${pkgname}-${pkgver}
 autoreconf -fiv
 ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var
 make
}

package() {
 cd ${srcdir}/${pkgname}-${pkgver}
 make DESTDIR="${pkgdir}" install
}
