# Maintainer: Dmitry Kharitonov <darksab0r at gmail com>
# Contributor: Daniel Bermond < yahoo-com: danielbermond >
# Contributor: rcpoison <rc dot poison at gmail dot com>
# Contributor: Gerad Munsch <gmunsch@unforgivendevelopment.com>
# Contributor: Rudolf Polzer <divVerent[at]xonotic[dot]org>
# Contributor: Ionut Biru <ibiru@archlinux.org>
# Contributor: Tom Newsom <Jeepster@gmx.co.uk>
# Contributor: Paul Mattal <paul@archlinux.org>

# If you don't want CUDA/CUVID support, you can remove
# depends_x86_64=('cuda') line and 
# $_cuda \, $_cuvid \, $_libnpp \ lines from PKGBUILD
#
# Add "--enable-decklink \" to configure flags
# if you have decklink-sdk installed

pkgname=ffmpeg-full-nvenc
_pkgbasename=ffmpeg
pkgver=3.1.1
pkgrel=8
epoch=1
pkgdesc="Record, convert, and stream audio and video (all codecs including Nvidia NVENC)"
arch=('i686' 'x86_64')
url="http://ffmpeg.org/"
license=('GPL' 'custom:UNREDISTRIBUTABLE')
depends=('alsa-lib' 'bzip2' 'celt' 'chromaprint-fftw' 'faac' 'flite' 'fontconfig' 'frei0r-plugins'
         'fribidi' 'glibc' 'gnutls' 'gsm' 'jack' 'kvazaar' 'ladspa' 'lame' 'libass' 
         'libavc1394' 'libbluray' 'libbs2b' 'libcaca' 'libcdio-paranoia' 'libcl' 'libdc1394'
         'libebur128' 'libfdk-aac' 'libgme' 'libiec61883' 'libilbc' 'libmfx-git' 'libmodplug'
         'libomxil-bellagio' 'libpulse' 'libsoxr' 'libssh' 'libtheora' 'libva' 'libvdpau' 'libwebp'
         'libxv' 'mesa' 'netcdf' 'nut-multimedia-git' 'openal' 'opencore-amr' 'opencl-headers'
         'opus' 'rubberband' 'rtmpdump' 'schroedinger' 'sdl' 'smbclient' 'speex' 'shine'
         'tesseract' 'twolame' 'v4l-utils' 'vid.stab' 'vo-amrwbenc' 'libxcb' 'xvidcore' 
         'wavpack' 'zeromq' 'zimg' 'zlib' 'zvbi' 'nvidia-utils'
         'libvorbisenc.so' 'libvorbis.so' 'libvpx.so' 'libx264.so' 'x265'
         'snappy' 'openh264' 'xavs' 'java-environment')
depends_x86_64=('cuda')
makedepends=('hardening-wrapper' 'libvdpau' 'nvidia-sdk' 'yasm' 'git')
optdepends=('avxsynth-git: for Avisynth support'
            'blackmagic-decklink-sdk: for Blackmagic DeckLink support; need to add --enable-decklink option in this PKGBUILD')
optdepends_x86_64=('intel-media-sdk: for Intel QSV support (Experimental! See PKGBUILD of that package for additional info)')
conflicts=('ffmpeg' 'ffmpeg-full' 'ffmpeg-git' 'ffmpeg-full-git' 'ffmpeg-full-extra')
provides=('libavcodec.so' 'libavdevice.so' 'libavfilter.so' 'libavformat.so'
          'libavresample.so' 'libavutil.so' 'libpostproc.so' 'libswresample.so'
          'libswscale.so' 'ffmpeg' 'qt-faststart')
source=(http://ffmpeg.org/releases/$_pkgbasename-$pkgver.tar.bz2{,.asc}
        'openh264-1.6-fix.patch'
        'UNREDISTRIBUTABLE.txt')
validpgpkeys=('FCF986EA15E6E293A5644F10B4322F04D67658D8')
sha256sums=('a5bca50a90a37b983eaa17c483a387189175f37ca678ae7e51d43e7610b4b3b4'
            'SKIP'
            '5120e4ff1399d454f9232f5d379d2f20930f2d89915b9d332a6594b2be830778'
            'e0c1b126862072a71e18b9580a6b01afc76a54aa6e642d2c413ba0ac9d3010c4')

prepare() {
  cd "$_pkgbasename-$pkgver"
  git apply ../openh264-1.6-fix.patch
}

build() {
  cd $_pkgbasename-$pkgver

  # Add x86_64 (opt)depends to the build
  if [ "$CARCH" = "x86_64" ]; then
      _cuda="--enable-cuda"
      _cudainc="-I/opt/cuda/include"
      _cudalib="-L/opt/cuda/lib64"
      _cuvid="--enable-cuvid"
      _libnpp="--enable-libnpp"
      _intelsdklib="-Wl,-rpath -Wl,/opt/intel/mediasdk/lib64"
  else
      _cuda=""
      _cudainc=""
      _cudalib=""
      _cuvid=""
      _libnpp=""
     _intelsdklib=""
  fi

  msg "Starting configure..."

  ## Add "--enable-decklink \" 
  ## if you have decklink-sdk installed
  ./configure \
    --prefix=/usr \
    --extra-cflags="-I/usr/include/nvidia-sdk \
                    ${_cudainc} \
                    -I/usr/lib/jvm/$(archlinux-java get)/include \
                    -I/usr/lib/jvm/$(archlinux-java get)/include/linux" \
    --extra-ldflags="${_cudalib} ${_intelsdklib}" \
    \
    --enable-rpath \
    --enable-gpl \
    --enable-version3 \
    --enable-nonfree \
    --disable-static \
    --enable-shared \
    --enable-avresample \
    \
    \
    $_cuda \
    $_cuvid \
    $_libnpp \
    \
    --enable-libmfx \
    --enable-nvenc \
    --enable-omx \
    --enable-omx-rpi \
    \
    \
    --enable-avisynth \
    --enable-audiotoolbox \
    --enable-chromaprint \
    --enable-decoder=atrac3 \
    --enable-decoder=atrac3p \
    --enable-bzlib \
    --enable-fontconfig \
    --enable-frei0r \
    --enable-gnutls \
    --enable-gpl \
    --enable-gray \
    --enable-iconv \
    --enable-jni \
    --enable-ladspa \
    --enable-libass \
    --enable-libbluray \
    --enable-libbs2b \
    --enable-libcaca \
    --enable-libcdio \
    --enable-libcelt \
    --enable-libdc1394 \
    --enable-libebur128 \
    --enable-libfaac \
    --enable-libfdk-aac \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libgme \
    --enable-libgsm \
    --enable-libiec61883 \
    --enable-libilbc \
    --enable-libkvazaar \
    --enable-libmodplug \
    --enable-libmp3lame \
    --enable-libnut \
    --enable-libopencore-amrnb \
    --enable-libopencore-amrwb \
    --enable-libopencv \
    --enable-libopenh264 \
    --disable-libopenjpeg \
    --enable-libopus \
    --enable-libpulse \
    --enable-librubberband \
    --enable-librtmp  \
    --enable-libschroedinger \
    --enable-libshine \
    --enable-libsmbclient \
    --enable-libsnappy \
    --enable-libsoxr \
    --enable-libspeex \
    --enable-libssh \
    --enable-libtesseract \
    --enable-libtheora \
    --enable-libtwolame \
    --enable-libv4l2 \
    --enable-libvidstab \
    --enable-libvo-amrwbenc \
    --enable-libvorbis \
    --enable-libvpx \
    --enable-libwavpack \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libxavs \
    --enable-libxcb \
    --enable-libxcb-shm \
    --enable-libxcb-xfixes \
    --enable-libxcb-shape \
    --enable-libxvid \
    --enable-libzimg \
    --enable-libzmq \
    --enable-libzvbi \
    --enable-mediacodec \
    --enable-netcdf \
    --enable-openal \
    --enable-opencl \
    --enable-opengl \
    --enable-openssl \
    --enable-sdl \
    --enable-vaapi \
    --enable-vda \
    --enable-vdpau \
    --enable-videotoolbox \
    --enable-x11grab \
    --enable-xlib \
    --enable-zlib

    
  msg "Starting make"
  make
  make tools/qt-faststart
  make doc/ff{mpeg,play,server}.1
}

package() {
  cd $_pkgbasename-$pkgver
  make DESTDIR="$pkgdir" install install-man
  install -Dm 755 tools/qt-faststart "${pkgdir}"/usr/bin/
  install -Dm 644 "$srcdir"/UNREDISTRIBUTABLE.txt "$pkgdir/usr/share/licenses/$pkgname/UNREDISTRIBUTABLE.txt"
}
