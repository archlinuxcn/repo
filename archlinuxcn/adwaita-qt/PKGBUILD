# Maintainer: Mark Wagie <mark dot wagie at tutanota dot com>
# Contributor: Victor Homic <aur (at) dothomic (dot) de>
# Contributor: Iyán Méndez Veiga <me (at) iyanmv (dot) com>
# Contributor: Aniket Pradhan <aniket17133 (at) iiitd (dot) ac (dot) in>
# Contributor: Martin Briza <m (at) rtinbriza (dot) cz>

pkgname=('adwaita-qt' 'adwaita-qt6')
pkgbase=adwaita-qt
pkgver=1.4.0+9+g3e55077
pkgrel=1
pkgdesc="A style to bend Qt applications to look like they belong into GNOME Shell"
arch=('x86_64' 'aarch64')
url="https://github.com/FedoraQt/adwaita-qt"
license=('GPL')
depends=('qt5-x11extras' 'qt6-base')
makedepends=('cmake' 'git' 'sassc')
_commit=3e5507748fbd990afad11e6ce99d6d81b5421635
source=("git+https://github.com/FedoraQt/adwaita-qt.git#commit=$_commit")
sha256sums=('SKIP')

pkgver() {
  cd "$srcdir/$pkgbase"
  git describe --tags | sed 's/-/+/g'
}

build() {
  cmake -B build-qt5 -S "$pkgbase" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DUSE_QT6=OFF \
    -Wno-dev
  make -C build-qt5

  cmake -B build-qt6 -S "$pkgbase" \
    -DCMAKE_BUILD_TYPE=None \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DUSE_QT6=ON \
    -Wno-dev
  make -C build-qt6
}

package_adwaita-qt() {
  pkgdesc="A style to bend Qt5 applications to look like they belong into GNOME Shell"
  depends=('qt5-x11extras')
  provides=('libadwaitaqtpriv.so=1' 'libadwaitaqt.so=1')

  make -C build-qt5 DESTDIR="$pkgdir" install
}

package_adwaita-qt6() {
  pkgdesc="A style to bend Qt6 applications to look like they belong into GNOME Shell"
  depends=('libxcb' 'qt6-base')
  provides=('libadwaitaqt6priv.so=1' 'libadwaitaqt6.so=1')

  make -C build-qt6 DESTDIR="$pkgdir" install
}
