# Maintainer: sum01 <sum01@protonmail.com>
pkgname=rocketchat-desktop
pkgver=2.11.0
_srcname="Rocket.Chat.Electron-$pkgver"
pkgrel=3
pkgdesc='Rocket.Chat Native Cross-Platform Desktop Application via Electron.'
arch=('i686' 'x86_64')
url="https://github.com/RocketChat/Rocket.Chat.Electron"
license=('MIT')
depends=('nss' 'libxss' 'gconf' 'gtk3')
makedepends=('sed' 'yarn>=0.21.3' 'nodejs>=7.0.0' 'node-gyp' 'python2')
conflicts=('rocketchat-client-bin')
source=("$pkgname-$pkgver.tar.gz::https://github.com/RocketChat/Rocket.Chat.Electron/archive/$pkgver.tar.gz")
sha512sums=('660ba9e38d0d319fc18710e47b6979ca907135c9cd893b19df830fa01587956eba833fadd165919e568fe76d8055209f6a13344fb6daf8f094527f84ae7a0ca4')
prepare() {
	sed -i 's/"deb",/"dir"/' "$srcdir/$_srcname/package.json"
	sed -i '/"rpm"/d' "$srcdir/$_srcname/package.json"
	sed -i 's|${SNAP}/meta/gui/icon.png|rocketchat-desktop|' "$srcdir/$_srcname/snap/gui/$pkgname.desktop"
}
build() {
	cd "$srcdir/$_srcname"
	yarn install --non-interactive --pure-lockfile --cache-folder "$srcdir/yarn-cache"
	yarn release
}
package() {
	install -Dm644 "$srcdir/$_srcname/snap/gui/icon.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/$pkgname.png"
	install -Dm644 "$srcdir/$_srcname/snap/gui/$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname/$pkgname.desktop"
	install -Dm644 "$srcdir/$_srcname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
	if [[ $CARCH == "i686" ]]; then
		_distname="linux-ia32-unpacked"
	else
		_distname="linux-unpacked"
	fi
	mkdir -p "$pkgdir"/{usr/bin,opt}
	cp -rf "$srcdir/$_srcname/dist/$_distname" "$pkgdir/opt/$pkgname"
	ln -sf /opt/$pkgname/rocketchat "$pkgdir/usr/bin/$pkgname"
}
