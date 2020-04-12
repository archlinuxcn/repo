# Maintainer: Sam Burgos <santiago.burgos1089@gmail.com>

pkgname=lightdm-slick-greeter
_pkgname=slick-greeter
pkgver=1.3.2
#_pkgver=master.mint19
pkgrel=1
pkgdesc='A slick-looking LightDM greeter'
arch=(i686 x86_64)
url="https://github.com/linuxmint/${_pkgname}"
license=(GPL3)
depends=(
    cairo
    freetype2
    gtk3
    libcanberra
    libxext
    lightdm
    pixman
    python
    xorg-server
)
optdepends=('numlockx: enable numerical keypad on supported keyboard')
makedepends=(
    intltool
    vala
)
backup=('etc/lightdm/slick-greeter.conf')
install=slick-greeter.install
source=("${_pkgname}-${pkgver}.tar.gz::$url/archive/${pkgver}.tar.gz")
sha256sums=('0654faee4578c7499205f52e95e158b6a0ccadca8933bb3e94690f80a4f15ce0')

#prepare() {
#  cd ${_pkgname}-${pkgver}
#  #Allow compiling with newer versions of Vala
#  patch -Np0 -i ../compile_new_vala.patch
#}

build() {
    cd ${_pkgname}-${pkgver}
    #cd ${_pkgname}-${_pkgver}
    aclocal --install
    autoreconf -vfi
    intltoolize -f
    ./configure \
        --prefix=/usr \
        --sysconfdir=/etc \
        --sbindir=/usr/bin \
        --libexecdir=/usr/lib/lightdm
    make
}

package() {
    cd ${_pkgname}-${pkgver}
    #cd ${_pkgname}-${_pkgver}
    make DESTDIR="${pkgdir}" install
    # adjust launcher name
    mv $pkgdir/usr/share/xgreeters/slick-greeter.desktop \
      $pkgdir/usr/share/xgreeters/lightdm-slick-greeter.desktop
}
