# Maintainer: Johannes Wienke <languitar@semipol.de>

pkgname=jdtls
pkgver=1.56.0
pkgrel=1
pkgdesc="Eclipse Java language server"
arch=(any)
url="https://github.com/eclipse/eclipse.jdt.ls"
license=('EPL-2.0')
depends=('java-runtime>=21')
optdepends=('python: for the official launcher script')
makedepends=()
source=("https://download.eclipse.org/jdtls/milestones/1.56.0/jdt-language-server-1.56.0-202601291528.tar.gz")
sha256sums=('988492f1a4350be52aafbe538dc04f5c4dae08ad0e1f2aa35317622ed2dbe3c6')

package() {
  mkdir -p "${pkgdir}/usr/share/java/jdtls"
  cp -R "${srcdir}/"config_* "${srcdir}/features" "${srcdir}/plugins" "${srcdir}/bin" "${pkgdir}/usr/share/java/jdtls"
  mkdir -p "${pkgdir}/usr/bin"
  ln -s --relative "${pkgdir}/usr/share/java/jdtls/bin/jdtls" "${pkgdir}/usr/bin/jdtls"
}
