# Maintainer: Vladimir Kamensky  <mastersoft24@yandex.ru>



_pkgname=browser-beta
pkgname=yandex-${_pkgname}
pkgver=17.6.1.835_1
_pkgver=17.6.1.835-1
pkgrel=1
#epoch=1

pkgdesc="The web browser from Yandex.
 Yandex Browser is a browser that combines a minimal design with sophisticated technology to make the web faster, safer, and easier."
arch=("x86_64")
license=("custom:yandex-browser")
categories=("network")

options=(!strip)

depends=("flac" "gconf" "gtk2" "harfbuzz-icu" "libxss" "nss" "opus" "snappy" "ttf-font" "xdg-utils" "libxkbfile")
optdepends=(
    "speech-dispatcher" 
    "kdebase-kdialog: needed for file dialogs in KDE"
    "ttf-liberation: fix fonts for some PDFs"
    "yandex-browser-ffmpeg-codecs: support for h.264 and other non-free media formats"
)

source=("${pkgname}-${pkgver}.deb::http://repo.yandex.ru/yandex-browser/deb/pool/main/y/yandex-browser-beta/yandex-browser-beta_${_pkgver}_amd64.deb")
md5sums=("d9b2b425580f6c9fad6852a4f20b1815")

prepare() {
    tar -xf data.tar.xz
}

package() {
    cp -dr --no-preserve=ownership opt usr "${pkgdir}"/
    install -D -m0644 "${pkgdir}"/opt/yandex/${_pkgname}/product_logo_128.png "${pkgdir}"/usr/share/pixmaps/${pkgname}.png
    chmod 4755 "${pkgdir}"/opt/yandex/${_pkgname}/yandex_browser-sandbox
}