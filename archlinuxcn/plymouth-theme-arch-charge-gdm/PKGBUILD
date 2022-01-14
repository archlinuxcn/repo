#Maintainer: Nick Boughton <nicholasboughton@gmail.com>
#Contributor: smcdougall <simon at sjmcdougall dot com>

pkgname=plymouth-theme-arch-charge-gdm
pkgver=0.2.1
pkgrel=1
pkgdesc="A Plyouth theme based on Fedora's Charge theme, but featuring the ArchLinux logo. Based on sjmcdougall's Arch Charge theme"
arch=('any')
url="https://github.com/nboughton/plymouth-theme-arch-charge-gdm"
license=('GPL')
depends=('plymouth')

install='plymouth-theme-arch-charge-gdm.install'
source=("https://github.com/nboughton/$pkgname/archive/v$pkgver.tar.gz")
sha512sums=('e15c82cb6f01d50620bfeceb2ab1da1f736d99ea84afbce803719ddb62be0c011a059cae8c6521b87341bf07f998dff7e790b138e6a2c746a335c2ae890ecc58')

package() {
    cd $srcdir/$pkgname-$pkgver/src
    mkdir -p $pkgdir/usr/share/plymouth/themes/arch-charge-gdm
    install -Dm644 * "${pkgdir}"/usr/share/plymouth/themes/arch-charge-gdm
}

