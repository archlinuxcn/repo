# Maintainer: Jeremy Gust <jeremy AT plasticsoup DOT net>
pkgname=hyprpicker
pkgver=0.2.0
pkgrel=2
pkgdesc="A wlroots-compatible Wayland color picker that does not suck."
arch=(x86_64)
url="https://github.com/hyprwm/hyprpicker"
license=('BSD')
depends=('cairo' 'libxkbcommon' 'wayland')
optdepends=('wl-clipboard: Allows --autocopy to automatically copy the output to the clipboard.')
makedepends=('cmake'
             'libglvnd'
             'libjpeg-turbo'
             'ninja'
             'pango'
             'wayland-protocols'
             'wlroots'
             )
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('fa1b0c29682f5ede5a03d754770d152f38d869bc1faa300564680cef2de0758a')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  make all
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  install -Dm755 build/hyprpicker "$pkgdir/usr/bin/hyprpicker"
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 doc/hyprpicker.1 "$pkgdir/usr/share/man/man1/hyprpicker.1"
  install -Dm644 README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
}
