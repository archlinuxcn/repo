# Maintainer: yk <yk at archlinuxcn dot org>

_pkgname=desktop-app
pkgname=leanote
pkgver=2.2.3
pkgrel=1
pkgdesc="Knowledge, Blog, Sharing, Cooperation."
arch=("i686" "x86_64")
url="https://leanote.com/"
license=("GPL3")
depends=("electron" "gconf")
makedepends=("electron" "gulp")
provides=("${pkgname}")
conflicts=("${pkgname}")
#install=$pkgname.install

source=("leanote.desktop"
"leanote"
)
sha256sums=('8dab30fe0835432e44b5a3a1d46aebde8716a2a47ba4031cbe2a01560987aa83'
'57155a0e423bc98f0e83acb35f03ace06b3de54bdc64b2373128671c801727b1'
)

source_x86_64=("https://sourceforge.net/projects/leanote-desktop-app/files/${pkgver}/leanote-desktop-linux-x64-v${pkgver}.zip/download")
source_i686=("https://sourceforge.net/projects/leanote-desktop-app/files/${pkgver}/leanote-desktop-linux-ia33-v${pkgver}.zip/download")
sha256sums_x86_64=('17c0e0510ae247ec4f05f428209f414bbccf25939c1e378ab09fad6afb5b85bb')
sha256sums_i686=('2ad20d4004c4a0220d400821273d1f28a121a8d6fa1b9ee3db9141ebf5838578')

build() {
	cd "${srcdir}"
    rm -rf __MACOSX 
    rm -rf .DS_Store
}

package() {
    install -d "${pkgdir}"/opt
    cp -R ${srcdir}/ "${pkgdir}"/opt/leanote
    install -D -m655 "./${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
    install -D -m644 "./${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
    install -D -m644 "${srcdir}/${pkgname}.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
    install -D -m644 "${srcdir}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
    install -D -m644 "${srcdir}/LICENSES.chromium.html" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSES.chromium.html"
}
