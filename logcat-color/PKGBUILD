# Maintainer: Thomas Weißschuh <thomas t-8ch de>

pkgname=logcat-color
pkgver=0.6.0
pkgrel=4
pkgdesc='A colorful alternative to "adb logcat"'
arch=('any')
url='https://github.com/marshall/logcat-color'
license=('Apache')
depends=('python2-colorama')
makedepends=('python2-setuptools')
source=("$pkgname-$pkgver.tar.gz"::"https://github.com/marshall/logcat-color/archive/v$pkgver.tar.gz")
sha256sums=('029e23bcea63b91d099b46c552a379dd5a8eb22cefc1fadf38b7b077f8a74c51')

prepare() {
  cd "$srcdir/logcat-color-${pkgver}"

  sed -i 's#/usr/bin/env python$#/usr/bin/env python2#' logcat-color test/mock-adb
}

build() {
  cd "$srcdir/logcat-color-${pkgver}"
  python2 setup.py build
}

check() {
  cd "$srcdir/logcat-color-${pkgver}"

  python2 test/test.py
}

package() {
  cd "$srcdir/logcat-color-${pkgver}"
  python2 setup.py install --root="$pkgdir/" --optimize=1
}
