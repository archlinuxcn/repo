# Maintainer: Johannes Wienke <languitar@semipol.de>

pkgname=jdtls
pkgver=1.36.0
pkgrel=1
pkgdesc="Eclipse Java language server"
arch=(any)
url="https://github.com/eclipse/eclipse.jdt.ls"
license=('EPL-2.0')
depends=('java-runtime>=17')
optdepends=('python: for the official launcher script')
makedepends=()
source=("https://download.eclipse.org/jdtls/milestones/1.36.0/jdt-language-server-1.36.0-202405301306.tar.gz")
sha256sums=('028e274d06f4a61cad4ffd56f89ef414a8f65613c6d05d9467651b7fb03dae7b')

package() {
    mkdir -p "${pkgdir}/usr/share/java/jdtls"
    cp -R "${srcdir}/"config_* "${srcdir}/features" "${srcdir}/plugins" "${srcdir}/bin" "${pkgdir}/usr/share/java/jdtls"
    mkdir -p "${pkgdir}/usr/bin"
    ln -s --relative "${pkgdir}/usr/share/java/jdtls/bin/jdtls" "${pkgdir}/usr/bin/jdtls"
}
