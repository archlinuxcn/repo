# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgbase=qt6-base
pkgname=(qt6-base qt6-xcb-private-headers)
_qtver=6.6.2
pkgver=${_qtver/-/}
pkgrel=4
arch=(x86_64)
url='https://www.qt.io'
license=(GPL3 LGPL3 FDL custom)
pkgdesc='A cross-platform application and UI framework'
depends=(brotli
         dbus
         double-conversion
         fontconfig
         freetype2
         gcc-libs
         glib2
         glibc
         harfbuzz
         icu
         krb5
         libb2
         libcups
         libdrm
         libgl
         libice
         libinput
         libjpeg-turbo
         libpng
         libproxy
         libsm
         libx11
         libxcb
         libxkbcommon
         libxkbcommon-x11
         md4c
         mesa
         mtdev
         openssl
         pcre2
         shared-mime-info
         sqlite
         systemd-libs
         tslib
         vulkan-headers
         xcb-util-cursor
         xcb-util-image
         xcb-util-keysyms
         xcb-util-renderutil
         xcb-util-wm
         xdg-utils
         zlib
         zstd)
makedepends=(alsa-lib
             cmake
             cups
             freetds
             gst-plugins-base-libs
             gtk3
             libfbclient
             libpulse
             mariadb-libs
             ninja
             postgresql
             unixodbc
             xmlstarlet)
optdepends=('freetds: MS SQL driver'
            'gdk-pixbuf2: GTK platform plugin'
            'gtk3: GTK platform plugin'
            'libfbclient: Firebird/iBase driver'
            'mariadb-libs: MariaDB driver'
            'pango: GTK platform plugin'
            'perl: for syncqt'
            'postgresql-libs: PostgreSQL driver'
            'qt6-wayland: to run Qt6 applications in a Wayland session'
            'unixodbc: ODBC driver')
groups=(qt6)
_pkgfn=${pkgbase/6-/}-everywhere-src-$_qtver
source=(https://download.qt.io/official_releases/qt/${pkgver%.*}/$_qtver/submodules/$_pkgfn.tar.xz
        qt6-base-cflags.patch
        qt6-base-nostrip.patch)
sha256sums=('b89b426b9852a17d3e96230ab0871346574d635c7914480a2a27f98ff942677b'
            '5411edbe215c24b30448fac69bd0ba7c882f545e8cf05027b2b6e2227abc5e78'
            '4b93f6a79039e676a56f9d6990a324a64a36f143916065973ded89adc621e094')

prepare() {
  patch -d $_pkgfn -p1 < qt6-base-cflags.patch # Use system CFLAGS
  patch -d $_pkgfn -p1 < qt6-base-nostrip.patch # Don't strip binaries with qmake
}

build() {
  cmake -B build -S $_pkgfn -G Ninja \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DINSTALL_BINDIR=lib/qt6/bin \
    -DINSTALL_PUBLICBINDIR=usr/bin \
    -DINSTALL_LIBEXECDIR=lib/qt6 \
    -DINSTALL_DOCDIR=share/doc/qt6 \
    -DINSTALL_ARCHDATADIR=lib/qt6 \
    -DINSTALL_DATADIR=share/qt6 \
    -DINSTALL_INCLUDEDIR=include/qt6 \
    -DINSTALL_MKSPECSDIR=lib/qt6/mkspecs \
    -DINSTALL_EXAMPLESDIR=share/doc/qt6/examples \
    -DFEATURE_journald=ON \
    -DFEATURE_libproxy=ON \
    -DFEATURE_openssl_linked=ON \
    -DFEATURE_system_sqlite=ON \
    -DFEATURE_system_xcb_xinput=ON \
    -DFEATURE_no_direct_extern_access=ON \
    -DCMAKE_INTERPROCEDURAL_OPTIMIZATION=ON \
    -DCMAKE_MESSAGE_LOG_LEVEL=STATUS
  cmake --build build
}

package_qt6-base() {
  pkgdesc='A cross-platform application and UI framework'
  depends+=(qt6-translations)
  DESTDIR="$pkgdir" cmake --install build

  install -Dm644 $_pkgfn/LICENSES/* -t "$pkgdir"/usr/share/licenses/$pkgbase

# Install symlinks for user-facing tools
  cd "$pkgdir"
  mkdir usr/bin
  while read _line; do
    ln -s $_line
  done < "$srcdir"/build/user_facing_tool_links.txt
}

package_qt6-xcb-private-headers() {
  pkgdesc='Private headers for Qt6 Xcb'

  depends=("qt6-base=$pkgver")
  optdepends=()
  groups=()

  cd $_pkgfn
  install -d -m755 "$pkgdir"/usr/include/qt6xcb-private/{gl_integrations,nativepainting}
  cp -r src/plugins/platforms/xcb/*.h "$pkgdir"/usr/include/qt6xcb-private/
  cp -r src/plugins/platforms/xcb/gl_integrations/*.h "$pkgdir"/usr/include/qt6xcb-private/gl_integrations/
  cp -r src/plugins/platforms/xcb/nativepainting/*.h "$pkgdir"/usr/include/qt6xcb-private/nativepainting/
}
