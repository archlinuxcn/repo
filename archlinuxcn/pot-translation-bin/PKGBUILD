# Maintainer: Pylogmon <pylogmon@outlook.com>

pkgname=pot-translation-bin
_pkgname=pot-translation
prjname=pot
pkgver=1.13.0
pkgrel=1
pkgdesc="一个跨平台的划词翻译软件"
arch=('x86_64' 'i686' 'aarch64' 'armv7h')
url="https://github.com/pot-app/pot-desktop"
license=('GPL3')
provides=("$_pkgname")
conflicts=("$_pkgname" "$_pkgname-git")
depends=('webkit2gtk' 'gtk3' 'libayatana-appindicator' 'xdotool' 'libxcb' 'libxrandr' 'tesseract' 'tessdata')

source_x86_64=("${prjname}-${pkgver}-x86_64.deb::${url}/releases/download/${pkgver}/${prjname}_${pkgver}_amd64.deb")
source_i686=("${prjname}-${pkgver}-i686.deb::${url}/releases/download/${pkgver}/${prjname}_${pkgver}_i386.deb")
source_aarch64=("${prjname}-${pkgver}-aarch64.deb::${url}/releases/download/${pkgver}/${prjname}_${pkgver}_arm64.deb")
source_armv7h=("${prjname}-${pkgver}-armv7h.deb::${url}/releases/download/${pkgver}/${prjname}_${pkgver}_armhf.deb")

sha512sums_x86_64=('58f72eb59198d10f799e300194ddba0c1581d7ba02789aa911326ecbf269eab5a21f7fda393a725273a67c295c1b034953781a8fd5a655f72b93d9253b96b1e2')
sha512sums_i686=('8f89029a064bc20dddaf15731ae6ef37d5d31c25c3780c091a65ffac72bd4cd95bd980128a0dd8d3c383541d08ba604f0f412a6df4e2493f46035dbc7109d737')
sha512sums_aarch64=('fc32a8b3a4b0489298d4b02fbd3f065b01c1573f343fe95a5170df61faf3c4075fffd198929c70e3a114309d3305a4aa0907acfcbffeb1e64ae1b552155b98d1')
sha512sums_armv7h=('5e07f52629f66d9cedf8d21352b25e6121fbdf7347273fdfb8ae9b2c086e28e989a1878fd65085ed707972ba3dba4ae68f184333001512ee3bafa1cbe467c652')

package() {
    tar xpf data.tar.gz -C ${pkgdir}
}
