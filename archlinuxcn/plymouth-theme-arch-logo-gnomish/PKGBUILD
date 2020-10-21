# Maintainer: Ian Hernández <ihernandezs@openmailbox.org>

pkgname=plymouth-theme-arch-logo-gnomish
pkgver=1.0.0
pkgrel=1
pkgdesc="ArchLinux logo theme for plymouth with a GNOME(ish) flavour"
arch=('any')
url=""
license=('GPL')
depends=('plymouth')
install='plymouth-theme-arch-logo-gnomish.install'
source=('plymouth-theme-arch-logo-gnomish-src.tar.gz'
        'plymouth-theme-arch-logo-gnomish.install')
md5sums=('dfab042ad368d0b64cd286752ba14287' 
         '8e7ab45e9ddf60b4225a1e927128a159')

package() {
    cd $srcdir/${pkgname}
    mkdir -p $pkgdir/usr/share/plymouth/themes/arch-logo-gnomish
    install -Dm644 * "${pkgdir}"/usr/share/plymouth/themes/arch-logo-gnomish
}

