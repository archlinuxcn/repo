# Maintainer: Daniel Ruiz de Alegría <daniel@drasite.com>

pkgname="flat-remix-gnome"
pkgver=20220622
pkgrel=1
pkgdesc="Flat Remix is a GNOME Shell theme inspired by material design. It is mostly flat using a colorful palette with some shadows, highlights, and gradients for some depth."
arch=('any')
depends=('gnome-shell' 'make' 'glib2' 'imagemagick')
install=flat-remix-gnome.install
url="https://drasite.com/flat-remix-gnome"
license=('CC-BY-SA-4.0')
options=('!strip')
source=("https://github.com/daniruiz/${pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('SKIP')

package() {
	cd "${srcdir}/${pkgname}-${pkgver}/"
	make install DESTDIR=${pkgdir}
}
