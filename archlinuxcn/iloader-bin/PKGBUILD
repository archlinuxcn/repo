# Maintainer: Yuzu <aur at vitayuzu dot day>
pkgname=iloader-bin
pkgver=2.0.2
pkgrel=1
pkgdesc="User friendly sideloader"
arch=(x86_64)
url="https://github.com/nab138/iloader"
license=("MIT")
depends=(usbmuxd webkit2gtk-4.1 gtk3 cairo glibc glib2 libsoup3 hicolor-icon-theme gdk-pixbuf2 gcc-libs)
conflicts=(iloader-appimage)
source=("${pkgname}-${pkgver}.deb::$url/releases/download/v$pkgver/iloader-linux-amd64.deb"
        "${pkgname}-${pkgver}-LICENSE::$url/raw/refs/heads/main/LICENSE")
sha256sums=('e7a161302fcd6ce728ece34b6ee7b9c9b5cb04754fc09aa73fe54c3b137e408a'
            'c6e929e3490b6475e382b4f74aaddd068deb3bf27cca2109821591e692dfcb3b')

prepare() {
    tar -xzf data.tar.gz
}

package() {
    install -Dm755 usr/bin/iloader "$pkgdir/usr/bin/iloader"
    install -Dm644 usr/share/applications/iloader.desktop "$pkgdir/usr/share/applications/iloader.desktop"
    install -Dm644 "${pkgname}-${pkgver}-LICENSE" "$pkgdir/usr/share/licenses/iloader-bin/LICENSE"
    mkdir -p "$pkgdir/usr/share/icons/"
    cp -r usr/share/icons/hicolor "$pkgdir/usr/share/icons/"
}
