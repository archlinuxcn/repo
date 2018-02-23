# Maintainer: snql <snql DOT by AT gmail DOT com>
# Based on vivaldi-codecs-ffmpeg-extra-bin package <Maintainer: Fahad Hossain>
# http://security.ubuntu.com/ubuntu/pool/universe/c/chromium-browser/chromium-codecs-ffmpeg-extra_61.0.3163.100-0ubuntu1.1378_amd64.deb
pkgname=yandex-browser-codecs-ffmpeg-extra-bin
pkgver=61.0.3163.100
pkgrel=1378
epoch=1
pkgdesc="Prebuilt ffmpeg-codecs package for yandex.browser"
arch=(
  "x86_64"
)
url="https://packages.ubuntu.com/xenial/amd64/chromium-codecs-ffmpeg-extra/download"
license=('LGPL')
provides=(
  'yandex-browser-ffmpeg-codecs'
)
conflicts=(
  'yandex-browser-ffmpeg-codecs'
)
source=(
  
"http://security.ubuntu.com/ubuntu/pool/universe/c/chromium-browser/chromium-codecs-ffmpeg-extra_${pkgver}-0ubuntu1.${pkgrel}_amd64.deb"
)
md5sums=(
  "6e5268a86f4fefec858da0aa6e0407b1"
)

prepare() {
  cd "$srcdir"
  tar -xJf data.tar.xz
}

package() {
  cd "$srcdir"
  mkdir -p "$pkgdir/opt/yandex/browser-beta"
  cp "$srcdir/usr/lib/chromium-browser/libffmpeg.so" "$pkgdir/opt/yandex/browser-beta/libffmpeg.so"
}

