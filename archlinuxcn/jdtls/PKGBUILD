# Maintainer: Johannes Wienke <languitar@semipol.de>

pkgname=jdtls
pkgver=1.57.0
pkgrel=1
pkgdesc="Eclipse Java language server"
arch=(any)
url="https://github.com/eclipse/eclipse.jdt.ls"
license=('EPL-2.0')
depends=('java-runtime>=21')
optdepends=('python: for the official launcher script')
makedepends=()
source=("https://download.eclipse.org/jdtls/milestones/1.57.0/jdt-language-server-1.57.0-202602261110.tar.gz")
sha256sums=('f7ffa93fe1bbbea95dac13dd97cdcd25c582d6e56db67258da0dcceb2302601e')

package() {
  mkdir -p "${pkgdir}/usr/share/java/jdtls"
  cp -R "${srcdir}/"config_* "${srcdir}/features" "${srcdir}/plugins" "${srcdir}/bin" "${pkgdir}/usr/share/java/jdtls"
  mkdir -p "${pkgdir}/usr/bin"
  ln -s --relative "${pkgdir}/usr/share/java/jdtls/bin/jdtls" "${pkgdir}/usr/bin/jdtls"
}
