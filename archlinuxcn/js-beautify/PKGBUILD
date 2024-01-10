pkgname=js-beautify
pkgver=1.14.11
pkgrel=1
pkgdesc="CSS, HTML & JavaScript unobfuscator and beautifier"
arch=('any')
url="https://beautifier.io"
license=('MIT')
depends=('nodejs')
makedepends=('npm')
conflicts=('python-cssbeautifier' 'python-jsbeautifier')
source=("https://registry.npmjs.org/js-beautify/-/$pkgname-$pkgver.tgz")
noextract=("$pkgname-$pkgver.tgz")
sha256sums=('8cf92c33b53ce362e580b14c2352aff3fae8b2bd681ea6c9a81d9ef69951e254')

package() {
  npm install -g --prefix "$pkgdir/usr" "$pkgname-$pkgver.tgz"

  # npm gives ownership of ALL FILES to build user
  # https://bugs.archlinux.org/task/63396
  chown -R root:root "$pkgdir"

  install -d "$pkgdir/usr/share/licenses/$pkgname"
  ln -s "/usr/lib/node_modules/$pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/"
}
