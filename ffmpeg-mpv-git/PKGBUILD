# Maintainer : Daniel Bermond < yahoo-com: danielbermond >

pkgname=ffmpeg-mpv-git
pkgver=3.5.r88464.gd89410402a
pkgrel=1
pkgdesc='Complete solution to record, convert and stream audio and video (modified for mpv, git version)'
arch=('i686' 'x86_64')
url='http://www.ffmpeg.org/'
license=('GPL3')
depends=('alsa-lib' 'bzip2' 'fontconfig' 'fribidi' 'glibc' 'gmp' 'gnutls' 'gsm'
         'jack' 'lame' 'libavc1394' 'libiec61883' 'libmodplug' 'libpulse'
         'libraw1394' 'libsoxr' 'libssh' 'libtheora' 'libva' 'libvdpau'
         'libwebp' 'libx11' 'libxcb' 'opencore-amr' 'openjpeg2' 'opus'
         'sdl2' 'speex' 'v4l-utils' 'xz' 'zlib'
         'libass.so' 'libbluray.so' 'libfreetype.so' 'libvidstab.so'
         'libvorbisenc.so' 'libvorbis.so' 'libvpx.so'
         'libx264.so' 'libx265.so' 'libxvidcore.so')
makedepends=('git' 'ladspa' 'nasm')
optdepends=('ladspa: LADSPA filters')
provides=('libavcodec.so' 'libavdevice.so' 'libavfilter.so' 'libavformat.so'
          'libavresample.so' 'libavutil.so' 'libpostproc.so' 'libswresample.so'
          'libswscale.so')
source=("$pkgname"::'git+https://github.com/mpv-player/ffmpeg-mpv.git')
sha256sums=('SKIP')

pkgver() {
    cd "$pkgname"
    local _version="$(  git describe  --tags --long      | cut -d'-' -f1 | sed 's/^n//')"
    local _revision="$( git describe  --tags --match 'N' | cut -d'-' -f2)"
    local _shorthash="$(git rev-parse --short HEAD)"
    printf '%s.r%s.g%s' "$_version" "$_revision" "$_shorthash"
}

build() {
    cd "$pkgname"
    
    msg2 'Running ffmpeg configure script. Please wait...'
    
    ./configure \
        --prefix='/usr' \
        --incdir='/usr/include/ffmpeg-mpv-git' \
        --libdir='/usr/lib/ffmpeg-mpv-git' \
        --shlibdir='/usr/lib/ffmpeg-mpv-git' \
        --enable-rpath \
        --disable-debug \
        --disable-static \
        --disable-stripping \
        --enable-avisynth \
        --enable-avresample \
        --enable-fontconfig \
        --enable-gmp \
        --enable-gnutls \
        --enable-gpl \
        --enable-ladspa \
        --enable-libass \
        --enable-libbluray \
        --enable-libfreetype \
        --enable-libfribidi \
        --enable-libgsm \
        --enable-libiec61883 \
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
        --enable-libxvid \
        --enable-shared \
        --enable-version3
    make
    make tools/qt-faststart
}

package() {
    cd "$pkgname"
    make DESTDIR="$pkgdir" install
    rm -rf "${pkgdir}/usr/share"
    
    find "${pkgdir}/usr/bin" -type f -exec mv {} {}-mpv-git \;
    
    install -d -m755 "${pkgdir}/etc/ld.so.conf.d"
    printf '%s\n%s\n' '/usr/lib/' '/usr/lib/ffmpeg-mpv-git/' > "${pkgdir}/etc/ld.so.conf.d/51-ffmpeg-mpv-git.conf"
} 
