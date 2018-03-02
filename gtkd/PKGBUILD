# Maintainer: Severen Redwood <severen@shrike.me>
# Contributors: Robert Welin <robert.welin@gmail.com>
#               dsboger <https://github.com/dsboger>
# Report all package issues to `https://github.com/SShrike/pkgbuilds`

pkgname='gtkd'
pkgver='3.7.5'
pkgrel=1
pkgdesc='D bindings for GTK+ and related libraries.'
arch=('x86_64' 'i686')
url='http://gtkd.org/'
license=('LGPL')
depends=('liblphobos' 'gtk3')
makedepends=('ldc')
optdepends=('pango' 'atk' 'gdk-pixbuf2' 'gtksourceview3' 'gstreamer' 'vte3' 'libpeas')
source=("https://github.com/gtkd-developers/GtkD/archive/v${pkgver}.tar.gz")
sha512sums=('258bdb53d56006d6aeab04adbc8d8ed61b5ac56c4a0b63e4df135f801f08aa324b0506a059b1c29bd6dd76a0330756b50221316b33d18b9272949e0775539b93')

build() {
  cd ${srcdir}/GtkD-${pkgver}

  LDFLAGS='-defaultlib=druntime-ldc-shared,phobos2-ldc-shared' DC='ldc' make libdir='lib/' shared-{gtkd,gtkdgl,sv,gstreamer,vte,peas}
}

package() {
  cd ${srcdir}/GtkD-${pkgver}

  make prefix='/usr' libdir='lib/' DESTDIR="${pkgdir}/" \
    install-{shared,headers}-{gtkd,gtkdgl,gtkdsv,gstreamer,vte,peas}
}

# vim:set ts=2 sw=2 et:
