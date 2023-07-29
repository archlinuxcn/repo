# Maintainer: Pylogmon <pylogmon@outlook.com>

pkgname=pot-translation-bin
_pkgname=pot-translation
prjname=pot
pkgver=1.12.0
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

sha512sums_x86_64=('5dc55394b30da92bb48d32bfb935b1e6da93d3be983840bd210417905cda953dfa575f93aec4f9e58d991af02aef1fd937f816d19d50e8892737be50325f27f3')
sha512sums_i686=('2fe36df7efd03638b95a6096ca0f1f514c7667d1e2c34b017f7b817e93e675d5476d639644d95763722c60755433520a76688559f62431e50b89aa9b058fcb48')
sha512sums_aarch64=('7b806488b1d5b084d6839a4c158a6632025252dbe6b8987df18a6a6dfc6201f08ab5c40adb1bddd4af1424a217e804a6424fb47535f34fa1735d53378cb7507b')
sha512sums_armv7h=('ed731821e0e2464a9ac63af99dda1837a5f27b88df6df9a25ecea804624b2bfa6a8932a64e96db4dc5c54a96f00c1af02cc535686bfbfedd1830d3804f457076')

package() {
    tar xpf data.tar.gz -C ${pkgdir}
}
