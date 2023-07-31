# Maintainer: Pylogmon <pylogmon@outlook.com>

pkgname=pot-translation-bin
_pkgname=pot-translation
prjname=pot
pkgver=1.13.1
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

sha512sums_x86_64=('99792dbb7d90c8f0588a8f50ca48f84815b261370cc0bc4183bea67d46e46886d63924d9b9e8da4dbb3a43cedb5e9c09a0a4cfdb8d545ebb23025aad24d502a1')
sha512sums_i686=('b1e853a4634ad720e78f641f4b5bf5d3af09e70249935db90865de35016eec39fe62c02e32b15b42a24cd0aefae78d99a025e480e03fd94120d486be1d16a772')
sha512sums_aarch64=('5d0abf3da97fa1ad9f0be4da074a42fb822a82995208ac9ca0b6266eaab8fc92c6e8bb132669ce1690f0ecc0a80716ac7b08bdbb951cf7dbe20112671ef6168e')
sha512sums_armv7h=('323603c440214062eae266e46db6822853dfe64f19c27599af920dc57b1c89e031ae85085b0172f67ad5d67cb99b49cb17dedb78d3dc10206e1bddbab193d7da')

package() {
    tar xpf data.tar.gz -C ${pkgdir}
}
