# Maintainer: Yuzu <aur at vitayuzu dot day>
pkgname=iloader-bin
pkgver=1.1.5
pkgrel=3
pkgdesc="User friendly sideloader"
arch=(x86_64)
url="https://github.com/nab138/iloader"
license=("MIT")
depends=(usbmuxd webkit2gtk-4.1 gtk3 cairo glibc glib2 libsoup3 hicolor-icon-theme gdk-pixbuf2 gcc-libs)
conflicts=(iloader-appimage)
source=("${pkgname}-${pkgver}.deb::$url/releases/download/v$pkgver/iloader-linux-amd64.deb"
        "${pkgname}-${pkgver}-LICENSE::$url/raw/refs/heads/main/LICENSE")
sha256sums=('5d26a44dc7ffb99fa736c79da5ef74beb5a0cb9d06d141a797b24ad3db75c4e8'
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
