# Maintainer: Shatur95 <genaloner@gmail.com>

pkgname=crow-translate
pkgver=2.9.1
pkgrel=1
pkgdesc='A simple and lightweight translator that allows you to translate and speak text using Google, Yandex Bing, LibreTranslate and Lingva'
arch=(x86_64 aarch64)
url=https://github.com/crow-translate/crow-translate
license=(GPL3)
depends=(qt5-svg qt5-multimedia qt5-x11extras gst-plugins-good openssl tesseract)
makedepends=(git qt5-tools extra-cmake-modules)
source=($pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz)
sha256sums=(d73f9289231ee15654f6e1fc7349e86d83ccd75e98b7eb5477a647139d48f4ed)

build() {
  cd $pkgname-$pkgver

  cmake -B build -D CMAKE_INSTALL_PREFIX="$pkgdir/usr"
  cmake --build build
}

package() {
  cd $pkgname-$pkgver

  cmake --install build
  rm -f "${pkgdir}/usr/share/icons/hicolor/icon-theme.cache"
} 
