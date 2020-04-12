# Maintainer: Xuanwo <xuanwo@archlinuxcn.org>
pkgname=docsify-cli
pkgver=4.4.0
pkgrel=1
pkgdesc="A magical documentation generator."
arch=(any)
url="https://github.com/docsifyjs/docsify-cli"
license=('MIT')
depends=('nodejs')
makedepends=('npm')
provides=('docsify')
source=("https://registry.npmjs.org/$pkgname/-/$pkgname-$pkgver.tgz")
noextract=($pkgname-$pkgver.tgz)
sha256sums=('0b98c2e9c33630816d3a33517e7bdd65780c714d904914e4514fd4b21c6dcd44')
options=(!strip)

package() {
  npm install -g --prefix "$pkgdir/usr" $pkgname-$pkgver.tgz

  cd "$pkgdir"/usr

  # Fix permissions
  find . -exec chown -h 0:0 {} +
  find . -type d -exec chmod 755 {} +

  install -Dm 644 lib/node_modules/$pkgname/LICENSE -t share/licenses/$pkgname
}
