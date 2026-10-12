# Maintainer: Jonathan Grotelüschen <tippfehlr@archlinux.org>

pkgname=ocx
pkgver=2.0.15
pkgrel=1
pkgdesc="OpenCode extension manager with portable, isolated profiles. Your setup, anywhere."
arch=(any)
url="https://github.com/kdcokenny/ocx"
license=(MIT)
depends=(bun)
makedepends=(git)
source=("git+$url#tag=v$pkgver")
sha256sums=('6c1ba430a925a2459618918854994acfe8c2e300bde13f28dbb7eb49f797387a')

prepare() {
	cd $pkgname
	bun install --frozen-lockfile
}

build() {
	cd $pkgname/packages/cli
	bun run build
}

check() {
	cd $pkgname
	bun run check
	bun run test
}

package() {
	cd $pkgname
	install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"

	cd packages/cli
	install -Dm755 dist/index.js "$pkgdir/usr/bin/ocx"
}
