# maintainer: Sergey A. <murlakatamenka@disroot.org>
# ex-maintainer: Robert Cegliński <rob.ceglinski@gmail.com>
# Contributor: Christopher Snowhill <chris@kode54.net>
# Contributor: Denis Zheleztsov <difrex.punk@gmail.com>

pkgname=wlr-randr
pkgver=0.4.0
pkgrel=1
pkgdesc='Utility to manage outputs of a Wayland compositor'
arch=('x86_64')
url='https://sr.ht/~emersion/wlr-randr'
_url='https://git.sr.ht/~emersion/wlr-randr'
license=('MIT')
depends=('wayland')
makedepends=('meson')
source=("$pkgname-$pkgver.tar.gz::${_url}/archive/v$pkgver.tar.gz")
sha256sums=('3bf5446487a165cb071e24197206bb11d5db35ac05445d76184f4ef6b999ac1c')
validpgpkeys=('34FF9526CFEF0E97A340E2E40FDE7BE0E88F5E48')

build() {
  cd "$pkgname-v$pkgver"

  arch-meson build
  meson compile -C build
}

package() {
  cd "$pkgname-v$pkgver"

  meson install -C build --destdir "$pkgdir"
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
