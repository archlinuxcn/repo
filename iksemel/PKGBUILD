# $Id: PKGBUILD 55571 2011-09-14 10:35:20Z andrea $
# Maintainer: Mateusz Herych <heniekk@gmail.com>
# Contributor: Roman Kyrylych <Roman.Kyrylych@gmail.com>
# Contributor: Guillermo Vaya driadan@willinux.net

pkgname=iksemel
pkgver=1.4
pkgrel=2
pkgdesc="XML parser library for Jabber applications in ANSI C"
arch=('i686' 'x86_64')
url="http://code.google.com/p/iksemel/"
license=('LGPL')
depends=('glibc')
install=iksemel.install
source=("http://iksemel.googlecode.com/files/${pkgname}-$pkgver.tar.gz")
md5sums=('532e77181694f87ad5eb59435d11c1ca')
options=('!libtool')

build() {
  cd "${srcdir}"/$pkgname-$pkgver
  ./configure --prefix=/usr \
  	--infodir=/usr/share/info
  make
}

package() {
  cd "${srcdir}"/$pkgname-$pkgver
  make DESTDIR="${pkgdir}" install
  mv "${pkgdir}"/usr/share/info/$pkgname "${pkgdir}"/usr/share/info/$pkgname.info
  rm -rf "${pkgdir}"/usr/share/info/dir
}
