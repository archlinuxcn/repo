# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org>
# Contributor: Zen Wen <zen.8841@gmail.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=qt5-webkit
_pkgver=5.212.0-alpha4
_basever=5.15.3
pkgver=${_pkgver/-/}
pkgrel=20
arch=(x86_64)
url='https://github.com/qtwebkit/qtwebkit'
license=(GPL3 LGPL3 FDL custom)
pkgdesc='Classes for a WebKit2 based implementation and a new QML API'
source=("https://github.com/qtwebkit/qtwebkit/releases/download/qtwebkit-$_pkgver/qtwebkit-$_pkgver.tar.xz"
        "https://src.fedoraproject.org/rpms/qt5-qtwebkit/raw/rawhide/f/qtwebkit-cstdint.patch"
         icu68.patch
         glib-2.68.patch
         qt5-webkit-python-3.9.patch
         qt5-webkit-bison-3.7.patch)
depends=(qt5-location qt5-sensors qt5-webchannel libwebp libxslt libxcomposite gst-plugins-base hyphen woff2)
makedepends=(cmake ruby gperf python qt5-doc qt5-tools)
optdepends=('gst-plugins-good: Webm codec support')
sha256sums=('9ca126da9273664dd23a3ccd0c9bebceb7bb534bddd743db31caf6a5a6d4a9e6'
            '4c71c958eae45cae65c9f002024eb1369d06029b668e595158138ff7971e64f1'
            '0b40ed924f03ff6081af610bb0ee01560b7bd1fb68f8af02053304a01d4ccdf0'
            '4969dd03e482155e2490b50307dada81dda7bbc9e5398e3a53c20bc474f7c04e'
            '6e0cee08e4fa57b04752e80817f33562f48aa42608a3a620930b6040259b4932'
            '34f37b53ee0bc31c63ce85ebd1ae95543a8ba28483e387b20efd50574bd813be')
options=(!lto)

prepare() {
  cd qtwebkit-$_pkgver
  patch -p0 -i ../icu68.patch # Fix build with ICU 68.x
  patch -p1 -i ../glib-2.68.patch # https://github.com/qtwebkit/qtwebkit/issues/1057
  patch -p1 -i ../qt5-webkit-python-3.9.patch # Fix build with python 3.9
  patch -p1 -i ../qt5-webkit-bison-3.7.patch # Fix build with bison 3.7
  patch -p1 -i ../qtwebkit-cstdint.patch # gcc 11.1
}

build() {
  cmake -B build -S qtwebkit-$_pkgver \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_CXX_FLAGS="${CXXFLAGS} -DNDEBUG" \
    -DPORT=Qt \
    -DENABLE_TOOLS=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

  install -d "$pkgdir"/usr/share/licenses
  ln -s /usr/share/licenses/qt5-base "$pkgdir"/usr/share/licenses/${pkgname}
}
