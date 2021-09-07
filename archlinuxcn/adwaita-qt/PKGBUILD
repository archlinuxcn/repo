# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: Victor Homic <aur (at) dothomic (dot) de>
# Contributor: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Aniket Pradhan <aniket17133 (at) iiitd (dot) ac (dot) in>
# Contributor: Martin Briza <m (at) rtinbriza (dot) cz>

pkgname=adwaita-qt
pkgver=1.4.0
pkgrel=1
pkgdesc="A style to bend Qt applications to look like they belong into GNOME Shell"
arch=('x86_64')
url="https://github.com/FedoraQt/adwaita-qt"
license=('GPL')
depends=('qt5-x11extras')
makedepends=('cmake')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('f6ddfaf59f2c25f3401e1244c1e02733dc2079420d40452e5b2cbe45849c31d3')

build() {
  cmake -B build -S "$pkgname-$pkgver" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -Wno-dev
  make -C build
}

package() {
  make -C build DESTDIR="$pkgdir" install
}
