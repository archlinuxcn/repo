# Maintainer: Johannes Wienke <languitar@semipol.de>

pkgname=jdtls
pkgver=1.41.0
pkgrel=1
pkgdesc="Eclipse Java language server"
arch=(any)
url="https://github.com/eclipse/eclipse.jdt.ls"
license=('EPL-2.0')
depends=('java-runtime>=17')
optdepends=('python: for the official launcher script')
makedepends=()
source=("https://download.eclipse.org/jdtls/milestones/1.41.0/jdt-language-server-1.41.0-202410311350.tar.gz")
sha256sums=('adab7e8991d5bc379b5f4381e932353e4bc5818b2c3d80dcd78d12a3c2a897f5')

package() {
    mkdir -p "${pkgdir}/usr/share/java/jdtls"
    cp -R "${srcdir}/"config_* "${srcdir}/features" "${srcdir}/plugins" "${srcdir}/bin" "${pkgdir}/usr/share/java/jdtls"
    mkdir -p "${pkgdir}/usr/bin"
    ln -s --relative "${pkgdir}/usr/share/java/jdtls/bin/jdtls" "${pkgdir}/usr/bin/jdtls"
}
