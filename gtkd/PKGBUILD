# Maintainer: Severen Redwood <severen@shrike.me>
# Contributors: Robert Welin <robert.welin@gmail.com>
#               dsboger <https://github.com/dsboger>
# Report all package issues to `https://github.com/SShrike/pkgbuilds`

pkgname='gtkd'
pkgver='3.7.2'
pkgrel=1
pkgdesc='D bindings for GTK+ and related libraries.'
arch=('x86_64' 'i686')
url='http://gtkd.org/'
license=('LGPL')
depends=('liblphobos' 'gtk3')
makedepends=('ldc')
optdepends=('pango' 'atk' 'gdk-pixbuf2' 'gtksourceview3' 'gstreamer' 'vte3' 'libpeas')
source=("https://github.com/gtkd-developers/GtkD/archive/v${pkgver}.tar.gz")
sha512sums=('da0059a48fdc63d2f80b2fe2b947b88df9c28cc977843f5855131aec1c8dda0b90251e61172889d6f68b24174d593d491972dd8da72141e372fdb3775dd10405')

build() {
  cd ${srcdir}/GtkD-${pkgver}

  LDFLAGS='' DC='ldc' make libdir='lib/' shared-{gtkd,gtkdgl,sv,gstreamer,vte,peas}
}

package() {
  cd ${srcdir}/GtkD-${pkgver}

  make prefix='/usr' libdir='lib/' DESTDIR="${pkgdir}/" \
    install-{shared,headers}-{gtkd,gtkdgl,gtkdsv,gstreamer,vte,peas}
}

# vim:set ts=2 sw=2 et:
