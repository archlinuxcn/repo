# Maintainer: Megumi_fox <i@megumifox.com>

pkgname=qliveplayer
pkgver=3.19.2
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

sha256sums=('0c2bb64b50da70bb6bd24419041990bc0dc6c7a31ad99d33b6a3c4a6569e6a58')

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
