# Maintainer: Integral <integral@murena.io>

pkgname=audiotube
pkgver=23.04.0
pkgrel=1
pkgdesc="Client for YouTube Music"
arch=('x86_64' 'aarch64')
url="https://invent.kde.org/plasma-mobile/audiotube"
license=(GPL3)
depends=('ki18n' 'kirigami2' 'python-ytmusicapi' 'yt-dlp' 'gst-plugins-good' 'qt5-imageformats' 'kcrash' 'purpose')
makedepends=('fakeroot' 'binutils' 'extra-cmake-modules' 'pybind11' 'qt5-svg' 'python-ytmusicapi' 'kirigami-addons')
provides=('audiotube-git')
conflicts=('audiotube-git')
source=("https://github.com/KDE/${pkgname}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('6b45a2c26586906a01874f17cb66563b63e58883793a13fe752fecff5476cd1a')

build() {
  cd "${pkgname}-${pkgver}/"
  cmake -DCMAKE_INSTALL_PREFIX=/usr -B build
  make -C build
}

package() {
  cd "${pkgname}-${pkgver}/"
  make -C build DESTDIR="${pkgdir}" PREFIX=/usr install
}
