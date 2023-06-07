# Maintainer: Jose Riha <jose1711 gmail com>
# Maintainer: Sebastian J. Bronner <waschtl@sbronner.com>
# Maintainer: Kevin Stolp <kevinstolp@gmail.com>
# Contributor: Patrick Jackson <PatrickSJackson gmail com>
# Contributor: Christoph Vigano <mail@cvigano.de>

pkgname=st
pkgver=0.9
pkgrel=4
pkgdesc='A simple virtual terminal emulator for X.'
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
license=('MIT')
depends=(libxft)
url=https://st.suckless.org
source=(https://dl.suckless.org/$pkgname/$pkgname-$pkgver.tar.gz
        terminfo.patch
        README.terminfo.rst)
sha256sums=('f36359799734eae785becb374063f0be833cf22f88b4f169cd251b99324e08e7'
            'f9deea445a5c6203a0e8e699f3c3b55e27275f17fb408562c4dd5d649edeea23'
            '95be3197f7de77a0fe2e4f527202e17e910ee24e1ed6bc39beb320a1304bb7e1')
_sourcedir=$pkgname-$pkgver

prepare() {
  patch -d "$_sourcedir" -p 0 < terminfo.patch

  # This package provides a mechanism to provide a custom config.h. Multiple
  # configuration states are determined by the presence of two files in
  # $BUILDDIR:
  #
  # config.h  config.def.h  state
  # ========  ============  =====
  # absent    absent        Initial state. The user receives a message on how
  #                         to configure this package.
  # absent    present       The user was previously made aware of the
  #                         configuration options and has not made any
  #                         configuration changes. The package is built using
  #                         default values.
  # present                 The user has supplied his or her configuration. The
  #                         file will be copied to $_sourcedir and used during
  #                         build.
  #
  # After this test, config.def.h is copied from $_sourcedir to $BUILDDIR to
  # provide an up to date template for the user.
  if [ -e "$BUILDDIR/config.h" ]
  then
    cp "$BUILDDIR/config.h" "$_sourcedir"
  elif [ ! -e "$BUILDDIR/config.def.h" ]
  then
    echo \
      'This package can be configured in config.h. Copy the config.def.h that' \
      'was just placed into the package directory to config.h and modify it' \
      'to change the configuration. Or just leave it alone to continue to use' \
      'default values.'
  fi
  cp "$_sourcedir/config.def.h" "$BUILDDIR"
}

build() {
  make -C "$_sourcedir" X11INC=/usr/include/X11 X11LIB=/usr/lib/X11
}

package() {
  local shrdir="$pkgdir/usr/share"
  make -C "$_sourcedir" PREFIX=/usr DESTDIR="$pkgdir" install
  install -D -m 0644 -t "$shrdir/licenses/$pkgname" "$_sourcedir/LICENSE"
  install -D -m 0644 -t "$shrdir/doc/$pkgname" "$_sourcedir/README" README.terminfo.rst
  install -D -m 0644 -t "$shrdir/$pkgname" "$_sourcedir/st.info"
}
