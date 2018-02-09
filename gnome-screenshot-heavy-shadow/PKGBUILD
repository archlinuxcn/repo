# Maintainer: Brandon <aur at everdream.xyz>

pkgname=gnome-screenshot-heavy-shadow
pkgver=3.25.0
pkgrel=1
pkgdesc="Take pictures of your screen, with modified shadow effect"
arch=('any')
url="https://github.com/Cabbagec/gnome-screenshot-heavy-shadow"
license=('GPL2')
groups=('gnome')
depends=('dconf' 'gtk3' 'libcanberra')
makedepends=('meson' 'appstream-glib' 'git')
provides=('gnome-screenshot')
conflicts=('gnome-screenshot' 'gnome-screenshot-git')
source=("git+https://github.com/Cabbagec/gnome-screenshot-heavy-shadow#branch=master")
sha256sums=('SKIP')

build() {
	cd "$pkgname"
	./configure --prefix=/usr
	make
}

package() {
	cd "$pkgname"
	make DESTDIR="$pkgdir/" install
}
