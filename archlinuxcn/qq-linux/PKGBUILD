# Maintainer: Jack Wu (OriginCode) <self@origincode.me>

pkgname=qq-linux
pkgver=2.0.0_b1_1024
pkgrel=1
arch=('x86_64')
pkgdesc="Tencent QQ for Linux"
url="https://im.qq.com/linuxqq"
depends=('gtk2' 'glibc' 'gcc-libs' 'nss')
license=('custom')
source=(
    "$pkgname-${pkgver}_orig_x86_64.pkg.tar.xz::https://qd.myapp.com/myapp/qqteam/linuxQQ/linuxqq_2.0.0-b1-1024_x86_64.pkg.tar.xz"
    "qq.desktop"
)
md5sums=('d7d7d3666a46dc8e0cf24f8252974da1'
         '11d6d9830271ca6dee367e8d15567810')

package() {
    mkdir -p "$pkgdir/opt"
    cp -dpr --preserve=ownership "$srcdir/usr/share/tencent-qq" "$pkgdir/opt/"

    mkdir -p "$pkgdir/usr/bin"
    ln -s /opt/tencent-qq/qq "$pkgdir/usr/bin/qq"
    
    mkdir -p "$pkgdir/usr/share/applications"
    install -m644 "$srcdir/qq.desktop" "$pkgdir/usr/share/applications/"
}
