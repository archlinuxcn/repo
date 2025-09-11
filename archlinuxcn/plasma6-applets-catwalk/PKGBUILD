# Maintainer: Yuzu Vita <g311571057 at gmail dot com>
pkgname=plasma6-applets-catwalk
pkgver=None
pkgrel=1
pkgdesc="A simple plasmoid showing the total CPU usage. Visually made like RunCat."
arch=('any')
url="https://store.kde.org/p/2137844"
license=('GPL-2.0-or-later')
depends=(bash ksvg libksysguard libplasma kdeplasma-addons qt6-declarative kcmutils kirigami)
source=("org.kde.plasma.catwalk.tar.gz")
sha256sums=('ff09d115f133ec078fd4bf08f5e72805d075ddda845e845f0b3216e962ac7e3c')
options=(!emptydirs)

package() {
    install -d "$pkgdir/usr/share/plasma/plasmoids/"
    cp -r org.kde.plasma.catwalk "$pkgdir/usr/share/plasma/plasmoids/"
}
