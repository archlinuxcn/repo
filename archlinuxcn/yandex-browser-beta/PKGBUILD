# Maintainer: Vladimir Kamensky  <mastersoft24@yandex.ru>



_pkgname=browser-beta
pkgname=yandex-${_pkgname}
pkgver=20.11.3.188_1
_pkgver=20.11.3.188-1
pkgrel=1
#epoch=1

pkgdesc="The web browser from Yandex.
 Yandex Browser is a browser that combines a minimal design with sophisticated technology to make the web faster, safer, and easier."
arch=("x86_64")
license=("custom:yandex-browser")
categories=("network")

options=(!strip)

depends=("flac" "gconf" "gtk2" "harfbuzz-icu" "libxss" "nss" "opus" "snappy" "ttf-font" "xdg-utils" "libxkbfile" )
optdepends=(
    "speech-dispatcher" 
    "ttf-liberation: fix fonts for some PDFs"
    "yandex-libffmpeg"
)

source=("${pkgname}-${pkgver}.deb::http://repo.yandex.ru/yandex-browser/deb/pool/main/y/yandex-browser-beta/yandex-browser-beta_${_pkgver}_amd64.deb")
md5sums=("c7f6e4907438535479be26da6050e705")

prepare() {
    tar -xf data.tar.xz
}

package() {
    cp -dr --no-preserve=ownership opt usr "${pkgdir}"/
    install -D -m0644 "${pkgdir}"/opt/yandex/${_pkgname}/product_logo_128.png "${pkgdir}"/usr/share/pixmaps/${pkgname}.png
    chmod 4755 "${pkgdir}"/opt/yandex/${_pkgname}/yandex_browser-sandbox
}
