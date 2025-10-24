# Maintainer: Yuzu Vita <g311571057 at gmail dot com>
pkgname=plasma6-applets-catwalk
pkgver=2.3
pkgrel=4
pkgdesc="A simple plasmoid showing the total CPU usage. Visually made like RunCat."
arch=('any')
url="https://store.kde.org/p/2137844"
license=('GPL-2.0-or-later')
depends=(bash ksvg libksysguard libplasma qt6-declarative kcmutils kirigami)
source=("org.kde.plasma.catwalk.tar.gz"
        "0001-patch.patch")
sha256sums=('ff09d115f133ec078fd4bf08f5e72805d075ddda845e845f0b3216e962ac7e3c'
            'c6c19ac51097d2d5a093e01a31c2cf6516494478e191f91aa3862aeebfee4d26')
options=(!emptydirs)

prepare() {
    patch -Np1 < "0001-patch.patch"
}

package() {
    install -d "$pkgdir/usr/share/plasma/plasmoids/"
    cp -r org.kde.plasma.catwalk "$pkgdir/usr/share/plasma/plasmoids/"
}
