# Maintainer: Konstantin Liberty <jon9097 at gmail dot com>
# Maintainer: Cedric Girard <cgirard [dot] archlinux [at] valinor [dot] fr>
# Contributor: Michael Herzberg <{firstname}@{firstinitial}{lastname}.de>

pkgname=moonlight-qt
pkgver=6.1.0
pkgrel=2
pkgdesc='GameStream client for PCs (Windows, Mac, and Linux)'
arch=('x86_64')
license=('GPL-3.0-or-later')
url='https://moonlight-stream.org'
depends=('qt6-base' 'qt6-declarative' 'qt6-svg' 'ffmpeg' 'sdl2_ttf' 'sdl2-compat' 'lib32-sdl2-compat')
optdepends=('libva-intel-driver: hardware acceleration for Intel GPUs GMA 4500 (2008) up to Coffee Lake (2017)'
            'intel-media-driver: hardware acceleration for Intel GPUs starting from Broadwell (2014) and newer (e.g. Intel Arc)')
source=("https://github.com/moonlight-stream/${pkgname}/releases/download/v${pkgver}/MoonlightSrc-${pkgver}.tar.gz")
sha512sums=('390fe3f686c86a52dd0ff4b67e8e8beb6edcb175ddf92bc5de11d92ffdaf0b6a8d76be781c483b685626c705e63f07e156506112923c848a4a798ba703254829')

prepare() {
  sed -i '14i#include <string.h>' $srcdir/app/masterhook_internal.c
  sed -i '1a#include <cstring>' $srcdir/app/streaming/streamutils.cpp
  qmake6 PREFIX="$pkgdir/usr" moonlight-qt.pro
}

build() {
  make release
}

package() {
  make install
}
