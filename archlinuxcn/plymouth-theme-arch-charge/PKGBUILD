#Maintainer: smcdougall <simon at sjmcdougall dot com>

pkgname=plymouth-theme-arch-charge
pkgver=20190914
pkgrel=4
pkgdesc="A Plyouth theme based on Fedora's Charge theme, but featuring the ArchLinux logo."
arch=('any')
url="http://development.sjmcdougall.com/plymouth-themes/arch-charge"
license=('GPL')
depends=('plymouth')

install='plymouth-theme-arch-charge.install'
source=('plymouth-theme-arch-charge-src.tar.gz::https://github.com/smcdougall/plymouth-theme-arch-charge/releases/download/1.0/plymouth-theme-arch-charge-src.tar.gz'
        'plymouth-theme-arch-charge.install')
md5sums=('877364608091b9a5ffd9be54c6167610' 
         '55bd7a28c16ece14c388711006aca998')

package() {
    cd $srcdir/${pkgname}
    mkdir -p $pkgdir/usr/share/plymouth/themes/arch-charge
    install -Dm644 * "${pkgdir}"/usr/share/plymouth/themes/arch-charge
}

