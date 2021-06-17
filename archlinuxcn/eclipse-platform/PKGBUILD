# Maintainer: Florian Latifi <mail@florian-latifi.at>
# Contributor: Eddy <e.pedroni91 at gmail>
# Contributor: Shanto <shanto at hotmail>
# Contributor: Jesus Jerez <jhuss@archlinux.org.ve>

pkgname=eclipse-platform
pkgver=4.20
_pkgbuild=202106111600
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

sha512sums=('470f0e535ffab796cd63643fe18bd46ce5c9c34cb469b6d9ff06bd2a41e0f7ccc0aaa9049b3acbaf6e8b4bed79bab03e0653d0672c418f5610dc7a02b6420d99'
            '71393b01c2774654e1b3348ceedd6b110c7f1b26da93da40dac653ce2103a34997ec0e9e7fd4e977d869c149d19ef39f59738717cc6762e39b0bc0e7d53df4ac'
            'a588a628d9a04a408ad503aa27b505fef21cc9a2a3139c1d24247cafe9ab3d3bfa22844666d3224753f9cb25ac2f7e64e9f5ecd4d8b374e43c484959df38f374')

package() {
    install -d ${pkgdir}/usr/bin ${pkgdir}/usr/lib ${pkgdir}/usr/share/applications
    install -m755 "${srcdir}/eclipse.sh" "${pkgdir}/usr/bin/eclipse"
    install -Dm644 "${srcdir}/eclipse.desktop" "${pkgdir}/usr/share/applications/"

    for _i in 16 32 48 256; do
        install -Dm644 "${srcdir}"/eclipse/plugins/org.eclipse.platform_*/eclipse${_i}.png "$pkgdir/usr/share/icons/hicolor/${_i}x${_i}/apps/eclipse.png"
    done

    mv "${srcdir}/eclipse" "${pkgdir}/usr/lib/"
}
