# Maintainer: Johannes Wienke <languitar@semipol.de>

pkgname=jdtls
pkgver=1.46.1
pkgrel=1
pkgdesc="Eclipse Java language server"
arch=(any)
url="https://github.com/eclipse/eclipse.jdt.ls"
license=('EPL-2.0')
depends=('java-runtime>=21')
optdepends=('python: for the official launcher script')
makedepends=()
source=("https://download.eclipse.org/jdtls/milestones/1.46.1/jdt-language-server-1.46.1-202504011455.tar.gz")
sha256sums=('f435fdf6db3aa0d1598ef0f11f80bb20e09e67009001382719c313eff07de02c')

package() {
  mkdir -p "${pkgdir}/usr/share/java/jdtls"
  cp -R "${srcdir}/"config_* "${srcdir}/features" "${srcdir}/plugins" "${srcdir}/bin" "${pkgdir}/usr/share/java/jdtls"
  mkdir -p "${pkgdir}/usr/bin"
  ln -s --relative "${pkgdir}/usr/share/java/jdtls/bin/jdtls" "${pkgdir}/usr/bin/jdtls"
}
