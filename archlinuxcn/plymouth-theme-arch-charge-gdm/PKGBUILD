#Maintainer: Nick Boughton <nicholasboughton@gmail.com>
#Contributor: smcdougall <simon at sjmcdougall dot com>

pkgname=plymouth-theme-arch-charge-gdm
pkgver=0.1.1
pkgrel=1
pkgdesc="A Plyouth theme based on Fedora's Charge theme, but featuring the ArchLinux logo. Based on sjmcdougall's Arch Charge theme"
arch=('any')
url="https://github.com/nboughton/plymouth-theme-arch-charge-gdm"
license=('GPL')
depends=('plymouth')

install='plymouth-theme-arch-charge-gdm.install'
source=("https://github.com/nboughton/$pkgname/archive/v$pkgver.tar.gz")
sha512sums=('80a1e22ec071f889f8e3c37ec1befe85638f852b81c1323dd2696fd941a665ce7e2dd8a5225dc182e3a7ee0712566f294eca05533eec0ba6589ae1ecae81abf5')

package() {
    cd $srcdir/$pkgname-$pkgver/src
    mkdir -p $pkgdir/usr/share/plymouth/themes/arch-charge-gdm
    install -Dm644 * "${pkgdir}"/usr/share/plymouth/themes/arch-charge-gdm
}

