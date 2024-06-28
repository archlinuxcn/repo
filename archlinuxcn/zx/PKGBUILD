# Maintainer: Dušan Simić <dusan.simic1810@gmail.com>
# Contributor: Alex D'Andrea <alex at dandrea dot io>

pkgname=zx
pkgver=8.1.3
_commit=a3b7316ee6bf5bd954573c1a69770652b82d837d # tags/8.1.3
pkgrel=1
pkgdesc='A tool for writing better scripts'
arch=(any)
url=https://github.com/google/zx
license=(Apache)
depends=('nodejs>=16')
makedepends=(npm git)
source=("git+$url.git#commit=$_commit")
md5sums=('d325ba49143363aa2181b3eb96c85e50')

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

