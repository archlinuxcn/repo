# Maintainer: Bart Libert <bart plus aur at libert dot email>
# Contributor: Radim Sückr <kontakt@radimsuckr.cz>

# This PKGBUILD is based on https://aur.archlinux.org/packages/jdtls, thank you

pkgname=lemminx
pkgver=0.28.0
_jarname="${pkgname}-${pkgver}.jar"
pkgrel=1
pkgdesc='Eclipse XML language server'
arch=('any')
url='https://github.com/eclipse/lemminx'
license=('EPL-2.0')
depends=('java-runtime')
makedepends=()
# https://download.eclipse.org/lemminx/releases/
source=("${_jarname}::https://download.eclipse.org/lemminx/releases/${pkgver}/org.eclipse.lemminx-uber.jar"
        'launcher.sh')
sha512sums=('40f5501c7fdf65b35e948a1a8f0f1e3195a991d821c330da7584d3d3eba33b1b34df22049849c35f3e88ddd07bd99d50bf6e5877cc5182d249f0424a6eb374ec'
            '21973956910861bb7c608a0240cc8fd2ef15a5753bfee8df36dfda39721a06d474a66c59a22501b990fb3d3d063531a385dca62a7e91b248c1cb9509aff77cec')

package() {
    install -Dm644 "${srcdir}/${_jarname}" "${pkgdir}/usr/share/java/lemminx/${_jarname}"
    for file in ${srcdir}/license/*; do
        install -Dm644 "${srcdir}/license/${file##*/}" "${pkgdir}/usr/share/licenses/${pkgname}/${file##*/}"
    done
    install -Dm755 "${srcdir}/launcher.sh" "${pkgdir}/usr/bin/lemminx"
}
