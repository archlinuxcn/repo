# Maintainer: Fabio 'Lolix' Loli <fabio.loli@disroot.org> -> https://github.com/FabioLolix
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Federico Cinelli <cinelli@aur.archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>
# Contributor: Mcder3 <mcder3[at]gmail[dot]com>
# Contributor: MisterFred <mister.fred[at]free[dot]fr>

pkgname=cantata
pkgver=2.5.0
pkgrel=6
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
#depends+=(libtag.so
#          libebur128.so)
optdepends=('ffmpeg: ReplayGain support'
            'libebur128: ReplayGain support'
            'mpd: playback'
            'perl-uri: dynamic playlist'
            'sshfs: remote devices support')
makedepends=(cmake
             ffmpeg
             libebur128
             qt5-tools)
source=("https://github.com/CDrummond/cantata/releases/download/v$pkgver/$pkgname-$pkgver.tar.bz2"
        "cantata-tablib-2.0-compatibility.patch::https://github.com/fenuks/cantata/commit/45bac9eb3e99ed75b6539f92418556dac1c0193d.patch"
        "cantata-ffmpeg-7.0.patch::https://github.com/eclipseo/cantata/commit/0887cf117dd791192531dca47f4ec056a02b7c8a.patch")
sha256sums=('eb7e00ab3f567afaa02ea2c86e2fe811a475afab93182b95922c6eb126821724'
            'f9611a1c1e23b99ffb4ee709ec10982a9289e840ec4014b1bbaff798d226a8ad'
            '6da73f25c313d328fe0d1db665469720c618ab77008f20afe4d9b9db8a8301d7')

prepare() {
  cd "$pkgname-$pkgver"
  patch -Np1 -i ../cantata-tablib-2.0-compatibility.patch
  patch -Np1 -i ../cantata-ffmpeg-7.0.patch
}

build() {
  cmake -B build -S "$pkgname-$pkgver" -Wno-dev \
    -DCMAKE_INSTALL_PREFIX=/usr

  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build
}
