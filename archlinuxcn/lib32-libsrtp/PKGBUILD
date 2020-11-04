# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: orumin <dev@orum.in>

_basename=libsrtp
pkgname="lib32-$_basename"
pkgver=2.3.0
pkgrel=2
epoch=1
pkgdesc="Library for SRTP (Secure Realtime Transport Protocol) (32-bit)"
url="https://github.com/cisco/libsrtp"
arch=('x86_64')
license=(BSD)
depends=('lib32-glibc' 'libsrtp')
makedepends=('git')
checkdepends=('procps-ng')
options=('staticlibs')
_commit=d02d21111e379c297e93a9033d7b653135f732ee  # tags/v2.3.0
source=("git+https://github.com/cisco/libsrtp#commit=$_commit")
sha256sums=('SKIP')

pkgver() {
    cd $_basename
    git describe --tags | sed 's/^v//;s/-/+/g'
}

prepare() {
    cd $_basename

    # Fixup pkgver: There are tags like v1.5.4 but also "moving" tags like v1 and v1.5
    git tag | grep -Pv '^v\d+.\d+.\d+$' | xargs git tag -d

    # Fix building with GCC 10
    git cherry-pick -n 716a73862b387a2107f37398c0fb7d9a754c0ccd

    autoreconf -fvi
}

build() {
    cd $_basename

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure --prefix=/usr \
        --build=i686-pc-linux-gnu \
        --libdir=/usr/lib32

    make all
    make shared_library
}

check() {
    cd $_basename

    make runtest
}

package() {
    cd $_basename

    make DESTDIR="$pkgdir" install

    install -Dt "$pkgdir/usr/share/licenses/$pkgname" -m644 LICENSE

    cd "$pkgdir"/usr

    rm -r include
}
