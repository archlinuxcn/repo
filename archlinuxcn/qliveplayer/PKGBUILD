# Maintainer: Megumi_fox <i@megumifox.com>

pkgname=qliveplayer
pkgver=3.19.1
pkgrel=1
pkgdesc='Cute and useful Live Stream Player with danmaku support.'
arch=('x86_64')
url="https://github.com/IsoaSFlus/QLivePlayer"
license=('GPL2')
depends=('mpv' 
         'ffmpeg'
         'python-aiohttp'
         'qt5-base'
         'qt5-quickcontrols2'
         'qt5-graphicaleffects'
         'qt5-quickcontrols'
         'python'
         'ykdl-git')
makedepends=('cmake'
             'extra-cmake-modules' )
optdepends=('python-protobuf: for YouTube LiveChat support'
            'streamlink: for foreign streaming service support')

source=(
    "QLivePlayer-${pkgver}::https://github.com/IsoaSFlus/QLivePlayer/archive/${pkgver}.tar.gz"
)

sha256sums=('c0c97a6e0ecf63b2a6e5557fe741f479aa7e6fefa9a2f10b0cef480303651c90')

build() {
    cd $srcdir/QLivePlayer-${pkgver}
    mkdir -p build
    cd build
    cmake -DCMAKE_INSTALL_PREFIX="$pkgdir/usr" -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_LIBDIR=lib ..
    make
}

package() {
    cd $srcdir/QLivePlayer-${pkgver}/build
    make install
}
