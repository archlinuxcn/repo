# Mantainer: Franco Tortoriello

pkgname=dosbox-x-git
pkgver=6778.7922cd7ac
pkgrel=1
pkgdesc="x86 emulator with builtin DOS, with patches with more features"
arch=(i686 x86_64)
url="http://dosbox.sourceforge.net"
license=(GPL)
depends=(fluidsynth libxkbfile libpng libxrandr mesa ffmpeg)
makedepends=(git glu)
optdepends=()
source=(dosbox-x::git://github.com/joncampbell123/dosbox-x.git
	dosbox-x.png
	dosbox-x.desktop)

pkgver() {
  cd "$SRCDEST/dosbox-x"
  echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

build() {
  cd "$srcdir/dosbox-x"
  ./build
}

package() {
  cd "$srcdir/dosbox-x"
  make DESTDIR="$pkgdir" install
  install -Dm644 "$srcdir/dosbox-x.png" \
	"$pkgdir/usr/share/pixmaps/dosbox-x.png"
  install -Dm644 "$srcdir/dosbox-x.desktop" \
	"$pkgdir/usr/share/applications/dosbox-x.desktop"
}

md5sums=('SKIP'
         '3dcfe45c5ed0433316eaea51e3620b36'
	 '615228a51b52d4788c73940602f1dc97')

