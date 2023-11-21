# Maintainer: Yufan You <ouuansteve at gmail>
# Contributor: Luis Martinez <luis dot martinez at disroot dot org>
# Contributor: Shatur95 <genaloner@gmail.com>

pkgname=vim-language-server
pkgver=2.3.1
pkgrel=1
pkgdesc="VimScript language server, LSP for vim script"
arch=('any')
url="https://github.com/iamcco/vim-language-server"
license=('MIT')
depends=('nodejs')
makedepends=('npm')
source=("$pkgname-$pkgver.tgz::https://registry.npmjs.org/$pkgname/-/$pkgname-$pkgver.tgz")
noextract=("$pkgname-$pkgver.tgz")
sha256sums=('ffe0d18258a4b09bec46ec853f8838748c007c62c1fcf12d1eefedfaf19e1c46')

package() {
	export NODE_ENV=production
	npm install -g --cache "$srcdir/npm-cache" --prefix "$pkgdir/usr" "$pkgname-$pkgver.tgz"
	chown -R root:root "$pkgdir"
	## why does !emptydirs run after PURGE_TARGETS
	rm -rf "$pkgdir/usr/lib/node_modules/vim-language-server/.github/"
}
