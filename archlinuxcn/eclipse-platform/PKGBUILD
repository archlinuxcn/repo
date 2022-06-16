# Maintainer: Florian Latifi <mail@florian-latifi.at>
# Contributor: Eddy <e.pedroni91 at gmail>
# Contributor: Shanto <shanto at hotmail>
# Contributor: Jesus Jerez <jhuss@archlinux.org.ve>

pkgname=eclipse-platform
pkgver=4.24
_pkgbuild=202206070700
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
  "3cf805b62e945129080c4501198e2d0d57e76855f14d421122f7cc3955d5c48afe72218ad9d387a50ecaf617189d6aa822e9716bf7d5f935d023787370845500"
  "71393b01c2774654e1b3348ceedd6b110c7f1b26da93da40dac653ce2103a34997ec0e9e7fd4e977d869c149d19ef39f59738717cc6762e39b0bc0e7d53df4ac"
  "4155321f6a6f4671aa2753daa6466f4a06806b2d6fbc442066b75cbfd3ca3f45d61eb25bf9c662026fec7ffd307d30b3f1604792d0dfec4cca202656be627b97"
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
