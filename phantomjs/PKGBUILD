# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Dieter Plaetinck <dieter@plaetinck.be>
# Contributor: Vladimir Chizhov <jagoterr@gmail.com>
# Contributor: Henry Tang <henryykt@gmail.com>

pkgname=phantomjs
pkgver=2.1.1
pkgrel=12
pkgdesc='Headless WebKit with JavaScript API'
url='http://www.phantomjs.org/'
license=('BSD' 'LGPL' 'MIT')
arch=('i686' 'x86_64')
depends=('icu' 'libjpeg-turbo' 'libpng' 'fontconfig' 'gperf' 'ruby' 'python2' 'openssl-1.0')
makedepends=('git')
_qtbase_commit=b5cc0083a5766e773885e8dd624c51a967c17de0
_qtwebkit_commit=e7b74331d695bfa8b77e39cdc50fc2d84a49a22a
source=("$pkgname-$pkgver.tar.gz"::"https://github.com/ariya/phantomjs/archive/$pkgver.tar.gz"
        "$pkgname-qtbase-$_qtbase_commit.tar.gz"::"https://github.com/Vitallium/qtbase/archive/$_qtbase_commit.tar.gz"
        "$pkgname-qtwebkit-$_qtwebkit_commit.tar.gz"::"https://github.com/Vitallium/qtwebkit/archive/$_qtwebkit_commit.tar.gz"
        icu59.patch)
sha512sums=('07b769133957c5194c9afdaa347bd9a019ebe47653f98adf17a35d3dd12714d2f8e3773ced91d7d99f31cb18d7f73167022d5b0a3906d9aac0732ef96341f5ec'
            'bdbe5fe69a5b0348632cfc9cd21c49c7334c34ecf9a603e3f94d3f456e6327b3036c00a05d37f064d49788ae062adfcf25f2258083d3099f7ee1ce6d3ed813e8'
            '232f7060509a6615a2cd4fe71f22b32cf4b25f32a46d4dc3fa9e22d8c396c90389aabb63d43c76005bb779820f5d5555dbeb0d30054e1780619e0efd1807b272'
            'e349a14c5d32e5627f28be6ebd20104370ec6b7f086f670e7f19b484b38839220cfeb49178765f38d918d05fb889bbc990f8a3809db6d9e1cbde0af5b9dd923b')

prepare() {
  cd $pkgname-$pkgver

  rmdir src/qt/qt{base,webkit}
  ln -s ../../../qtbase-$_qtbase_commit src/qt/qtbase
  ln -s ../../../qtwebkit-$_qtwebkit_commit src/qt/qtwebkit

  patch -Np1 -d src/qt/qtwebkit <../icu59.patch
  mkdir "$srcdir/python2-path"
  ln -s /usr/bin/python2 "$srcdir/python2-path/python"

  # syncqt creates forwarded header files (include/QtCore/...). Normally, it's
  # run in git checkouts and skipped in stable versions as forwarded headers
  # are pre-generated. In this package, Qt mistakenly thinks this is a stable
  # version as .git is missing, so we need to run this command manually.
  cd src/qt/qtbase
  ./bin/syncqt.pl -minimal -module QtCore "$srcdir/$pkgname-$pkgver/src/qt/qtbase"
}

build() {
  cd $pkgname-$pkgver
  export PATH="$srcdir/python2-path:$PATH"
  export PYTHON=/usr/bin/python2
  export CXXFLAGS+=' -I/usr/include/openssl-1.0'
  export OPENSSL_LIBS='-L/usr/lib/openssl-1.0 -lssl -lcrypto'

  CFLAGS+=' -Wno-expansion-to-defined'
  CXXFLAGS+=' -Wno-expansion-to-defined'

  python2 build.py --confirm --release --qt-config='-no-rpath' --qt-config='-verbose'
}

package() {
  cd $pkgname-$pkgver
  install -Dm755 bin/phantomjs "$pkgdir/usr/bin/phantomjs"

  mkdir -p "$pkgdir/usr/share/$pkgname"
  cp -r examples "$pkgdir/usr/share/$pkgname/"

  install -Dm644 LICENSE.BSD "$pkgdir/usr/share/licenses/$pkgname/LICENSE.BSD"
  install -Dm644 third-party.txt "$pkgdir/usr/share/licenses/$pkgname/third-party.txt"
}

