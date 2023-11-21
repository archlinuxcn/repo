# Maintainer: Bart Libert <bart plus aur at libert dot email>
# Contributor: Radim Sückr <kontakt@radimsuckr.cz>

# This PKGBUILD is based on https://aur.archlinux.org/packages/jdtls, thank you

pkgname=lemminx
pkgver=0.27.0
_jarname="${pkgname}-${pkgver}.jar"
pkgrel=1
pkgdesc='Eclipse XML language server'
arch=('any')
url='https://github.com/eclipse/lemminx'
license=('EPL')
depends=('java-runtime')
makedepends=()
# https://download.eclipse.org/lemminx/releases/
source=("${_jarname}::https://download.eclipse.org/lemminx/releases/${pkgver}/org.eclipse.lemminx-uber.jar"
        'launcher.sh')
sha512sums=('1f2b790044b8f02be32695cf63a56bfdf59c8b33a17c0f4502655e958cf12be3acf74ca4c2f527b0b4736ee0dba1bbdd058b309c382e90cdfd1d6848cf73bfb3'
            '21973956910861bb7c608a0240cc8fd2ef15a5753bfee8df36dfda39721a06d474a66c59a22501b990fb3d3d063531a385dca62a7e91b248c1cb9509aff77cec')

package() {
    install -Dm644 "${srcdir}/${_jarname}" "${pkgdir}/usr/share/java/lemminx/${_jarname}"
    for file in ${srcdir}/license/*; do
        install -Dm644 "${srcdir}/license/${file##*/}" "${pkgdir}/usr/share/licenses/${pkgname}/${file##*/}"
    done
    install -Dm755 "${srcdir}/launcher.sh" "${pkgdir}/usr/bin/lemminx"
}
