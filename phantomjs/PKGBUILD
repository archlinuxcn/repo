# $Id$
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Dieter Plaetinck <dieter@plaetinck.be>
# Contributor: Vladimir Chizhov <jagoterr@gmail.com>
# Contributor: Henry Tang <henryykt@gmail.com>

pkgname=phantomjs
pkgver=2.1.1
pkgrel=11
pkgdesc="Headless WebKit with JavaScript API"
url="http://www.phantomjs.org/"
license=('BSD' 'LGPL' 'MIT')
arch=('i686' 'x86_64')
depends=('icu>=61' 'libjpeg-turbo' 'libpng' 'fontconfig' 'gperf' 'ruby' 'python2' 'openssl-1.0')
makedepends=('git')
source=("git+https://github.com/ariya/${pkgname}.git#tag=$pkgver"
        icu59.patch)
sha512sums=('SKIP'
            'e349a14c5d32e5627f28be6ebd20104370ec6b7f086f670e7f19b484b38839220cfeb49178765f38d918d05fb889bbc990f8a3809db6d9e1cbde0af5b9dd923b')

prepare() {
  cd $pkgname
  git submodule update --init
  patch -Np1 -d src/qt/qtwebkit <../icu59.patch
  mkdir "$srcdir/python2-path"
  ln -s /usr/bin/python2 "$srcdir/python2-path/python"
}

build() {
  cd $pkgname
  export PATH="$srcdir/python2-path:$PATH" PYTHON=/usr/bin/python2
  export CXXFLAGS+=" -I/usr/include/openssl-1.0"
  export OPENSSL_LIBS='-L/usr/lib/openssl-1.0 -lssl -lcrypto'

  CFLAGS+=" -Wno-expansion-to-defined"
  CXXFLAGS+=" -Wno-expansion-to-defined"

  python2 build.py --confirm --release --qt-config='-no-rpath'
}

package() {
  install -Dm755 "$srcdir/$pkgname/bin/phantomjs" "$pkgdir/usr/bin/phantomjs"

  mkdir -p "$pkgdir/usr/share/$pkgname"
  cp -r "$srcdir/$pkgname/examples" "$pkgdir/usr/share/$pkgname"/

  install -Dm644 "$srcdir/$pkgname/LICENSE.BSD" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.BSD"
  install -Dm644 "$srcdir/$pkgname/third-party.txt" "$pkgdir/usr/share/licenses/$pkgname/third-party.txt"
}

