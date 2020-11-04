# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: zaplo

_basename=webrtc-audio-processing
pkgname=lib32-webrtc-audio-processing
pkgver=0.3.1
pkgrel=2
pkgdesc="AudioProcessing library based on Google's implementation of WebRTC"
url="https://freedesktop.org/software/pulseaudio/webrtc-audio-processing/"
arch=(x86_64)
license=(custom)
depends=(lib32-gcc-libs webrtc-audio-processing)
makedepends=(git)
_commit=e882a5442ac22c93648e12837248d651d18b9247  # tags/v0.3.1^0
source=("git+https://anongit.freedesktop.org/git/pulseaudio/webrtc-audio-processing#commit=$_commit")
sha256sums=('SKIP')

pkgver() {
    cd $_basename

    git describe --tags | sed 's/^v//;s/-/+/g'
}

prepare() {
    cd $_basename

    NOCONFIGURE=1 ./autogen.sh
}

build() {
    cd $_basename

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure \
        --build=i686-pc-linux-gnu \
        --prefix=/usr \
        --libdir=/usr/lib32 \
        --disable-static

    make
}

package() {
    cd $_basename

    make DESTDIR=${pkgdir} install

    rm -r "$pkgdir/usr/include"

    install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}
