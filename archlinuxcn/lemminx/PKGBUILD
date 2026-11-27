# Maintainer: Bart Libert <bart plus aur at libert dot email>
# Contributor: Radim Sückr <kontakt@radimsuckr.cz>

# This PKGBUILD is based on https://aur.archlinux.org/packages/jdtls, thank you

pkgname=lemminx
pkgver=0.40.0
_jarname="${pkgname}-${pkgver}.jar"
pkgrel=2
pkgdesc='Eclipse XML language server'
arch=('any')
url='https://github.com/eclipse/lemminx'
license=('EPL-2.0')
depends=('java-runtime')
makedepends=()
# https://download.eclipse.org/lemminx/releases/
source=("${_jarname}::https://www.eclipse.org/downloads/download.php?file=/lemminx/releases/${pkgver}/org.eclipse.lemminx-uber.jar&r=1"
        'launcher.sh')
sha512sums=('86db51a8bd2ceaaa72f06e218913085de8c2ea08982db87498522e931891976602aeb7e1c8600ed8ec8178173470a043f393b29637b8d8bd41d78a22f1de2353'
            '5c7d71cec147b89eafd0cd11d1665f802d501ed77940a42508cfdb9a319cfe2572d6f614837f422727150f223a1c2d7c0b22a5e77d462510bc8435dc426cfdf6')
changelog=CHANGELOG.md

package() {
    install -Dm644 "${srcdir}/${_jarname}" "${pkgdir}/usr/share/java/lemminx/${_jarname}"
    install -Dm755 "${srcdir}/launcher.sh" "${pkgdir}/usr/bin/lemminx"
}
