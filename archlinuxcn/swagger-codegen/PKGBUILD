# Maintainer: Xuanwo <xuanwo@archlinuxcn.org>
# Contributor: Ondrej Kucera <ondrej.kucera@centrum.cz>
pkgname=swagger-codegen
pkgver=3.0.7
pkgrel=1
pkgdesc="Swagger Code Generator"
arch=("any")
url="https://github.com/swagger-api/swagger-codegen"
license=("Apache")
depends=('java-runtime')
makedepends=('maven')
provides=('swagger-codegen-cli')
source=($pkgname-${pkgver}.tar.gz::https://github.com/swagger-api/swagger-codegen/archive/v$pkgver.tar.gz
       swagger-codegen)
sha256sums=('4df70e638d1ce9023165c909827dd1cd02bbec1ae5756a4bb7891a0747886d66'
            '6a876066f7433d1e5b812c63817eff122804db37b2fd79c5013d79844b2b8828')

build() {
  cd $srcdir/$pkgname-${pkgver}
  mvn clean package
}

package() {
  install -Dm644 "$srcdir/$pkgname-${pkgver}/modules/swagger-codegen-cli/target/swagger-codegen-cli.jar" "$pkgdir/usr/share/swagger-codegen/swagger-codegen-cli.jar"
  install -Dm755 swagger-codegen "$pkgdir/usr/bin/swagger-codegen"
}

# vim: ft=sh syn=sh et

