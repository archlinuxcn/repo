# Maintainer: Jack Wu (OriginCode) <self@origincode.me>

pkgname=qq-linux
pkgver=2.0.0_b1_1024
pkgrel=3
arch=('x86_64')
pkgdesc="Tencent QQ for Linux"
url="https://im.qq.com/linuxqq"
depends=('gtk2' 'glibc' 'gcc-libs' 'nss')
license=('custom')
source=(
    "$pkgname-${pkgver}_orig_x86_64.pkg.tar.xz::https://qd.myapp.com/myapp/qqteam/linuxQQ/linuxqq_2.0.0-b1-1024_x86_64.pkg.tar.xz"
    "qq.desktop"
)
sha512sums=(
    'b430ee22c7d32f61982482e24ed47ad249c95ec5ba750b8d7537f880e3780a8513b101061511949245139fe122a582bdce87b784301de85e14593a8b4ad58866'
    'a6118c6a2dc03d22b423d4bca393c6a2ef0c8494f6480db0ee1b29ca28485e3a5e648d9485595d2d4c921d1688f72c70a70949c241b2fdde6d43bd0053cdcaa2'
)
provides=('linuxqq')
conflicts=('linuxqq')

package() {
    mkdir -p "$pkgdir/opt"
    cp -dpr --preserve=ownership "$srcdir/usr/share/tencent-qq" "$pkgdir/opt/"

    mkdir -p "$pkgdir/usr/bin"
    ln -s /opt/tencent-qq/qq "$pkgdir/usr/bin/qq"
    
    install -Dm644 "$srcdir/qq.desktop" "$pkgdir/usr/share/applications/"
}
