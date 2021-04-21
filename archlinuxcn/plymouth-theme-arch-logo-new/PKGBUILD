pkgname="plymouth-theme-arch-logo-new"
pkgver=0.2
pkgrel=3
pkgdesc="Replace the logo from package plymouth-theme-arch-logo"
arch=('any')
url="https://gitlab.com/menelkir/plymouth-arch-logo-new"
license=('GPL')
depends=('plymouth')
source=(https://gitlab.com/menelkir/plymouth-arch-logo-new/-/archive/v${pkgver}/plymouth-arch-logo-new-v${pkgver}.tar.bz2)
sha512sums=('233967016419017263b8842251b4ee9b7c0258521f8c0362fff633823c8e3ddc1ee225480d292ab832e22c712d2f20439345b1e53fde77c5356981abe9f7220f')

package() {
    cd "${srcdir}/plymouth-arch-logo-new-v${pkgver}"
    mkdir -p $pkgdir/usr/share/plymouth/themes/arch-logo-new
    install -Dm644 * $pkgdir/usr/share/plymouth/themes/arch-logo-new
}

post_install() {
    echo "==> To activate run:"
    echo "==> sudo plymouth-set-default-theme -R arch-logo-new"
}

post_upgrade() {
    post_install $1
}


