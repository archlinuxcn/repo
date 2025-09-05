# Maintainer: Johannes Wienke <languitar@semipol.de>

pkgname=jdtls
pkgver=1.50.0
pkgrel=1
pkgdesc="Eclipse Java language server"
arch=(any)
url="https://github.com/eclipse/eclipse.jdt.ls"
license=('EPL-2.0')
depends=('java-runtime>=21')
optdepends=('python: for the official launcher script')
makedepends=()
source=("https://download.eclipse.org/jdtls/milestones/1.50.0/jdt-language-server-1.50.0-202509041425.tar.gz")
sha256sums=('3292c5c33888f95ab0ff718e777ee94ff5496b8635a23a8844b876ee090ebdea')

package() {
  mkdir -p "${pkgdir}/usr/share/java/jdtls"
  cp -R "${srcdir}/"config_* "${srcdir}/features" "${srcdir}/plugins" "${srcdir}/bin" "${pkgdir}/usr/share/java/jdtls"
  mkdir -p "${pkgdir}/usr/bin"
  ln -s --relative "${pkgdir}/usr/share/java/jdtls/bin/jdtls" "${pkgdir}/usr/bin/jdtls"
}
