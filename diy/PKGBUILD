# Maintainer: Boqun Feng <fixme AT archlinuxcn dot org>
pkgname=diy
pkgver=7.01
pkgrel=1
pkgdesc='The sofware suite provides tools to design and test weak memory models.'
arch=('i686' 'x86_64')
url='http://coq.inria.fr/'
license=('CeCiLL-B')
makedepends=('ocaml>=4.01')
source=("http://diy.inria.fr/sources/diy.tar.gz")
sha1sums=("1777d0bcf224cf7e02a77337494b3b7a8aae78c4")

build() {
	cd ${srcdir}/diy-$pkgver
	make all
}

package() {
	cd ${srcdir}/diy-${pkgver}
	make PREFIX="${pkgdir}/usr" install

	install -Dm644 LICENSE.txt ${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.txt

}
