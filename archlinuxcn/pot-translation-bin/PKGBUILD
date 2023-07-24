# Maintainer: Pylogmon <pylogmon@outlook.com>

pkgname=pot-translation-bin
_pkgname=pot-translation
prjname=pot
pkgver=1.10.1
pkgrel=1
pkgdesc="一个跨平台的划词翻译软件"
arch=('x86_64')
url="https://github.com/pot-app/pot-desktop"
license=('GPL3')
provides=("$_pkgname")
conflicts=("$_pkgname" "$_pkgname-git")
depends=('webkit2gtk' 'gtk3' 'libayatana-appindicator' 'xdotool' 'libxcb' 'libxrandr')

source=("${prjname}-${pkgver}-${arch}.deb::${url}/releases/download/${pkgver}/${prjname}_${pkgver}_amd64.deb")

sha512sums=('df8437c009b2c3e8f2a69984eedd424cf53b5ecff933f6808db6adc500f2ac559e6c97f5bed220d97940b568b26deab15758a1425ca4d92485cb8a83c6234d90')

package() {
    tar xpf data.tar.gz -C ${pkgdir}
}
