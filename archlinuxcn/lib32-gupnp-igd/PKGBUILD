# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>

_basename=gupnp-igd
pkgname=lib32-gupnp-igd
pkgver=0.2.5+3+gedd78a6
pkgrel=2
pkgdesc="A library to handle UPnP IGD port mapping (32-bit)"
url="https://wiki.gnome.org/Projects/GUPnP"
arch=(x86_64)
license=(LGPL)
depends=(lib32-gupnp gupnp-igd)
makedepends=(git gobject-introspection gtk-doc)
_commit=edd78a6561fc1a6e6769342157f0e4db62705fa3  # master
source=("git+https://gitlab.gnome.org/GNOME/gupnp-igd.git#commit=$_commit")
sha256sums=('SKIP')

pkgver() {
    cd $_basename

    git describe --tags | sed 's/-/+/g'
}

prepare() {
    cd $_basename

    # gupnp 1.2
    git cherry-pick -n 63531558a16ac2334a59f627b2fca5576dcfbb2e

    gtkdocize
    autoreconf -fvi
}

build() {
    cd $_basename

    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

    ./configure \
        --prefix=/usr \
        --build=i686-pc-linux-gnu \
        --libdir=/usr/lib32 \
        --disable-gtk-doc

    sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool

    make
}

check() {
    cd $_basename

    # test broken (requires root to bind lowport)
    make check || :
}

package() {
    cd $_basename

    make DESTDIR="${pkgdir}" install

    cd "$pkgdir/usr"

    rm -r include share
}

