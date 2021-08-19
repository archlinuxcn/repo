# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=gnome-shell-extension-shuzhi
_pkgname=shuzhi
pkgver=40.1
pkgrel=2
pkgdesc="A wallpaper generation extension for gnome shell, inspired by Jizhi."
arch=('any')
url="https://github.com/tuberry/shuzhi"
license=('GPL3')
depends=('gnome-shell')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha512sums=('88d6b78567c182a4813c8da16f578b2e623ddf75770b081605300a94b752cd2d648ecb3102d0c5d732ccd4825f53a442ca88d596e7c7e523d5f6d493e6051f94')

build() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	make
}

package() {
	cd "${srcdir}/${_pkgname}-${pkgver}"
	make DESTDIR="${pkgdir}/" install
}
