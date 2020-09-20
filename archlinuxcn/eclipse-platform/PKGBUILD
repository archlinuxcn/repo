# Maintainer: Florian Latifi <mail@florian-latifi.at>
# Contributor: Eddy <e.pedroni91 at gmail>
# Contributor: Shanto <shanto at hotmail>
# Contributor: Jesus Jerez <jhuss@archlinux.org.ve>

pkgname=eclipse-platform
pkgver=4.17
_pkgbuild=202009021800
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

sha512sums=('897a77f4ec7a40e4d0aa86b4942f1eafbe7347e02d240fec34b7fce37f6c5e6d07f97b6b0ebffce2de9d10632b615b92c3376925720a15189c4b62c0b5cb37a2'
            '71393b01c2774654e1b3348ceedd6b110c7f1b26da93da40dac653ce2103a34997ec0e9e7fd4e977d869c149d19ef39f59738717cc6762e39b0bc0e7d53df4ac'
            'eb3e245f27a0eb328bdf3dcc1258013d55cf24d4ec3864cdc0ad9c68995bfc1af44f05a5973368f115e9957359c9e50b4cefa2fa7014c36e499447c48769f505')

package() {
    install -d ${pkgdir}/usr/bin ${pkgdir}/usr/lib ${pkgdir}/usr/share/applications
    install -m755 "${srcdir}/eclipse.sh" "${pkgdir}/usr/bin/eclipse"
    install -Dm644 "${srcdir}/eclipse.desktop" "${pkgdir}/usr/share/applications/"
    
    for _i in 16 32 48 256; do
        install -Dm644 "${srcdir}"/eclipse/plugins/org.eclipse.platform_*/eclipse${_i}.png "$pkgdir/usr/share/icons/hicolor/${_i}x${_i}/apps/eclipse.png"
    done
    
    mv "${srcdir}/eclipse" "${pkgdir}/usr/lib/"
}
