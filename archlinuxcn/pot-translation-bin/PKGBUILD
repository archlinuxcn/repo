# Maintainer: Pylogmon <pylogmon@outlook.com>

pkgname=pot-translation-bin
_pkgname=pot-translation
prjname=pot
pkgver=1.11.1
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

sha512sums_x86_64=('296ad6aeb2069d210cd99c01094cd36c2342b95fe7a68c3c67c2854e4bedd4a09dbe966b7f80ea4b8db8a49cab1cc36e5f113ee893efdf56facfcc7e72124ded')
sha512sums_i686=('be480178fa65d8beb913d327a774695e3533b97251efe983a1996c502703d176c49ace8a63c3e05f09c85322a04bac26078f0ebecbd811d6f37476774b12190f')
sha512sums_aarch64=('4377680341520faed080309bbae56c57c6334fbf15cbea7e3388f14e59355a6c748e990e2aa40b6d27b62d3177a2ca51f5e43389c4729e254648b896d7e63e6b')
sha512sums_armv7h=('517ecfbacb3cb863920c5e06c9b262ac9ada132e89edc9c2379336c4ed52ebb5d91b0fc15d7376b325854d6bb26f39374ec2e4685806b69e53039b826a9fbbc0')

package() {
    tar xpf data.tar.gz -C ${pkgdir}
}
