# Maintainer:
# Contributor: dorphell <dorphell@archlinux.org>
# Contributor: Jochem Kossen <j.kossen@home.nl>

pkgname=cd-discid
pkgver=1.4
pkgrel=3
pkgdesc="A backend utility to get CDDB discid information from a CD-ROM disc"
arch=('x86_64')
url="http://linukz.org/cd-discid.shtml"
license=('GPL')
depends=('glibc')
source=("http://linukz.org/download/${pkgname}-${pkgver}.tar.gz")
sha512sums=('04f3962f7f3f0780c41b2f361397b54efe9c9748643d83311d63f7476d28f9bd295b96dd81f06df2c1e7d6ef095c6732107101c0fb7375fa521f4db67a3984da')

build() {
  cd $pkgname-$pkgver
  make
}

package() {
  cd $pkgname-$pkgver
  make DESTDIR="${pkgdir}" PREFIX=/usr STRIP="/usr/bin/true" install
}
