# Contributor: Yurii Kolesnykov <yurikoles@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Maintainer: ava1ar <mail(at)ava1ar(dot)me>

pkgbase=gstreamer0.10-base
_pkgname=gst-plugins-base
pkgname=('gstreamer0.10-base' 'gstreamer0.10-base-plugins')
pkgver=0.10.36
pkgrel=13
arch=('i686' 'x86_64' 'armv7h')
license=('LGPL')
makedepends=('gstreamer0.10>=0.10.36' 'orc' 'libxv' 'alsa-lib' 'cdparanoia' 
             'libvisual' 'libvorbis' 'libtheora' 'pango' 'gobject-introspection')
options=(!emptydirs)
url='http://gstreamer.freedesktop.org/'
source=("https://gstreamer.freedesktop.org/src/${_pkgname}/${_pkgname}-${pkgver}.tar.xz"
        fix-crash-0-byte-ogg.patch
        colorbalance-fix-abi.patch
        videoscale-fix-negotiation.patch
        ayuv64-lanczos.patch
        gstaudio-symbols.patch
        enum_headers.patch)
sha256sums=('1fe45c3894903001d4d008b0713dab089f53726dcb5842d5b40c2595a984e64a'
            'a6a01035ea9627737f9c17f72919857ed43ccc7c2cb08b645b43ed89f78d0f4f'
            '7442c5c68068428b8c7ac1d3825ce29f1bb152b75b77047b9e806c7d322b780c'
            'ae27f7be58997217f67898b37b138a485c203389e56b65e6b31c23f769ef39ca'
            '3792dfe80c69f51c0db98533e8fb16707b5dd2ee6933ea6098583af873ceb44a'
            '56e7a988df39d2ec4befa265536ad8c30d3c8d18d136cebef64e8d6baac1abae'
            '0e2a6ef0479621d522c7dbaeb577df3e422c8f7111f5892540f8437475a38932')

prepare() {
  cd ${_pkgname}-${pkgver}
  sed -i -e '/AC_PATH_XTRA/d' -e 's/AM_CONFIG_HEADER/AC_CONFIG_HEADERS/' configure.ac
  patch -Np1 -i ../fix-crash-0-byte-ogg.patch
  patch -Np1 -i ../colorbalance-fix-abi.patch
  patch -Np1 -i ../ayuv64-lanczos.patch
  patch -Np1 -i ../videoscale-fix-negotiation.patch
  patch -Np1 -i ../gstaudio-symbols.patch
  patch -Np1 -i ../enum_headers.patch
}

build() {
  cd ${_pkgname}-${pkgver}
  NOCONFIGURE=1 ./autogen.sh
  ./configure --prefix=/usr --sysconfdir=/etc --localstatedir=/var --disable-static --enable-experimental --disable-gnome_vfs --disable-gtk-doc
  make
  sed -e 's/^SUBDIRS_EXT =.*/SUBDIRS_EXT =/' -i Makefile
}

package_gstreamer0.10-base() {
  pkgdesc="GStreamer Multimedia Framework Base plugin libraries"
  depends=('gstreamer0.10>=0.10.36' 'orc' 'libxv')

  cd ${_pkgname}-${pkgver}
  make DESTDIR="${pkgdir}" install
}

package_gstreamer0.10-base-plugins() {
  pkgdesc="GStreamer Multimedia Framework Base Plugins (gst-plugins-base)"
  depends=("gstreamer0.10-base=${pkgver}" 'alsa-lib' 'cdparanoia' 'libvisual' 'libvorbis' 'libtheora' 'pango')
  replaces=('gstreamer0.10-alsa' 'gstreamer0.10-theora' 'gstreamer0.10-libvisual' 'gstreamer0.10-pango' 'gstreamer0.10-cdparanoia' 'gstreamer0.10-vorbis' 'gstreamer0.10-ogg')
  conflicts=('gstreamer0.10-alsa' 'gstreamer0.10-theora' 'gstreamer0.10-libvisual' 'gstreamer0.10-pango' 'gstreamer0.10-cdparanoia' 'gstreamer0.10-vorbis' 'gstreamer0.10-ogg')
  groups=('gstreamer0.10-plugins')

  cd ${_pkgname}-${pkgver}
  make -C gst-libs DESTDIR="${pkgdir}" install
  make -C ext DESTDIR="${pkgdir}" install
  make -C gst-libs DESTDIR="${pkgdir}" uninstall
}
