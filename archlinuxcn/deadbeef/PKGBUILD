# Maintainer: Lukas Fleischer <lfleischer@archlinux.org>
# Contributor: Alexey Yakovenko <waker@users.sourceforge.net>

pkgname=deadbeef
pkgver=1.8.4
pkgrel=1
pkgdesc='A GTK+ audio player for GNU/Linux.'
arch=('x86_64')
url='http://deadbeef.sourceforge.net'
license=('GPL2')
depends=('alsa-lib' 'hicolor-icon-theme' 'desktop-file-utils' 'jansson')
makedepends=('libvorbis' 'libmad' 'flac' 'curl' 'imlib2' 'wavpack' 'libsndfile' 'libcdio' 'libcddb'
             'libx11' 'faad2' 'zlib' 'intltool' 'pkgconfig' 'libpulse' 'libzip' 'libsamplerate'
             'yasm' 'ffmpeg' 'gtk2' 'gtk3')
optdepends=('gtk2: for the GTK2 interface'
            'gtk3: for the GTK3 interface'
            'libsamplerate: for Resampler plugin'
            'libvorbis: for Ogg Vorbis playback'
            'libmad: for MP1/MP2/MP3 playback'
            'mpg123: for MP1/MP2/MP3 playback'
            'flac: for FLAC playback'
            'curl: for Last.fm scrobbler, SHOUTcast, Icecast, Podcast support'
            'imlib2: for artwork plugin'
            'wavpack: for WavPack playback'
            'libsndfile: for Wave playback'
            'libcdio: audio cd plugin'
            'libcddb: audio cd plugin'
            'faad2: for AAC/MP4 support'
            'dbus: for OSD notifications support'
            'pulseaudio: for PulseAudio output plugin'
            'libx11: for global hotkeys plugin'
            'zlib: for Audio Overload plugin'
            'libzip: for vfs_zip plugin'
            'ffmpeg: for ffmpeg plugin')
source=("https://github.com/DeaDBeeF-Player/${pkgname}/archive/${pkgver}.tar.gz")
sha512sums=('18c54ae2c7931419ea06f3eb581cc8e704fa6eb87d330fc09f7295f4a8ef6e88b6f8c314223c34c321cd2a54f14cb6911add41602250c39c1b1c1edbf64d63b7')

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	
	./autogen.sh 
	./configure --prefix=/usr
}

build () {
	cd "${srcdir}/${pkgname}-${pkgver}"
	make
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	make DESTDIR="$pkgdir" install
}
