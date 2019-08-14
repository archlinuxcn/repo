#Maintainer: weearc <q19981121@163.com>
pkgname=motrix
pkgver=1.4.1
pkgrel=3
pkgdesc="elegent downloading tool frontend for aria2c,using vue(release version)"
arch=('x86_64')
url="https://github.com/agalwood/Motrix"
license=('MIT')
depends=('electron4' 'aria2')
makedepends=('npm')
conflicts=('motrix-git')

source=("https://github.com/agalwood/Motrix/archive/v$pkgver.tar.gz")

sha256sums=('cd10cd5c704f0d780ff501e2861a316b95c44d11b653045574ae07b9a3ccaa8b')

prepare() {
    sed -i 's/"postinstall"/"ignore"/' "$srcdir/Motrix-$pkgver/package.json"
}

build() {
    cd "$srcdir/Motrix-$pkgver"
    npm_config_cache="$srcdir/npm_cache" npm install
    npm run pack
    npm prune --production
}

package() {
    # makedir
    mkdir -p "$pkgdir/usr/bin"
    mkdir -p "$pkgdir/usr/lib/motrix"
    mkdir -p "$pkgdir/usr/share/applications"
    # install aria2
    install -Dm644 "$srcdir/Motrix-$pkgver/extra/linux/engine/aria2.conf" "$pkgdir/usr/lib/motrix/engine/aria2.conf"
    ln -sf /usr/bin/aria2c "$pkgdir/usr/lib/motrix/engine/aria2c"
    # install js
    cp -r "$srcdir/Motrix-$pkgver/dist" "$pkgdir/usr/lib/motrix/app"
    cp -r "$srcdir/Motrix-$pkgver/node_modules" "$pkgdir/usr/lib/motrix/app/node_modules"
    echo '{"name":"Motrix","version":"v'$pkgver'","main":"./electron/main.js"}' > "$pkgdir/usr/lib/motrix/app/package.json"
    # icon
    install -Dm644 "$srcdir/Motrix-$pkgver/static/512x512.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/motrix.png"
    # launch script
    echo "#!/bin/bash
export ELECTRON_IS_DEV=0
exec /usr/bin/electron /usr/lib/motrix/app
    " > "$pkgdir/usr/bin/motrix"
    chmod +x "$pkgdir/usr/bin/motrix"
    # desktop file
    echo "[Desktop Entry]
Name=Motrix
Comment=A full-featured download manager.
Exec=/usr/bin/motrix
Icon=motrix
Type=Application
Categories=Network;FileTransfer;
MimeType=application/x-bittorrent;x-scheme-handler/mo;x-scheme-handler/motrix;x-scheme-handler/magnet;x-scheme-handler/thunder;
Categories=Network;
    " > "$pkgdir/usr/share/applications/motrix.desktop"
}
