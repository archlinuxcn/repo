# Maintainer: Dmitry Kharitonov <darksab0r at gmail com>
# Contributor: Matthias Grosser <mtgrosser at gmx dot net>
# Contributor: Leonard de Ruijter <leonard@aur.archlinux.org>

pkgname=shine
pkgver=3.1.0
pkgrel=3
pkgdesc='Super fast fixed-point MP3 encoder'
arch=('arm' 'i686' 'x86_64')
url="https://github.com/savonet/shine"
source=(https://github.com/savonet/$pkgname/archive/$pkgver.tar.gz)
license=(GPL2)
depends=('glibc')
makedepends=('automake' 'autoconf' 'make' 'libtool')
options=('!libtool' '!strip')
sha256sums=('d2b6d09d670a1585d103ed26ea754be76dd3a07033da0a118e8f586ee2ada5e3')
build() {
	cd "${srcdir}/${pkgname}-${pkgver}"
        ./bootstrap
	./configure --prefix=/usr
        make all
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
}

