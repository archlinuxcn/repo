# Maintainer: Nicolas Lenz <nicolas@eisfunke.com>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Ionut Biru <ibiru@archlinux.org>
# Contributor: Tom Newsom <Jeepster@gmx.co.uk>
# Contributor: Paul Mattal <paul@archlinux.org>

pkgname=ffmpeg4.0
pkgver=4.0.3
pkgrel=1
epoch=1
pkgdesc='Complete solution to record, convert and stream audio and video, version 4.0'
arch=('x86_64')
url='http://ffmpeg.org/'
license=('GPL3')
depends=(
  'alsa-lib' 'aom' 'bzip2' 'fontconfig' 'fribidi' 'glibc' 'gmp' 'gnutls' 'gsm'
  'jack' 'lame' 'libavc1394' 'libdrm' 'libiec61883' 'libmodplug'
  'libomxil-bellagio' 'libpulse' 'libraw1394' 'libsoxr' 'libssh' 'libtheora'
  'libvdpau' 'libwebp' 'libx11' 'libxcb' 'libxext' 'libxml2' 'libxv'
  'opencore-amr' 'openjpeg2' 'opus' 'sdl2' 'speex' 'v4l-utils' 'xz' 'zlib'
  'libass.so' 'libbluray.so' 'libfreetype.so' 'libva-drm.so' 'libva.so'
  'libva-x11.so' 'libvidstab.so' 'libvorbisenc.so' 'libvorbis.so' 'libvpx.so'
  'libx264.so' 'libx265.so' 'libxvidcore.so'
)
makedepends=('ffnvcodec-headers' 'git' 'ladspa' 'yasm')
optdepends=('ladspa: LADSPA filters')
provides=(
  'libavcodec.so' 'libavdevice.so' 'libavfilter.so' 'libavformat.so'
  'libavutil.so' 'libpostproc.so' 'libswresample.so' 'libswscale.so' 'ffmpeg=4.0.3'
)
conflicts=('ffmpeg')
source=("git+https://git.ffmpeg.org/ffmpeg.git#tag=n${pkgver}")
sha256sums=('SKIP')

build() {
  cd ffmpeg

  ./configure \
    --prefix='/usr' \
    --disable-debug \
    --disable-static \
    --disable-stripping \
    --enable-fontconfig \
    --enable-gmp \
    --enable-gnutls \
    --enable-gpl \
    --enable-ladspa \
    --enable-libaom \
    --enable-libass \
    --enable-libbluray \
    --enable-libdrm \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libgsm \
    --enable-libiec61883 \
    --enable-libjack \
    --enable-libmodplug \
    --enable-libmp3lame \
    --enable-libopencore_amrnb \
    --enable-libopencore_amrwb \
    --enable-libopenjpeg \
    --enable-libopus \
    --enable-libpulse \
    --enable-libsoxr \
    --enable-libspeex \
    --enable-libssh \
    --enable-libtheora \
    --enable-libv4l2 \
    --enable-libvidstab \
    --enable-libvorbis \
    --enable-libvpx \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libxcb \
    --enable-libxml2 \
    --enable-libxvid \
    --enable-nvdec \
    --enable-nvenc \
    --enable-omx \
    --enable-shared \
    --enable-version3

  make
  make tools/qt-faststart
  make doc/ff{mpeg,play}.1
}

package() {
  make DESTDIR="${pkgdir}" -C ffmpeg install install-man
  install -Dm 755 ffmpeg/tools/qt-faststart "${pkgdir}"/usr/bin/
}

# vim: ts=2 sw=2 et:
