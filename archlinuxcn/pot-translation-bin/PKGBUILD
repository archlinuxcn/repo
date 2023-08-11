# Maintainer: Pylogmon <pylogmon@outlook.com>

pkgname=pot-translation-bin
_pkgname=pot-translation
prjname=pot
pkgver=1.14.0
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

sha512sums_x86_64=('b701faca8a29c210f6468a3874943e2193d9ebb91b0f0520ad26317d7f62329fcd1e4274ac27f5640d7bdb3897a1f6097bff7adc38fd2465f1b2c0fb6b42714e')
sha512sums_i686=('a112685e4fbcef4f0efb91c02794d6f61fdfaa6209c6c075da76a03cf062f86e942bbe45d408d4703b6de61cd2ec8bbd09eed354525012b4df8a4de7739b090d')
sha512sums_aarch64=('6ac95f5045c5f90380764db57a0e235d6041d7d3d654f45781812f2fd87b5871608de169a0e9381e8faa1be1f58495c1c5a50861d21cdd5e9b40f8167fdf339c')
sha512sums_armv7h=('1a562d9485270322803d5379e0873e4499b2c93c0ec4d260efb2b533dbdc36ae6ad1810a35509cfb08616b616507c7b0f4ff957eb1c4f457270c966a1b4466e6')

package() {
    tar xpf data.tar.gz -C ${pkgdir}
}
