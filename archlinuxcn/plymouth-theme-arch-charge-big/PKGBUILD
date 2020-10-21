#Maintainer: smcdougall <simon at sjmcdougall dot com>

pkgname=plymouth-theme-arch-charge-big
pkgver=20190914
pkgrel=3
pkgdesc="A Plyouth theme based on Fedora's Charge theme, but featuring the ArchLinux logo.  This version has a larger logo than the regular variant."
arch=('any')
url="http://development.sjmcdougall.com/plymouth-themes/arch-charge"
license=('GPL')
depends=('plymouth')

install='plymouth-theme-arch-charge-big.install'
source=('plymouth-theme-arch-charge-big-src.tar.gz::https://github.com/smcdougall/plymouth-theme-arch-charge/releases/download/1.0/plymouth-theme-arch-charge-big-src.tar.gz'
        'plymouth-theme-arch-charge-big.install')
md5sums=('7b61242549e4a331ffee1695aa06a49d' 
         '54ebc03f22123a5c971cefbb3a3fe35c')

package() {
    cd $srcdir/${pkgname}
    mkdir -p $pkgdir/usr/share/plymouth/themes/arch-charge-big
    install -Dm644 * "${pkgdir}"/usr/share/plymouth/themes/arch-charge-big
}

