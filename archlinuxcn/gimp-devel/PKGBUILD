# Maintainer: twa022 <twa022 at gmail dot com>

_pkgname=gimp
pkgname=${_pkgname}-devel
pkgver=2.99.14
pkgrel=2
pkgdesc="GNU Image Manipulation Program (Development version)"
arch=('i686' 'x86_64' 'armv7h' 'aarch64')
url="https://www.gimp.org/"
license=('GPL' 'LGPL')
depends=('gtk3' 'lcms2' 'libwmf' 'icu' 'enchant' 'libgexiv2' 'librsvg' 'desktop-file-utils'
         'libexif' 'libgudev' 'openjpeg2' 'poppler-glib' 'poppler-data' 'openexr' 'mypaint-brushes1'
         'babl>=0.1.98' 'gegl>=0.4.40' 'cairo' 'python-gobject' 'appstream-glib' 'libxmu' 'graphviz')
makedepends=('appstream' 'intltool' 'libxslt' 'glib-networking'
             'alsa-lib' 'curl' 'ghostscript' 'libxpm'
             'libheif' 'libwebp' 'libmng' 'iso-codes' 'aalib' 'zlib' 'libjxl'
             'gjs'  'luajit' 'meson' 'gobject-introspection'
             'gi-docgen' 'xorg-server-xvfb' 'vala' 'highway' 'meson') #'yelp-tools')
checkdepends=('xorg-server-xvfb')
optdepends=('gutenprint: for sophisticated printing only as gimp has built-in cups print support'
            'alsa-lib: for MIDI event controller module'
            'curl: for URI support'
            'ghostscript: for postscript support'
            'libxpm: XPM support'
            'libheif: HEIF support'
            'libjxl: JPEG XL support'
            'libwebp: WebP support'
            'libmng: MNG support'
            'iso-codes: Language support'
            'aalib: ASCII art support'
            'zlib: Compression routines'
            'gjs: JavaScript scripting support'
            'luajit: LUA scripting support'
            'lua51-lgi: LUA scripting support')
conflicts=("${_pkgname}")
provides=("${_pkgname}=${pkgver}")
source=("https://download.gimp.org/pub/gimp/v${pkgver%.*}/${_pkgname}-${pkgver}.tar.xz"
        'babl-0.1-name-change-meson.patch'
        'linux.gpl')
sha256sums=('313a205475d1ff03c5c4d9602f09f5c975ba6c1c79d8843e2396f9fe2abdf7a8'
            'e012d022fe53eaf4cd2fc08f07cb0377fb14c8f791e42d13027983e41f7f4fc2'
            '1003bbf5fc292d0d63be44562f46506f7b2ca5729770da9d38d3bb2e8a2f36b3')

prepare() {
  cd "${_pkgname}-${pkgver}"
  patch -Np1 -i ../babl-0.1-name-change-meson.patch
}

build() {
  local meson_options=(
  )

  arch-meson "${_pkgname}-${pkgver}" build "${meson_options[@]}"
  meson compile -C build
}

package() {
  meson install -C build --destdir "$pkgdir"

  install -Dm 644 "${srcdir}/linux.gpl" "${pkgdir}/usr/share/gimp/2.99/palettes/Linux.gpl"
}
