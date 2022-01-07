# Maintainer: Stephen Gregoratto <dev@sgregoratto.me>
pkgname=wev-git
pkgver=1.0.0.r2.g54de46d
pkgrel=1
pkgdesc='Print wayland events, like xev(1)'
url='https://git.sr.ht/~sircmpwn/wev'
license=('MIT')
provides=('wev')
arch=('i686' 'x86_64' 'armv6h' 'armv7h')
depends=('wayland' 'libxkbcommon')
makedepends=('git' 'scdoc' 'wayland-protocols')
source=("${pkgname%-git}::git+$url"
	"wev-git.patch")
sha256sums=('SKIP'
            'd93b7cfbee98559178b1e650ae1bbdd7bb2fe07376c76a0312cb17c7529472f9')

pkgver() {
  cd "${pkgname%-git}"
  ( set -o pipefail
    git describe --long 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g' ||
    printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
  )
}

prepare() {
  cd "${pkgname%-git}"
  patch -Np1 -i "$srcdir/wev-git.patch"
}

build() {
  cd "${pkgname%-git}"
  make PREFIX=/usr
}

package() {
  cd "${pkgname%-git}"
  make DESTDIR="$pkgdir" PREFIX="/usr" MANDIR="/usr/share/man" install
  install -Dm644 "LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
