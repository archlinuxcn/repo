# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Ionut Biru <ibiru@archlinux.org
# Contributor: Pierre Schmitz <pierre@archlinux.de>
# Contributor: Mikko Seppälä <t-r-a-y@mbnet.fi>

pkgname=lib32-gtk2
pkgver=2.24.33
pkgrel=5
pkgdesc="GObject-based multi-platform GUI toolkit (legacy, 32-bit)"
url="https://www.gtk.org/"
arch=(x86_64)
license=(LGPL-2.1-or-later)
depends=(
  gtk2
  lib32-atk
  lib32-cairo
  lib32-gdk-pixbuf2
  lib32-glib2
  lib32-glibc
  lib32-libcups
  lib32-librsvg
  lib32-libx11
  lib32-libxcomposite
  lib32-libxcursor
  lib32-libxdamage
  lib32-libxext
  lib32-libxfixes
  lib32-libxi
  lib32-libxinerama
  lib32-libxrandr
  lib32-libxrender
  lib32-pango
)
makedepends=(
  git
  glib2-devel
  gobject-introspection
  gtk-doc
)
source=(
  "git+https://gitlab.gnome.org/GNOME/gtk.git#tag=$pkgver"
  gtk-query-immodules-2.0-32.hook
  0001-Lower-severity-of-XID-collision-warnings.patch
  0002-Stop-looking-for-modules-in-cwd.patch
)
b2sums=('1b18d1cfef55466209cf93be45af15dc058a8b74d13ab590cfc7f0b09b0584adc62d4330aaed65185c0142cc8c326e4274c8e75e0af94bec5be3cfcca105c1e6'
        'e9a1c4037c9e1fd03e0c139059165a85b6258b0535bd8150d5b1bdab71f056240bd0448f2f1d6930aa1b1b73299707e79ce83c6f28dcbeb7664412c136bb5401'
        '45ecc976d9eb9d990fc204230aa052a6d1b2bdfdc94788be37d576ab262a1da49855eb46ecd4bfce4efde6e2f817a1660c6d1fa756be3b372f7f8d13b0ef0fd0'
        '06ca1c6f0e8f6a7c7a3cc08ce3d358af978d28fc4aa8d9e981883e3ad5adf7d821bcb27bc8b93bf65171a92396ac8f7ad62c90db501a492cca7c30b6081e957f')

prepare() {
  cd gtk
  git apply -3 ../0001-Lower-severity-of-XID-collision-warnings.patch

  # CVE-2024-6655: https://www.openwall.com/lists/oss-security/2024/09/09/1
  # https://gitlab.gnome.org/GNOME/gtk/-/merge_requests/7361
  git apply -3 ../0002-Stop-looking-for-modules-in-cwd.patch

  sed -i '/AM_INIT_AUTOMAKE/s/]/ foreign]/' configure.ac
  autoreconf -fvi
}

build() {
  local configure_options=(
    --prefix=/usr
    --libdir=/usr/lib32
    --sysconfdir=/etc
    --localstatedir=/var
    --with-xinput=yes
    --disable-gtk-doc
  )

  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG=i686-pc-linux-gnu-pkg-config
  CFLAGS+=" -Wno-error=implicit-int -Wno-error=incompatible-pointer-types"

  cd gtk
  ./configure "${configure_options[@]}"
  sed -i -e 's/ -shared / -Wl,-O1,--as-needed\0/g' libtool
  make
}

package() {
  optdepends=(
    'adwaita-fonts: Default font'
    'adwaita-icon-theme: Default icon theme'
    'gnome-themes-extra-gtk2: Default widget theme'
  )
  provides=(
    libgailutil.so
    libgdk-x11-2.0.so
    libgtk-x11-2.0.so
  )
  install=lib32-gtk2.install

  make -C gtk DESTDIR="$pkgdir" install
  rm -r "$pkgdir"/{etc,usr/{include,share}}
  find "$pkgdir/usr/bin" -type f -not -name gtk-query-immodules-2.0 -delete
  mv "$pkgdir"/usr/bin/gtk-query-immodules-2.0{,-32}

  install -Dm644 gtk-query-immodules-2.0-32.hook -t "$pkgdir/usr/share/libalpm/hooks"
}

# vim:set sw=2 sts=-1 et:
