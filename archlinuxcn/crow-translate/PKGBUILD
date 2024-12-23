# Maintainer: Shatur95 <genaloner@gmail.com>

pkgname=crow-translate
pkgver=3.1.0
pkgrel=1
pkgdesc='Application that allows you to translate and speak text'
arch=(x86_64 aarch64)
url=https://apps.kde.org/crowtranslate/
license=(GPL-3.0-or-later)
depends=(qt5-svg qt5-multimedia qt5-x11extras kwayland5 gst-plugins-good openssl tesseract)
makedepends=(qt5-tools extra-cmake-modules)
source=(https://download.kde.org/stable/$pkgname/$pkgver/$pkgname-v$pkgver.tar.gz)
sha256sums=(8cafa4a812079020839beaf0b133e08be6e47d6ffa1cf90f3417efdc7589c7a1)

build() {
  cd $pkgname-v$pkgver

  cmake -B build -D CMAKE_INSTALL_PREFIX="$pkgdir/usr"
  cmake --build build
}

package() {
  cd $pkgname-v$pkgver

  cmake --install build
  rm -f "${pkgdir}/usr/share/icons/hicolor/icon-theme.cache"
} 
