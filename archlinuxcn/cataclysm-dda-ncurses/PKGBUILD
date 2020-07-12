# Maintainer: Reihar <reihar@necronomicon.fr>
# Contributor: Nick Hu <nickhu00@gmail.com>
# Contributor: Fernando Carmona Varo <ferkiwi @t gmail dot com>
pkgname=cataclysm-dda-ncurses
pkgver=0.E.2
_pkgver=0.E-2
pkgrel=3
pkgdesc="Cataclysm: Dark Days Ahead is an actively maintained roguelike set in a post-apocalyptic world, forked from the original. (ncurses only)"
arch=('i686' 'x86_64')
url="http://www.cataclysmdda.com/"
license=('CCPL:by-sa')
depends=('ncurses' 'ncurses')
makedepends=('gettext' 'astyle')
conflicts=('cataclysm-dda' 'cataclysm-dda-git' 'cataclysm-dda-ncurses-bin')

install='cataclysm-dda-ncurses.install'
source=("$pkgname-$_pkgver.tar.gz::https://github.com/CleverRaven/Cataclysm-DDA/archive/${_pkgver}.tar.gz")
sha256sums=('41546e877e2eee79c8492b3ec808ef53a4b9b208d788dac2b1a570ef143426e9')

build() {
  cd "$srcdir/Cataclysm-DDA-${_pkgver}"

  make PREFIX=/usr RELEASE=1 USE_XDG_DIR=1 ZLEVELS=1 LOCALIZE=1
}

package() {
  cd "$srcdir/Cataclysm-DDA-${_pkgver}"

  make DESTDIR="$pkgdir" PREFIX="/usr" RELEASE=1 ZLEVELS=1 LANGUAGES="all" install
  
  #The doc goes in /usr/share/doc  
  install -dm755 "$pkgdir/usr/share/doc/cataclysm-dda"
  unlink doc/JSON_LOADING_ORDER.md
  cp -T data/json/LOADING_ORDER.md doc/JSON_LOADING_ORDER.md
  cp -r *.txt doc/* "$pkgdir/usr/share/doc/cataclysm-dda/"
  
  # License file
  install -Dm644 LICENSE.txt "$pkgdir/usr/share/licenses/${pkgname}/LICENSE"

  #Launcher symlinks
  install -dm755  "$pkgdir/usr/bin/"
}
