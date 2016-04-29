# Maintainer:  Philip Sequeira <phsequei@gmail.com>
# Contributor: Rudolf Polzer <divVerent@xonotic.org>
# Contributor: Bartłomiej Piotrowski <nospam@bpiotrowski.pl>
# Contributor: Eivind Uggedal <eivind@uggedal.com>

# WARNING: The configure script will automatically enable any optional
# features it finds support for on your system. If you want to avoid
# linking against something you have installed, you'll have to disable
# it in the configure below. The package() script will attempt to
# update the dependencies based on dynamic libraries when packaging.

pkgname=mpv-git
_gitname=mpv
pkgver=43170.g304d9d5
pkgrel=1
pkgdesc='Video player based on MPlayer/mplayer2 (git version)'
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
license=('GPL3')
url='https://mpv.io'
_undetected_depends=('hicolor-icon-theme')
depends=('ffmpeg' "${_undetected_depends[@]}")
optdepends=('youtube-dl: for --ytdl')
makedepends=('git' 'python-docutils')
provides=('mpv')
conflicts=('mpv')
options=('!emptydirs')
install=mpv.install
source=('git+https://github.com/mpv-player/mpv'
        'find-deps.py')
md5sums=('SKIP'
         'ffb774b13decbefc62908dda0332046b')
sha256sums=('SKIP'
            'ce974e160347202e0dc63f6a7a5a89e52d2cc1db2d000c661fddb9dc1d007c02')

pkgver() {
  cd "$srcdir/$_gitname"
  #_curtag="$(git rev-list --tags --max-count=1)"
  #_tagver="$(git describe --tags $_curtag | sed -e 's:^v::' -e 's:-:_:g')"
  #_commits="$(git rev-list --count HEAD --since=$_tagver)"
  #_sha="$(git rev-parse --short HEAD)"
  #printf "%s_%s_g%s" $_tagver $_commits $_sha
  echo "$(git rev-list --count HEAD).g$(git rev-parse --short HEAD)"
}

prepare() {
  cd "$srcdir/$_gitname"
  ./bootstrap.py
}

build() {
  cd "$srcdir/$_gitname"

  CFLAGS="$CFLAGS -I/usr/include/samba-4.0"

  ./waf configure --prefix=/usr \
        --confdir=/etc/mpv \
        --enable-zsh-comp \
        --enable-libmpv-shared \
        --enable-gpl3

  ./waf build
}

package() {
  cd "$srcdir/$_gitname"
  ./waf install --destdir="$pkgdir"

  # Update dependencies automatically based on dynamic libraries
  _detected_depends=($("$srcdir"/find-deps.py "$pkgdir"/usr/{bin/mpv,lib/libmpv.so}))
  echo 'Auto-detected dependencies:'
  echo "${_detected_depends[@]}" | fold -s -w 79 | sed 's/^/ /'
  depends=("${_detected_depends[@]}" "${_undetected_depends[@]}")
}
