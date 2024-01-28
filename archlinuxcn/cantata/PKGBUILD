# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor:  Federico Cinelli <cinelli@aur.archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Mcder3 <mcder3[at]gmail[dot]com>
# Contributor: MisterFred <mister.fred[at]free[dot]fr>

pkgname=cantata
pkgver=2.5.0
pkgrel=4
pkgdesc='Qt5 client for the music player daemon (MPD)'
arch=(x86_64)
url='https://github.com/CDrummond/cantata'
license=(GPL3)
depends=(libcddb
         libcdio-paranoia
         libmtp
         libmusicbrainz5
         media-player-info
         mpg123
         qt5-multimedia
         qt5-svg
         taglib
         udisks2)
optdepends=('ffmpeg: ReplayGain support'
            'libebur128: ReplayGain support'
            'mpd: playback'
            'perl-uri: dynamic playlist'
            'sshfs: remote devices support')
makedepends=(cmake
             ffmpeg
             libebur128
             qt5-tools)
source=(https://github.com/CDrummond/cantata/releases/download/v$pkgver/$pkgname-$pkgver.tar.bz2)
sha256sums=('eb7e00ab3f567afaa02ea2c86e2fe811a475afab93182b95922c6eb126821724')

build() {
  cmake -B build -S $pkgname-$pkgver \
    -DCMAKE_INSTALL_PREFIX=/usr
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
