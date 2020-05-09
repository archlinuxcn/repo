# Maintainer: Anton Kudelin <kudelin at protonmail dot com>
# Contributor: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Daniel Nagy <danielnagy at gmx de>
# Contributor: grimsock <lord.grimsock at gmail dot com>
# Contributor: Alucryd <alucryd at gmail dot com>

_pkgname=testng
pkgname=java-${_pkgname}
pkgver=7.1.1
pkgrel=1
pkgdesc='A testing framework inspired by JUnit and NUnit'
arch=('any')
url="http://testng.org"
license=('Apache')
depends=("jdk8-openjdk" "java-runtime")
source=("https://github.com/cbeust/$_pkgname/archive/$pkgver.tar.gz")
sha256sums=('56a276d405f0e17770b0341d54d5d47dc08bbd6d59d0406f2f0fa18895e08ca7')

build() {
  cd "$srcdir/$_pkgname-$pkgver"
  ./gradlew --daemon clean build
}

check() {
  cd "$srcdir/$_pkgname-$pkgver"
  ./gradlew --daemon test
}

package() {
  install -Dm644 \
    "$srcdir/$_pkgname-$pkgver/build/libs/$_pkgname-$pkgver-SNAPSHOT.jar" \
    "$pkgdir/usr/share/java/$_pkgname/$_pkgname-$pkgver.jar"
}
