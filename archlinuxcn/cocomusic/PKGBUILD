# Maintainer: Bruce Zhang
# Maintainer: WhiredPlanck

pkgname=cocomusic
_name=CoCoMusic
nodeversion=8
pkgver=2.0.7
pkgrel=1
pkgdesc="A simple music player built by electron and vue"
arch=('x86_64' 'i686')
url="https://github.com/xtuJSer/CoCoMusic"
license=('LGPL')
depends=('electron4')
makedepends=('npm' 'jq' 'moreutils' 'nvm')
provides=('cocomusic')
source=("$pkgname-$pkgver.tar.gz::https://github.com/xtuJSer/CoCoMusic/archive/V$pkgver.tar.gz")
sha256sums=('1f73ed4e11a0c87c9d3efea2a1505338883dd887ecf0d1e886e6f697dec0e817')

prepare() {
	cd "$_name-$pkgver"

	local cache="$srcdir/npm-cache"
    local dist=/usr/lib/electron4

	jq '.build.electronDist = $dist | .build.electronVersion = $version | .devDependencies.electron = $version' \
        --arg dist "$dist" \
        --arg version "$(sed s/^v// $dist/version)" \
        package.json | sponge package.json

	# Setting up node 8
	source /usr/share/nvm/init-nvm.sh
	nvm install "$nodeversion"
	nvm use "$nodeversion"

	npm install --cache "$cache"
}

build() {
	cd "$_name-$pkgver"

	./node_modules/.bin/electron-rebuild
	npm run build:dir

	# Deactivate nvm
	source /usr/share/nvm/init-nvm.sh
	nvm deactivate
	nvm uninstall "$nodeversion"
}

package() {
	cd "$srcdir/$_name-$pkgver/build/linux-unpacked/resources"
	install -Dm644 app.asar "$pkgdir/usr/lib/cocomusic/app.asar"

	cd "$srcdir/$_name-$pkgver/build/icons"
	install -Dm644 32x32.png "$pkgdir/usr/share/icons/hicolor/32x32/apps/cocomusic.png"
	install -Dm644 256x256.png "$pkgdir/usr/share/icons/hicolor/256x256/apps/cocomusic.png"

	cd "$srcdir"
	echo "[Desktop Entry]
Name=CocoMusic
Comment=a simple music player.
Exec=cocomusic %U
Terminal=false
Type=Application
Icon=cocomusic
StartupWMClass=CocoMusic
Categories=AudioVideo;Audio;Player;Music;
" > "$srcdir/cocomusic.desktop"
	echo "#!/usr/bin/env sh
exec electron4 /usr/lib/cocomusic/app.asar \$@
" > "$srcdir/cocomusic.sh"

	install -Dm755 "$srcdir/cocomusic.sh" "$pkgdir/usr/bin/cocomusic"
	install -Dm644 "$srcdir/cocomusic.desktop" "$pkgdir/usr/share/applications/cocomusic.desktop"
}
