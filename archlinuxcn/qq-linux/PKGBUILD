# Maintainer: Jack Wu (OriginCode) <self@origincode.me>

pkgname=qq-linux
pkgver=2.0.0_b2_1082
pkgrel=1
arch=('x86_64')
pkgdesc="Tencent QQ for Linux"
url="https://im.qq.com/linuxqq"
depends=('gtk2' 'glibc' 'gcc-libs' 'nss')
license=('custom')
source=(
    "$pkgname-${pkgver}_orig_x86_64.pkg.tar.xz::http://down.qq.com/qqweb/LinuxQQ_1/linuxqq_2.0.0-b2-1082_x86_64.pkg.tar.xz"
    "qq.desktop"
)
sha512sums=('01a5babf0fbc5e96f5ddeef3fbb6f5e766523766742d6f95ecf84d2a7f599d35dd9971ba67c8976ae7c26c5cd5f985a81e124b3621d041ebb26c7ff9db525df7'
            'a848ecb95c69250a13bf33e3fbad0bcef2cd30973dd0bb0cea9ad4d742d607f63b76791ccbbedc4dd412bd0c39c6ec515c40dea9a8471a4635dfaa3528bfe3d2')
provides=('linuxqq')
conflicts=('linuxqq')

package() {
    mkdir -p "$pkgdir/opt/tencent-qq"
    cp -pr "$srcdir/usr/local/bin/"* "$pkgdir/opt/tencent-qq/"
    cp -pr "$srcdir/usr/local/share/tencent-qq/"* "$pkgdir/opt/tencent-qq/"

    mkdir -p "$pkgdir/usr/bin"
    ln -s ../../opt/tencent-qq/qq "$pkgdir/usr/bin/qq"
    
    install -Dm644 "$pkgdir/opt/tencent-qq/qq.png" "$pkgdir/usr/share/icons/hicolor/48x48/apps/qq.png"
    install -Dm644 "$srcdir/qq.desktop" "$pkgdir/usr/share/applications/qq.desktop"
}
