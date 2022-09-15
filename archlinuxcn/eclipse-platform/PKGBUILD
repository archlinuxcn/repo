# Maintainer: Florian Latifi <mail@florian-latifi.at>
# Contributor: Eddy <e.pedroni91 at gmail>
# Contributor: Shanto <shanto at hotmail>
# Contributor: Jesus Jerez <jhuss@archlinux.org.ve>

pkgname=eclipse-platform
pkgver=4.25
_pkgbuild=202208311800
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
  "456fb91fcd80707fd4f5753322550253985e37da90025325deb9b1b0a9d36315567488d2378eb535fef517a8cf84bfd0f9508031eb20b8e105d00ab28671f49f"
  "71393b01c2774654e1b3348ceedd6b110c7f1b26da93da40dac653ce2103a34997ec0e9e7fd4e977d869c149d19ef39f59738717cc6762e39b0bc0e7d53df4ac"
  "9e97a96de20641da4f9b7be425d63fa4a7d7fab30b94b85f7f1b295d1cbc769bffe0ebaba5577e33683c7b1a2014dd78e4be97f7941b0ddcb6f2fac4461f5871"
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
