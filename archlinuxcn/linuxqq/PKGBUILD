# Maintainer: Jack Wu (OriginCode) <self@origincode.me>

pkgname=linuxqq
pkgver=2.0.0_b2_1089
pkgrel=1
epoch=1
arch=('x86_64')
pkgdesc="Tencent QQ for Linux"
url="https://im.qq.com/linuxqq"
depends=('gtk2' 'glibc' 'gcc-libs' 'nss')
license=('custom')
source=(
    "$pkgname-${pkgver}_orig_x86_64.pkg.tar.xz::https://down.qq.com/qqweb/LinuxQQ/linuxqq_2.0.0-b2-1089_x86_64.pkg.tar.xz"
    "qq.desktop"
    "linuxqq.install"
)
sha512sums=('bf1cece63f30b5dd655bf2a85128a4dcabe00de8474b90f8553091f722e7140f545f6d97b6820b9c3c1f27ebd127e8a4ebc6e247ffe503bdc2a4cd97c1145dcb'
            'a6118c6a2dc03d22b423d4bca393c6a2ef0c8494f6480db0ee1b29ca28485e3a5e648d9485595d2d4c921d1688f72c70a70949c241b2fdde6d43bd0053cdcaa2'
            '11782ecda823feedc925e0ba87380dedb5ab19aeab7bd8e3be52f7e71737429ef1341a96554045b30ba91e9a7559c5a1c7cdf3bca1b75e2908a0ddad9a7b918b')
replaces=('qq-linux')

package() {
    mkdir -p "$pkgdir/opt/tencent-qq"
    cp -pr "$srcdir/usr/local/bin/"* "$pkgdir/opt/tencent-qq/"
    cp -pr "$srcdir/usr/local/share/tencent-qq/"* "$pkgdir/opt/tencent-qq/"

    mkdir -p "$pkgdir/usr/bin"
    ln -s ../../opt/tencent-qq/qq "$pkgdir/usr/bin/qq"
    
    install -Dm644 "$pkgdir/opt/tencent-qq/qq.png" "$pkgdir/usr/share/icons/hicolor/48x48/apps/qq.png"
    install -Dm644 "$srcdir/qq.desktop" "$pkgdir/usr/share/applications/qq.desktop"
}
