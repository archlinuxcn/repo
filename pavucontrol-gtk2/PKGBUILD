# Maintainer: WorMzy Tykashi <wormzy.tykashi@gmail.com>
# Contributor: Jan "heftig" Steffens <jan.steffens@gmail.com>
# Contributor: Corrado Primier <bardo@aur.archlinux.org>
# Contributor: William Rea <sillywilly@gmail.com>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=pavucontrol-gtk2
_name=pavucontrol
pkgver=3.0
pkgrel=2
pkgdesc="A GTK volume control tool for PulseAudio"
arch=(i686 x86_64)
url="http://freedesktop.org/software/pulseaudio/pavucontrol/"
license=(GPL2)
depends=(gnome-icon-theme libcanberra-pulse gtkmm libsigc++)
makedepends=(intltool lynx)
provides=(pavucontrol)
conflicts=(pavucontrol)
source=(${url}/${_name}-${pkgver}.tar.xz
        stream-elipsis.patch)
sha256sums=('b3d2ea5a25fc88dcee80c396014f72df1b4742f8cfbbc5349c39d64a0d338890'
            'ca5a9adeae4bb5167fd767d3218b17aeca8513fd55f0395ea390fc685d44478e')

prepare() {
  cd $_name-$pkgver
  patch -p1 -i "$srcdir/stream-elipsis.patch"
}

build() {
  cd $_name-$pkgver
  ./configure --prefix=/usr --disable-gtk3
  make
}

package() {
  cd $_name-$pkgver
  make DESTDIR="$pkgdir" install
}
