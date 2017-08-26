# Contributor: Levente Polyak <anthraxx[at]archlinux[dot]org>
# Contributor: Giovanni Scafora <giovanni@archlinux.org>
# Contributor: Sarah Hay <sarahhay@mb.sympatico.ca>
# Contributor: Martin Sandsmark <martin.sandsmark@kde.org>

pkgname=vlc-qt5
_pkgname=vlc
pkgver=2.2.6
pkgrel=1
pkgdesc='Multi-platform MPEG, VCD/DVD, and DivX player (Qt5 version)'
url='https://www.videolan.org/vlc/'
arch=('i686' 'x86_64')
license=('LGPL2.1' 'GPL2')
depends=('a52dec' 'libdvbpsi' 'libxpm' 'libdca' 'libproxy'
         'sdl_image' 'libdvdnav' 'libtiger' 'lua' 'libmatroska'
         'zvbi' 'taglib' 'libmpcdec' 'ffmpeg2.8' 'faad2' 'libupnp'
         'libshout' 'libmad' 'libmpeg2' 'xcb-util-keysyms' 'libtar'
         'libxinerama')
makedepends=('live-media' 'libnotify' 'libbluray' 'flac'
             'libdc1394' 'libavc1394' 'lirc' 'libcaca' 'gtk2'
             'librsvg' 'portaudio' 'libgme' 'xosd' 'projectm'
             'twolame' 'aalib' 'libmtp' 'libdvdcss' 'smbclient'
             'libgoom2' 'vcdimager' 'opus' 'libssh2' 'mesa' 'qt5-base')
optdepends=('avahi: for service discovery using bonjour protocol'
            'libnotify: for notification plugin'
            'gtk2: for notify plugin'
            'ncurses: for ncurses interface support'
            'libdvdcss: for decoding encrypted DVDs'
            'lirc: for lirc plugin'
            'libavc1394: for devices using the 1394ta AV/C'
            'libdc1394: for IEEE 1394 plugin'
            'libva-vdpau-driver: vdpau back-end for nvidia'
            'libva-intel-driver: back-end for intel cards'
            'libbluray: for Blu-Ray support'
            'flac: for Free Lossless Audio Codec plugin'
            'portaudio: for portaudio support'
            'twolame: for TwoLAME mpeg2 encoder plugin'
            'projectm: for ProjectM visualisation plugin'
            'libcaca: for colored ASCII art video output'
            'libgme: for libgme plugin'
            'librsvg: for SVG plugin'
            'libgoom2: for libgoom plugin'
            'vcdimager: navigate VCD with libvcdinfo'
            'aalib: for ASCII art plugin'
            'libmtp: for MTP devices support'
            'smbclient: for SMB access plugin'
            'libcdio: for audio CD playback support'
            'ttf-freefont: for subtitle font '
            'ttf-dejavu: for subtitle font'
            'opus: for opus support'
            'libssh2: for sftp support'
            'lua-socket: for http interface'
            'qt5-base: for the GUI')
conflicts=($_pkgname)
provides=($_pkgname)
options=('!emptydirs')
source=(https://download.videolan.org/${_pkgname}/${pkgver}/${_pkgname}-${pkgver}.tar.xz{,.asc}
        update-vlc-plugin-cache.hook
        lua53_compat.patch)
sha512sums=('9aff5922eb8b3c6a24e6153c367b0170dbc67602ae3e9304f52d2da00c9081d66cc98abd722b7c95b6c7d2e6cc7c86f21f9cba42c7d4bf29ca97d0f2d3553f8d'
            'SKIP'
            'd9e69a01eb8868647beac0f419328e6ca3fe14a2e2a9e6ce4b61ed590b41b0136fb3ac9e284b174a910c2fe8822d1b37445a48d0b7caea647060ebfabe899e7b'
            '33cda373aa1fb3ee19a78748e2687f2b93c8662c9fda62ecd122a2e649df8edaceb54dda3991bc38c80737945a143a9e65baa2743a483bb737bb94cd590dc25f')
validpgpkeys=('65F7C6B4206BD057A7EB73787180713BE58D1ADC') # VideoLAN Release Signing Key

prepare() {
  cd ${_pkgname}-${pkgver}
  sed -i -e 's:truetype/freefont:TTF:g' modules/text_renderer/freetype.c
  sed -i -e 's:truetype/ttf-dejavu:TTF:g' modules/visualization/projectm.cpp
  patch -p1 < "${srcdir}/lua53_compat.patch"
}

build() {
  cd ${_pkgname}-${pkgver}

  export PKG_CONFIG_PATH="/usr/lib/ffmpeg2.8/pkgconfig"
  export CFLAGS+=" -I/usr/include/samba-4.0"
  export CPPFLAGS+=" -I/usr/include/samba-4.0"
  export CXXFLAGS+=" -std=c++11"
  export LUAC=/usr/bin/luac
  export LUA_LIBS="`pkg-config --libs lua`"
  export RCC=/usr/bin/rcc-qt5

  ./configure --prefix=/usr \
              --sysconfdir=/etc \
              --disable-rpath \
              --enable-faad \
              --enable-nls \
              --enable-lirc \
              --enable-ncurses \
              --enable-realrtsp \
              --enable-aa \
              --enable-vcdx \
              --enable-upnp \
              --enable-opus \
              --enable-sftp

  make
}

package() {
  cd "${_pkgname}-${pkgver}"

  make DESTDIR="${pkgdir}" install

  for res in 16 32 48 128; do
    install -Dm 644 "${srcdir}/vlc-${pkgver}/share/icons/${res}x${res}/vlc.png" \
                     "${pkgdir}/usr/share/icons/hicolor/${res}x${res}/apps/vlc.png"
  done

  install -Dm 644 "${srcdir}/update-vlc-plugin-cache.hook" -t "${pkgdir}/usr/share/libalpm/hooks"
}

# vim: ts=2 sw=2 et:
