# Maintainer: Ye Jingchen <ye.jingchen@gmail.com>

pkgname=capitaine-cursors
pkgver=r3
pkgrel=1
pkgdesc="An x-cursor theme inspired by macOS and based on KDE Breeze, dark & light variant"
arch=('any')
url="https://github.com/keeferrourke/capitaine-cursors"
license=('LGPL3')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/keeferrourke/$pkgname/releases/download/$pkgver/$pkgname.tar.xz"
        "${pkgname}-light-${pkgver}.tar.gz::https://github.com/keeferrourke/$pkgname/releases/download/$pkgver/$pkgname-light.tar.xz")
sha256sums=('ec43cade1c4d8698ac3b35b08f13af17d5a86c64a8ff4e24ed8d05007d4aaae1'
            '4d6d3c489dfdfd6b47fdda4a68d0404f5546aa7fbedcee0fb2ff2babf8564294')

package() {
    install -dm755 "$pkgdir/usr/share/icons"

    cp -r dist/ "$pkgdir/usr/share/icons/capitaine-cursors"
    cp -r dist-white/ "$pkgdir/usr/share/icons/capitaine-cursors-light"
}

# vim: ts=4 sw=4 expandtab
