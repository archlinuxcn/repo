# Maintainer: Dušan Simić <dusan.simic1810@gmail.com>
# Contributor: Alex D'Andrea <alex at dandrea dot io>

pkgname=zx
pkgver=8.2.2
pkgrel=1
pkgdesc='A tool for writing better scripts'
arch=(any)
url=https://github.com/google/zx
license=(Apache-2.0)
depends=('nodejs>=16')
makedepends=(npm git)
source=("git+$url.git#tag=$pkgver")
sha256sums=('7b20691422fd91c27c107c311b5a92903b34ff94cc5c59e9097b8b6b5c7cd32a')

build() {
	cd "$pkgname"
	npm install --cache "$srcdir/npm-cache"
	npm run build
}

package() {
	cd "$pkgname"

	local _npmdir="$pkgdir/usr/lib/node_modules"
	install -d "$_npmdir/$pkgname"
	cp -r build/ package.json "$_npmdir/$pkgname"

	mkdir -p "$pkgdir/usr/bin"
	ln -s "$(realpath -m --relative-to=/usr/bin /usr/lib/node_modules/$pkgname/build/cli.js)" "$pkgdir/usr/bin/zx"
	chmod 0755 "$pkgdir/usr/bin/zx"

	install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

