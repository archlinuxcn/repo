# Maintainer: juanrubio

_githubname=tizonia-openmax-il
pkgname=tizonia-all
pkgver=0.22.0
pkgrel=1
pkgdesc="Command-line cloud music player for Linux with support for Spotify, Google Play Music, YouTube, SoundCloud, TuneIn, iHeartRadio, Plex servers and Chromecast devices."
arch=('x86_64')
url="https://tizonia.org"
license=('LGPL')
makedepends=(git boost meson ninja)
depends=(
    # official repositories:
    'libmad'
    'sqlite'
    'libutil-linux'
    'taglib'
    'mediainfo'
    'sdl'
    'lame'
    'faad2'
    'libcurl-gnutls'
    'libvorbis'
    'libvpx'
    'mpg123'
    'opus'
    'opusfile'
    'libogg'
    'libfishsound'
    'flac'
    'liboggz'
    'libsndfile'
    'alsa-lib'
    'libpulse'
    'boost-libs'
    'hicolor-icon-theme'
    'python-pafy'
    'python-eventlet'
    'youtube-dl'
    'python-levenshtein'
    'python-joblib'

    # AUR:
    'log4c'
    'libspotify'
    'python-gmusicapi'
    'python-soundcloud'
    'python-pychromecast'
    'python-plexapi'
    'python-fuzzywuzzy'
    'python-spotipy'
)
source=("${_githubname}-${pkgver}.tar.gz"::"https://github.com/tizonia/${_githubname}/archive/v${pkgver}.tar.gz")
md5sums=('236dd33a25700bf8d752af17b95bd50f')

prepare() {
  command -v tizonia &> /dev/null \
      && { \
      echo >&2 "Please uninstall tizonia-all or tizonia-all-git before proceeding." ; \
      echo >&2 "See https://github.com/tizonia/tizonia-openmax-il/issues/485." ; \
      exit 1; }
  mkdir -p "$srcdir/path"
}

build() {
    cd "${_githubname}-${pkgver}"
    pwd
    CFLAGS='-O2 -s -DNDEBUG' \
    CXXFLAGS='-O2 -s -DNDEBUG -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security' \
    arch-meson build -Dbashcompletiondir=/usr/share/bash-completion/completions -Dzshcompletiondir=/usr/share/zsh/site-functions
    ninja -j1 -C build
}

package() {
    cd "${_githubname}-${pkgver}"
    pwd
    DESTDIR=$pkgdir ninja -C build install
}
