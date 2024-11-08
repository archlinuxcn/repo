# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Bartłomiej Piotrowski <bpiotrowski@archlinux.org>
# Contributor: Ionut Biru <ibiru@archlinux.org>
# Contributor: Tom Newsom <Jeepster@gmx.co.uk>
# Contributor: Paul Mattal <paul@archlinux.org>

_pkgname=ffmpeg
pkgname=${_pkgname}6.1
pkgver=6.1.2
pkgrel=2
pkgdesc='Complete solution to record, convert and stream audio and video (legacy v6.1)'
arch=(x86_64)
url=https://ffmpeg.org
license=(GPL-3.0-only)
depends=(
  alsa-lib
  aom
  bzip2
  cairo
  dav1d
  fontconfig
  freetype2
  fribidi
  glib2
  glibc
  gmp
  gnutls
  gsm
  harfbuzz
  jack
  lame
  libass
  libavc1394
  libbluray
  libbs2b
  libdrm
  libgl
  libiec61883
  libjxl
  libmodplug
  libopenmpt
  libplacebo
  libpulse
  libraw1394
  librsvg
  libsoxr
  libssh
  libtheora
  libva
  libvdpau
  libvorbis
  libvpx
  libwebp
  libx11
  libxcb
  libxext
  libxml2
  libxv
  ocl-icd
  onevpl
  opencore-amr
  openjpeg2
  opus
  rav1e
  rubberband
  sdl2
  snappy
  speex
  srt
  svt-av1
  v4l-utils
  vapoursynth
  vid.stab
  vmaf
  vulkan-icd-loader
  x264
  x265
  xvidcore
  xz
  zimg
  zlib
)
makedepends=(
  amf-headers
  avisynthplus
  clang
  ffnvcodec-headers
  frei0r-plugins
  git
  ladspa
  mesa
  nasm
  opencl-headers
  vulkan-headers
)
optdepends=(
  'avisynthplus: AviSynthPlus support'
  'frei0r-plugins: Frei0r video effects support'
  'intel-media-sdk: Intel QuickSync support (legacy)'
  'ladspa: LADSPA filters'
  'nvidia-utils: Nvidia NVDEC/NVENC support'
  'onevpl-intel-gpu: Intel QuickSync support'
)
_tag=b1a4534186ca51b0457579fc05a5739eb2cc45cd
source=(
  git+https://git.ffmpeg.org/ffmpeg.git#tag=${_tag}
  add-av_stream_get_first_dts-for-chromium.patch
)
b2sums=('3b34bb1ff8f909d95c554fa40275f7dda0bb4e922480ae0bb990a7c33c250ca36109cb5ad0dafb6fa028dd5ff66f7c5d028a1eedc2ce81e1507527db2a7b41ff'
        '555274228e09a233d92beb365d413ff5c718a782008075552cafb2130a3783cf976b51dfe4513c15777fb6e8397a34122d475080f2c4483e8feea5c0d878e6de')
#validpgpkeys=(DD1EC9E8DE085C629B3E1846B18E8928B3948D64) # Michael Niedermayer <michael@niedermayer.cc>

prepare() {
  cd "${_pkgname}"
  # FS#79281: fix assembling with binutil as >= 2.41
  git cherry-pick -n effadce6c756247ea8bae32dc13bb3e6f464f0eb
  # FS#77813: fix playing ogg files with mplayer
  git cherry-pick -n cbcc817353a019da4332ad43deb7bbc4e695d02a
  patch -Np1 -i ../add-av_stream_get_first_dts-for-chromium.patch # https://crbug.com/1251779
  # use non-deprecated nvenc GUID for conftest
  git cherry-pick -n 03823ac0c6a38bd6ba972539e3203a592579792f
  # Fix VDPAU vo
  git cherry-pick -n e9c93009fc34ca9dfcf0c6f2ed90ef1df298abf7
  # Fix bug in av_fft_end
  git cherry-pick -n a562cfee2e214252f8b3f516527272ae32ef9532
  git cherry-pick -n 250471ea1745fc703eb346a2a662304536a311b1
  # Fix build with latest vulkan headers
  git cherry-pick -n fef22c87ada4517441701e6e61e062c9f4399c8e
  # Fix nvenc
  git cherry-pick -n 06c2a2c425f22e7dba5cad909737a631cc676e3f
  git cherry-pick -n 9d675bb60d2542631f37613aa92b7e1144bbeaa1
  git cherry-pick -n 43b417d516b0fabbec1f02120d948f636b8a018e
}

pkgver() {
  cd "${_pkgname}"
  git describe --tags | sed 's/^n//'
}

build() {
  cd "${_pkgname}"

  export CFLAGS+=' -Wno-error=incompatible-pointer-types'

  ./configure \
    --prefix=/usr \
    --incdir="/usr/include/${pkgname}" \
    --libdir="/usr/lib/${pkgname}" \
    --disable-debug \
    --disable-static \
    --disable-stripping \
    --disable-doc \
    --disable-programs \
    --enable-amf \
    --enable-avisynth \
    --enable-cuda-llvm \
    --enable-lto \
    --enable-fontconfig \
    --enable-frei0r \
    --enable-gmp \
    --enable-gnutls \
    --enable-gpl \
    --enable-ladspa \
    --enable-libaom \
    --enable-libass \
    --enable-libbluray \
    --enable-libbs2b \
    --enable-libdav1d \
    --enable-libdrm \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libgsm \
    --enable-libharfbuzz \
    --enable-libiec61883 \
    --enable-libjack \
    --enable-libjxl \
    --enable-libmodplug \
    --enable-libmp3lame \
    --enable-libopencore_amrnb \
    --enable-libopencore_amrwb \
    --enable-libopenjpeg \
    --enable-libopenmpt \
    --enable-libopus \
    --enable-libplacebo \
    --enable-libpulse \
    --enable-librav1e \
    --enable-librsvg \
    --enable-librubberband \
    --enable-libsnappy \
    --enable-libsoxr \
    --enable-libspeex \
    --enable-libsrt \
    --enable-libssh \
    --enable-libsvtav1 \
    --enable-libtheora \
    --enable-libv4l2 \
    --enable-libvidstab \
    --enable-libvmaf \
    --enable-libvorbis \
    --enable-libvpl \
    --enable-libvpx \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libxcb \
    --enable-libxml2 \
    --enable-libxvid \
    --enable-libzimg \
    --enable-nvdec \
    --enable-nvenc \
    --enable-opencl \
    --enable-opengl \
    --enable-shared \
    --enable-vapoursynth \
    --enable-version3 \
    --enable-vulkan
  make
}

package() {
  depends+=(
    libass.so
    libbluray.so
    libbs2b.so
    libdav1d.so
    libfreetype.so
    libharfbuzz.so
    libjxl.so
    libopenmpt.so
    libplacebo.so
    librav1e.so
    librsvg-2.so
    librubberband.so
    libva.so
    libva-drm.so
    libva-x11.so
    libvidstab.so
    libvorbisenc.so
    libvorbis.so
    libvpx.so
    libx264.so
    libx265.so
    libxvidcore.so
    libzimg.so
  )

  make DESTDIR="${pkgdir}" -C "${_pkgname}" install

  cd "${pkgdir}"
  local file
  for file in "usr/lib/${pkgname}/"*; do
    if [[ "$file" == *.so ]]; then
      ln -srfv -- usr/lib/"$(readlink "$file")" "$file"
    elif [[ ! -d "$file" ]]; then
      mv -v "$file" usr/lib
    fi
  done

  rm -rv usr/share
}

# vim: ts=2 sw=2 et:
