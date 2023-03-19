# Maintainer: Florian Latifi <mail@florian-latifi.at>
# Contributor: Eddy <e.pedroni91 at gmail>
# Contributor: Shanto <shanto at hotmail>
# Contributor: Jesus Jerez <jhuss@archlinux.org.ve>

pkgname=eclipse-platform
pkgver=4.27
_pkgbuild=202303020300
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
  "f0a854c25acba76114ecc9bdca67358cb1467e8258159279ca2006c24cb8d8a06a05bc72075b7b1c7bcfa4fb2e30d262c8e0dc3030ad0beec218e2b64237de1f"
  "5d0068de0b134468d6a9f0c2be1ac7a8253152cac9e9561ba32c0bc11bb503dbcc7dba64ff3989179c3276bac9153bae46205d86978442a067837eb8677c384d"
  "b75e2fd8d5fccfc57d75d6c717cd10b325bd4d0813de9dddefa1719d6fa617428154d0f0f70032ae29d8ec31d181a4601a8457ad29c61201922a05f97428d266"
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
