# Maintainer: Shatur95 <genaloner@gmail.com>

pkgname=crow-translate
pkgver=2.11.0
pkgrel=1
pkgdesc='A simple and lightweight translator that allows you to translate and speak text using Google, Yandex Bing, LibreTranslate and Lingva'
arch=(x86_64 aarch64)
url=https://github.com/crow-translate/crow-translate
license=(GPL3)
depends=(qt5-svg qt5-multimedia qt5-x11extras kwayland gst-plugins-good openssl tesseract)
makedepends=(qt5-tools extra-cmake-modules)
source=($pkgname-$pkgver.tar.gz::$url/releases/download/$pkgver/$pkgname-$pkgver-source.tar.gz)
sha256sums=(f9557906bda87321b6dbef489fd0bcf90b2ac1e493d2500870b1c31c953039f8)

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
