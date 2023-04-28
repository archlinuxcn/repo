# Maintainer: j.r <j.r@jugendhacker.de>
pkgname=sonixd
pkgver=0.15.5
pkgrel=1
pkgdesc="A full-featured Subsonic/Jellyfin compatible desktop music player"
arch=('x86_64')
url="https://github.com/jeffvli/sonixd"
license=('GPL3')
depends=('electron22')
makedepends=('yarn' 'asar' 'python3' 'git' 'node-gyp')
conflicts=("$pkgname-bin")
replaces=("$pkgname-bin")
source=("$pkgname-$pkgver.tar.gz::https://github.com/jeffvli/sonixd/archive/refs/tags/v$pkgver.tar.gz"
	"$pkgname"
	"$pkgname.desktop")
sha256sums=('1de05c325a0e86c24f1c917c33f577645481e898d842134e7d5f8e6650916d5e'
            'cd44df72a8c0cbe961150bf449a5676f2b34bb7608c4c81e7b92f1a288ad4da0'
            '9e2e1cce47b594b75b8df7a1cf3a5a6da340dda9d0cfdf2aa305d097fc0bbc7a')

prepare() {
	cd "$pkgname-$pkgver"
	mkdir -p "$srcdir/.electron-gyp"
	touch "$srcdir/.electron-gyp/.yarnrc"

	HOME="$srcdir/.electron-gyp" yarn install --frozen-lockfile --cache-folder="$srcdir/yarn-cache"
}

build() {
	cd "$pkgname-$pkgver"

	_ver="$(</usr/lib/electron22/version)"
	local i686=ia32 x86_64=x64
	export NODE_ENV=production
	yarn build --cache-folder="$srcdir/yarn-cache"
	yarn run --cache-folder="$srcdir/yarn-cache" \
		electron-builder --linux --"${!CARCH}" --dir \
		-c.electronDist=/usr/lib/electron22 \
		-c.electronVersion="$_ver"
}

package() {
	install -Dm755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
	install -Dm755 "$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"

	cd "$pkgname-$pkgver"
	local i686=linux-ia32-unpacked x86_64=linux-unpacked

	install -d "$pkgdir/usr/lib/$pkgname/"

	install -Dm644 "release/${!CARCH}/resources/assets/icons/512x512.png" "$pkgdir/usr/share/pixmaps/$pkgname.png"
	cp -r "release/${!CARCH}/resources/assets" "$pkgdir/usr/lib/$pkgname"
	asar e "release/${!CARCH}/resources/app.asar" "$pkgdir/usr/lib/$pkgname/$pkgname/"
}
