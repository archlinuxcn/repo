# Maintainer: Shatur95 <genaloner@gmail.com>

pkgname=crow-translate
pkgver=2.8.3
pkgrel=1
pkgdesc='A simple and lightweight translator that allows to translate and say selected text using Google, Yandex and Bing translate API'
arch=(x86_64 aarch64)
url=https://github.com/crow-translate/crow-translate
license=(GPL3)
depends=(qt5-base qt5-svg qt5-multimedia qt5-x11extras gst-plugins-good openssl tesseract)
makedepends=(git qt5-tools extra-cmake-modules)
source=($pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz)
sha256sums=(1b2607ca89bf53d8907638028534de4a1f4394146cc2c9f85ffed4aded73d8b5)

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
