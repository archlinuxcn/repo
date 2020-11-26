# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>
# Contributor: orumin <dev@orum.in>

_basename=gst-plugins-bad
pkgname=lib32-gst-plugins-bad
pkgver=1.16.2
pkgrel=6
pkgdesc="GStreamer open-source multimedia framework bad plugins (32-bit)"
url="https://gstreamer.freedesktop.org/"
arch=(x86_64)
license=(LGPL)
depends=(lib32-aom lib32-bluez-libs lib32-celt lib32-chromaprint lib32-curl lib32-faac lib32-faad2
        lib32-fluidsynth lib32-gnutls lib32-gst-plugins-base-libs lib32-gst-plugins-good lib32-ladspa
        lib32-lcms2 lib32-libbs2b lib32-libdc1394 lib32-libdca lib32-libde265 lib32-libdvdnav
        lib32-libdvdread lib32-libexif lib32-libfdk-aac lib32-libgme lib32-libgudev lib32-libkate
        lib32-liblrdf lib32-libmms lib32-libmodplug lib32-libmpcdec lib32-libmpeg2 lib32-libnice
        lib32-libofa lib32-librsvg lib32-libsrtp lib32-libusb lib32-libvdpau lib32-libwebp lib32-lilv
        lib32-lv2 lib32-mjpegtools lib32-neon lib32-openal lib32-openexr lib32-openjpeg2 lib32-rtmpdump
        lib32-sbc lib32-soundtouch lib32-spandsp lib32-srt lib32-vulkan-icd-loader lib32-wayland
        lib32-webrtc-audio-processing lib32-wildmidi lib32-x265 lib32-zbar lib32-zvbi
        gst-plugins-bad)
makedepends=(git lib32-gtk3 lib32-libtiger lib32-vulkan-validation-layers lv2
             meson python vulkan-headers)
checkdepends=(xorg-server-xvfb)
_commit=a6f26408f74a60d02ce6b4f0daee392ce847055f  # tags/1.16.2^0
source=("git+https://gitlab.freedesktop.org/gstreamer/gst-plugins-bad.git#commit=$_commit"
        "0001-vulkan-Drop-use-of-VK_RESULT_BEGIN_RANGE.patch")
sha256sums=('SKIP'
            '0c6c51a371d8f381a2190280913cc41e06c17c25dbb1167043072003b3f0d338')

pkgver() {
    cd $_basename

    git describe --tags | sed 's/-/+/g'
}

prepare() {
    cd $_basename

    # Fix build with lib32-neon 0.31
    git cherry-pick -n f10b424418e448211e3427a76fcd046e157ef0b7

    # Fix build with vulkan-headers 1.2.140
    git apply -3 ../0001-vulkan-Drop-use-of-VK_RESULT_BEGIN_RANGE.patch

    # Fix build with GCC 10
    git cherry-pick -n a0cd455dd0e0375c6395fe732173225ea7e18562
}

build() {
    export CC='gcc -m32'
    export CXX='g++ -m32'
    export PKG_CONFIG='/usr/bin/i686-pc-linux-gnu-pkg-config'

    arch-meson $_basename build \
        --libdir=/usr/lib32 \
        -D directfb=disabled \
        -D flite=disabled \
        -D gsm=disabled \
        -D iqa=disabled \
        -D msdk=disabled \
        -D nvdec=disabled \
        -D nvenc=disabled \
        -D opencv=disabled \
        -D openh264=disabled \
        -D openmpt=disabled \
        -D openni2=disabled \
        -D opensles=disabled \
        -D sctp=disabled \
        -D tinyalsa=disabled \
        -D voaacenc=disabled \
        -D voamrwbenc=disabled \
        -D wasapi=disabled \
        -D wpe=disabled \
        -D gl=disabled \
        -D gobject-cast-checks=disabled \
        -D package-name="GStreamer Bad Plugins (Arch Linux)" \
        -D package-origin="https://www.archlinux.org/" \
        -D introspection=disabled \
        -D dtls=disabled

    meson compile -C build
}

check() (
    mkdir -p -m 700 "${XDG_RUNTIME_DIR:=$PWD/runtime-dir}"
    export XDG_RUNTIME_DIR

    xvfb-run -s '-screen 0 1920x1080x24 -nolisten local +iglx -noreset' \
        meson test -C build --print-errorlogs
)

package() {
    DESTDIR="$pkgdir" meson install -C build

    rm -rf "${pkgdir}"/usr/{bin,include,share}
}
