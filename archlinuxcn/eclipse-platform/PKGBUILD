# Maintainer: Florian Latifi <mail@florian-latifi.at>
# Contributor: Eddy <e.pedroni91 at gmail>
# Contributor: Shanto <shanto at hotmail>
# Contributor: Jesus Jerez <jhuss@archlinux.org.ve>

pkgname=eclipse-platform
pkgver=4.23
_pkgbuild=202203080310
pkgrel=1
pkgdesc="A minimal installation suitable for complete per-user customization with the built-in Eclipse package manager"
url="https://www.eclipse.org"
arch=("x86_64")
license=("EPL")
depends=("java-runtime>=11" "unzip" "webkit2gtk")
optdepends=()
conflicts=("eclipse-common")
provides=("eclipse=$pkgver")
options=(!strip)

source=("http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-${pkgver}-${_pkgbuild}/eclipse-platform-${pkgver}-linux-gtk-x86_64.tar.gz&r=1"
        "eclipse.sh"
        "eclipse.desktop")

sha512sums=('004184344e405d7526211c2ff07a772c1c9f3edb86fc7be2a6a90ca2af8ae00fbc63b35909140cf5849ff33af8d92d1a613afaaf03fa5496a3a458b3e22c542e'
            '71393b01c2774654e1b3348ceedd6b110c7f1b26da93da40dac653ce2103a34997ec0e9e7fd4e977d869c149d19ef39f59738717cc6762e39b0bc0e7d53df4ac'
            '6ea9f91f0704ec775aed2520737e4139ed7efcf89fd51220614e8fb8e8ce9e7460b8ff77d01519e5921f449752f60a1b36196c057e78a1906bfa4b2d346bdae2')

package() {
    install -d ${pkgdir}/usr/bin ${pkgdir}/usr/lib ${pkgdir}/usr/share/applications
    install -m755 "${srcdir}/eclipse.sh" "${pkgdir}/usr/bin/eclipse"
    install -Dm644 "${srcdir}/eclipse.desktop" "${pkgdir}/usr/share/applications/"

    for _i in 16 32 48 256; do
        install -Dm644 "${srcdir}"/eclipse/plugins/org.eclipse.platform_*/eclipse${_i}.png "$pkgdir/usr/share/icons/hicolor/${_i}x${_i}/apps/eclipse.png"
    done

    mv "${srcdir}/eclipse" "${pkgdir}/usr/lib/"
}
