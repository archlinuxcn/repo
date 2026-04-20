# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Chris Kitching <chriskitching@linux.com>

pkgbase=lib32-gstreamer
pkgname=(
  lib32-gstreamer
  lib32-gst-plugins-base-libs
  lib32-gst-plugins-base
  lib32-gst-plugins-good
)
pkgver=1.28.1
pkgrel=3
pkgdesc="Multimedia graph framework (32-bit)"
url="https://gstreamer.freedesktop.org/"
arch=(x86_64)
license=(LGPL-2.1-or-later)
makedepends=(
  git
  glib2-devel
  lib32-aalib
  lib32-alsa-lib
  lib32-bzip2
  lib32-cairo
  lib32-cdparanoia
  lib32-flac
  lib32-gcc-libs
  lib32-gdk-pixbuf2
  lib32-glib2
  lib32-glibc
  lib32-gtk3
  lib32-jack
  lib32-libavc1394
  lib32-libcaca
  lib32-libcap
  lib32-libdrm
  lib32-libdv
  lib32-libelf
  lib32-libglvnd
  lib32-libgudev
  lib32-libiec61883
  lib32-libjpeg-turbo
  lib32-libogg
  lib32-libpng
  lib32-libpulse
  lib32-libraw1394
  lib32-libshout
  lib32-libsoup3
  lib32-libtheora
  lib32-libunwind
  lib32-libvpx
  lib32-libx11
  lib32-libxcb
  lib32-libxdamage
  lib32-libxext
  lib32-libxfixes
  lib32-libxi
  lib32-libxml2
  lib32-libxtst
  lib32-libxv
  lib32-mesa
  lib32-mpg123
  lib32-nettle
  lib32-opus
  lib32-orc
  lib32-pango
  lib32-rust
  lib32-sdl2
  lib32-speex
  lib32-taglib
  lib32-twolame
  lib32-v4l-utils
  lib32-wavpack
  lib32-wayland
  lib32-zlib
  meson
  wayland-protocols
)
checkdepends=(xorg-server-xvfb)
source=(
  "git+https://gitlab.freedesktop.org/gstreamer/gstreamer.git?signed#tag=$pkgver"
  0001-HACK-meson-Disable-broken-tests.patch
)
b2sums=('8e92829812e06312f99db805f59d2757f476f7c38dcf596adf37407f537d8664a27b9067059ab669b89bebfc367d2e724b6e1bd0717e05937b5a01f1a9ba4445'
        'ff9b5e5e8dde09e242766bcf9e943e41a518967bb991586fb68906d91036ac3e8c79a499a5e66d294b4759a44dba3c7bea5a4e61d5fd9aab2fdf58e8b3ab6329')
validpgpkeys=(
  D637032E45B8C6585B9456565D2EEE6F6F349D7C # Tim Müller <tim@gstreamer-foundation.org>
)

prepare() {
  cd gstreamer

  # Disable broken tests
  git apply -3 ../0001-HACK-meson-Disable-broken-tests.patch
}

build() {
  local meson_options=(
    --cross-file lib32
    --libexecdir lib32
    -D bad=disabled
    -D benchmarks=disabled
    -D devtools=disabled
    -D doc=disabled
    -D examples=disabled
    -D ges=disabled
    -D glib_debug=disabled
    -D gpl=enabled
    -D gst-examples=disabled
    -D gst-plugins-base:gl-graphene=disabled
    -D gst-plugins-base:libvisual=disabled
    -D gst-plugins-base:tremor=disabled
    -D gst-plugins-good:amrnb=disabled
    -D gst-plugins-good:amrwbdec=disabled
    -D gst-plugins-good:lame=disabled
    -D gst-plugins-good:rpicamsrc=disabled
    -D gstreamer:bash-completion=disabled
    -D gstreamer:dbghelp=disabled
    -D gstreamer:ptp-helper-permissions=capabilities
    -D introspection=disabled
    -D libav=disabled
    -D libnice=disabled
    -D orc-source=system
    -D package-name="Arch Linux Lib32 GStreamer ${epoch:+$epoch:}$pkgver-$pkgrel"
    -D package-origin="https://www.archlinux.org/"
    -D python=disabled
    -D qt5=disabled
    -D qt6=disabled
    -D rs=disabled
    -D rtsp_server=disabled
    -D sharp=disabled
    -D ugly=disabled
  )

  # https://gitlab.freedesktop.org/gstreamer/gstreamer/-/issues/3197
  export GI_SCANNER_DISABLE_CACHE=1

  arch-meson gstreamer build "${meson_options[@]}"
  meson compile -C build
}

check() (
  export XDG_RUNTIME_DIR="$PWD/runtime-dir"
  mkdir -p -m 700 "$XDG_RUNTIME_DIR"

  export CK_TIMEOUT_MULTIPLIER=5
  export NO_AT_BRIDGE=1 GTK_A11Y=none

  # Flaky due to timeouts
  xvfb-run -s "-nolisten local" \
    meson test -C build --print-errorlogs -t $CK_TIMEOUT_MULTIPLIER || :
)

_install() {
  local src dir
  for src in "${files[@]}"; do
    dir="$pkgdir/$(dirname "$src")"
    mkdir -p "$dir"
    mv -v "$src" "$dir"
  done
}

package_lib32-gstreamer() {
  pkgdesc+=" - core"
  depends=(
    gstreamer
    lib32-gcc-libs
    lib32-glib2
    lib32-glibc
    lib32-libcap
    lib32-libelf
    lib32-libunwind
  )
  optdepends=()
  install=lib32-gstreamer.install

  meson install -C build --destdir "$srcdir/root"

  rm -R "$srcdir"/root/usr/{share,include}

  for _i in "$srcdir"/root/usr/bin/*; do
    mv "${_i}" "${_i}-32"
  done

  cd root; local files=(
    usr/lib32/libgst{reamer,base,check,controller,net}-1.0.so*
    usr/lib32/pkgconfig/gstreamer{,-base,-check,-controller,-net}-1.0.pc

    usr/lib32/gstreamer-1.0/gst-ptp-helper
    usr/lib32/gstreamer-1.0/gst-plugin-scanner
    usr/lib32/gstreamer-1.0/libgstcoreelements.so
    usr/lib32/gstreamer-1.0/libgstcoretracers.so

    usr/bin/gst-{inspect,launch,stats,tester,typefind}-1.0-32
  ); _install
}

package_lib32-gst-plugins-base-libs() {
  pkgdesc+=" - base"
  depends=(
    "lib32-gstreamer=$pkgver-$pkgrel"
    gst-plugins-base-libs
    lib32-gcc-libs
    lib32-glib2
    lib32-glibc
    lib32-libdrm
    lib32-libglvnd
    lib32-libgudev
    lib32-libjpeg-turbo
    lib32-libpng
    lib32-libx11
    lib32-libxcb
    lib32-libxext
    lib32-libxi
    lib32-libxv
    lib32-mesa
    lib32-orc
    lib32-wayland
    lib32-zlib
  )

  cd root; local files=(
    usr/lib32/libgst{allocators,app,audio,fft,gl,pbutils,riff,rtp,rtsp,sdp,tag,video}-1.0.so*
    usr/lib32/pkgconfig/gstreamer-{allocators,app,audio,fft,gl{,-egl,-prototypes,-wayland,-x11},pbutils,riff,rtp,rtsp,sdp,tag,video}-1.0.pc

    usr/lib32/pkgconfig/gstreamer-plugins-base-1.0.pc
    usr/lib32/gstreamer-1.0/include/gst/gl/gstglconfig.h
    usr/lib32/gstreamer-1.0/libgstadder.so
    usr/lib32/gstreamer-1.0/libgstapp.so
    usr/lib32/gstreamer-1.0/libgstaudioconvert.so
    usr/lib32/gstreamer-1.0/libgstaudiomixer.so
    usr/lib32/gstreamer-1.0/libgstaudiorate.so
    usr/lib32/gstreamer-1.0/libgstaudioresample.so
    usr/lib32/gstreamer-1.0/libgstaudiotestsrc.so
    usr/lib32/gstreamer-1.0/libgstbasedebug.so
    usr/lib32/gstreamer-1.0/libgstcompositor.so
    usr/lib32/gstreamer-1.0/libgstdsd.so
    usr/lib32/gstreamer-1.0/libgstencoding.so
    usr/lib32/gstreamer-1.0/libgstgio.so
    usr/lib32/gstreamer-1.0/libgstopengl.so
    usr/lib32/gstreamer-1.0/libgstoverlaycomposition.so
    usr/lib32/gstreamer-1.0/libgstpbtypes.so
    usr/lib32/gstreamer-1.0/libgstplayback.so
    usr/lib32/gstreamer-1.0/libgstrawparse.so
    usr/lib32/gstreamer-1.0/libgstsubparse.so
    usr/lib32/gstreamer-1.0/libgsttcp.so
    usr/lib32/gstreamer-1.0/libgsttypefindfunctions.so
    usr/lib32/gstreamer-1.0/libgstvideoconvertscale.so
    usr/lib32/gstreamer-1.0/libgstvideorate.so
    usr/lib32/gstreamer-1.0/libgstvideotestsrc.so
    usr/lib32/gstreamer-1.0/libgstvolume.so
    usr/lib32/gstreamer-1.0/libgstximagesink.so
    usr/lib32/gstreamer-1.0/libgstxvimagesink.so

    usr/bin/gst-{device-monitor,discoverer,play}-1.0-32
  ); _install
}

package_lib32-gst-plugins-base() {
  pkgdesc+=" - base plugins"
  depends=(
    "lib32-gst-plugins-base-libs=$pkgver-$pkgrel"
    "lib32-gstreamer=$pkgver-$pkgrel"
    gst-plugins-base
    lib32-alsa-lib
    lib32-cairo
    lib32-cdparanoia
    lib32-gcc-libs
    lib32-glib2
    lib32-glibc
    lib32-libogg
    lib32-libtheora
    lib32-libvorbis
    lib32-opus
    lib32-pango
  )

  cd root; local files=(
    usr/lib32/gstreamer-1.0/libgstalsa.so
    usr/lib32/gstreamer-1.0/libgstcdparanoia.so
    usr/lib32/gstreamer-1.0/libgstogg.so
    usr/lib32/gstreamer-1.0/libgstopus.so
    usr/lib32/gstreamer-1.0/libgstpango.so
    usr/lib32/gstreamer-1.0/libgsttheora.so
    usr/lib32/gstreamer-1.0/libgstvorbis.so
  ); _install
}

package_lib32-gst-plugins-good() {
  pkgdesc+=" - good plugins"
  depends=(
    "lib32-gst-plugins-base-libs=$pkgver-$pkgrel"
    "lib32-gstreamer=$pkgver-$pkgrel"
    gst-plugins-good
    lib32-aalib
    lib32-bzip2
    lib32-cairo
    lib32-flac
    lib32-gcc-libs
    lib32-gdk-pixbuf2
    lib32-glib2
    lib32-glibc
    lib32-libavc1394
    lib32-libcaca
    lib32-libdv
    lib32-libgudev
    lib32-libiec61883
    lib32-libjpeg-turbo
    lib32-libpng
    lib32-libpulse
    lib32-libraw1394
    lib32-libshout
    lib32-libsoup3
    lib32-libvpx
    lib32-libx11
    lib32-libxdamage
    lib32-libxext
    lib32-libxfixes
    lib32-libxml2
    lib32-libxtst
    lib32-mpg123
    lib32-nettle
    lib32-orc
    lib32-speex
    lib32-taglib
    lib32-twolame
    lib32-v4l-utils
    lib32-wavpack
    lib32-zlib
  )
  optdepends=("lib32-jack: JACK backend")

  cd root; local files=(
    usr/lib32/gstreamer-1.0/libgst1394.so
    usr/lib32/gstreamer-1.0/libgstaasink.so
    usr/lib32/gstreamer-1.0/libgstadaptivedemux2.so
    usr/lib32/gstreamer-1.0/libgstalaw.so
    usr/lib32/gstreamer-1.0/libgstalpha.so
    usr/lib32/gstreamer-1.0/libgstalphacolor.so
    usr/lib32/gstreamer-1.0/libgstapetag.so
    usr/lib32/gstreamer-1.0/libgstaudiofx.so
    usr/lib32/gstreamer-1.0/libgstaudioparsers.so
    usr/lib32/gstreamer-1.0/libgstauparse.so
    usr/lib32/gstreamer-1.0/libgstautodetect.so
    usr/lib32/gstreamer-1.0/libgstavi.so
    usr/lib32/gstreamer-1.0/libgstcacasink.so
    usr/lib32/gstreamer-1.0/libgstcairo.so
    usr/lib32/gstreamer-1.0/libgstcutter.so
    usr/lib32/gstreamer-1.0/libgstdebug.so
    usr/lib32/gstreamer-1.0/libgstdeinterlace.so
    usr/lib32/gstreamer-1.0/libgstdtmf.so
    usr/lib32/gstreamer-1.0/libgstdv.so
    usr/lib32/gstreamer-1.0/libgsteffectv.so
    usr/lib32/gstreamer-1.0/libgstequalizer.so
    usr/lib32/gstreamer-1.0/libgstflac.so
    usr/lib32/gstreamer-1.0/libgstflv.so
    usr/lib32/gstreamer-1.0/libgstflxdec.so
    usr/lib32/gstreamer-1.0/libgstgdkpixbuf.so
    usr/lib32/gstreamer-1.0/libgstgoom.so
    usr/lib32/gstreamer-1.0/libgstgoom2k1.so
    usr/lib32/gstreamer-1.0/libgsticydemux.so
    usr/lib32/gstreamer-1.0/libgstid3demux.so
    usr/lib32/gstreamer-1.0/libgstimagefreeze.so
    usr/lib32/gstreamer-1.0/libgstinterleave.so
    usr/lib32/gstreamer-1.0/libgstisomp4.so
    usr/lib32/gstreamer-1.0/libgstjack.so
    usr/lib32/gstreamer-1.0/libgstjpeg.so
    usr/lib32/gstreamer-1.0/libgstlevel.so
    usr/lib32/gstreamer-1.0/libgstmatroska.so
    usr/lib32/gstreamer-1.0/libgstmonoscope.so
    usr/lib32/gstreamer-1.0/libgstmpg123.so
    usr/lib32/gstreamer-1.0/libgstmulaw.so
    usr/lib32/gstreamer-1.0/libgstmultifile.so
    usr/lib32/gstreamer-1.0/libgstmultipart.so
    usr/lib32/gstreamer-1.0/libgstnavigationtest.so
    usr/lib32/gstreamer-1.0/libgstoss4.so
    usr/lib32/gstreamer-1.0/libgstossaudio.so
    usr/lib32/gstreamer-1.0/libgstpng.so
    usr/lib32/gstreamer-1.0/libgstpulseaudio.so
    usr/lib32/gstreamer-1.0/libgstreplaygain.so
    usr/lib32/gstreamer-1.0/libgstrtp.so
    usr/lib32/gstreamer-1.0/libgstrtpmanager.so
    usr/lib32/gstreamer-1.0/libgstrtsp.so
    usr/lib32/gstreamer-1.0/libgstshapewipe.so
    usr/lib32/gstreamer-1.0/libgstshout2.so
    usr/lib32/gstreamer-1.0/libgstsmpte.so
    usr/lib32/gstreamer-1.0/libgstsoup.so
    usr/lib32/gstreamer-1.0/libgstspectrum.so
    usr/lib32/gstreamer-1.0/libgstspeex.so
    usr/lib32/gstreamer-1.0/libgsttaglib.so
    usr/lib32/gstreamer-1.0/libgsttwolame.so
    usr/lib32/gstreamer-1.0/libgstudp.so
    usr/lib32/gstreamer-1.0/libgstvideo4linux2.so
    usr/lib32/gstreamer-1.0/libgstvideobox.so
    usr/lib32/gstreamer-1.0/libgstvideocrop.so
    usr/lib32/gstreamer-1.0/libgstvideofilter.so
    usr/lib32/gstreamer-1.0/libgstvideomixer.so
    usr/lib32/gstreamer-1.0/libgstvpx.so
    usr/lib32/gstreamer-1.0/libgstwavenc.so
    usr/lib32/gstreamer-1.0/libgstwavpack.so
    usr/lib32/gstreamer-1.0/libgstwavparse.so
    usr/lib32/gstreamer-1.0/libgstximagesrc.so
    usr/lib32/gstreamer-1.0/libgstxingmux.so
    usr/lib32/gstreamer-1.0/libgsty4m.so
  ); _install
}

# vim:set sw=2 sts=-1 et:
