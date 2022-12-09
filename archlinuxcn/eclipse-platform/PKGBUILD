# Maintainer: Florian Latifi <mail@florian-latifi.at>
# Contributor: Eddy <e.pedroni91 at gmail>
# Contributor: Shanto <shanto at hotmail>
# Contributor: Jesus Jerez <jhuss@archlinux.org.ve>

pkgname=eclipse-platform
pkgver=4.26
_pkgbuild=202211231800
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

source=(
  "http://www.eclipse.org/downloads/download.php?file=/eclipse/downloads/drops4/R-${pkgver}-${_pkgbuild}/eclipse-platform-${pkgver}-linux-gtk-x86_64.tar.gz&r=1"
  "eclipse.sh"
  "eclipse.desktop"
)

sha512sums=(
  "8667561ad78c0ede07858abe93db70b9fb5a9694f31ed1a75552e985972925cc3eeaf25f7abb1c88331a78b46a6c201e15bcc9760ce3628efa6e93fa16e6f24b"
  "71393b01c2774654e1b3348ceedd6b110c7f1b26da93da40dac653ce2103a34997ec0e9e7fd4e977d869c149d19ef39f59738717cc6762e39b0bc0e7d53df4ac"
  "0e04a9c6f3e69fb8066394a349ad3128e5ba10180b5003119b2f0c85b548113365d8876efb143b9d4d7fe31d7b38bf16979dfe20116ea082cfdf16e57bcf0c3b"
)

package() {
  install -d ${pkgdir}/usr/bin ${pkgdir}/usr/lib ${pkgdir}/usr/share/applications
  install -m755 "${srcdir}/eclipse.sh" "${pkgdir}/usr/bin/eclipse"
  install -Dm644 "${srcdir}/eclipse.desktop" "${pkgdir}/usr/share/applications/"

  for _i in 16 32 48 256; do
    install -Dm644 "${srcdir}"/eclipse/plugins/org.eclipse.platform_*/eclipse${_i}.png "$pkgdir/usr/share/icons/hicolor/${_i}x${_i}/apps/eclipse.png"
  done

  mv "${srcdir}/eclipse" "${pkgdir}/usr/lib/"
}
