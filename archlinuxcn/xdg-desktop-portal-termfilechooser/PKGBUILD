# Maintainer: shinka <shinnkka1@gmail.com>
pkgname=xdg-desktop-portal-termfilechooser
pkgver=1.4.3
pkgrel=1
pkgdesc='xdg-desktop-portal backend for your favorite terminal file chooser (hunkyburrito fork)'
url="https://github.com/hunkyburrito/xdg-desktop-portal-termfilechooser"
arch=('x86_64')
license=('MIT')
provides=('xdg-desktop-portal-impl' 'xdg-desktop-portal-termfilechooser')
depends=('xdg-desktop-portal' 'libinih')
makedepends=('meson' 'scdoc')
optdepends=(
  'kitty: default terminal for launching wrappers'
  'lf: wrapper included'
  'nnn: wrapper included'
  'ranger: wrapper included'
  'vifm: wrapper included'
  'yazi: wrapper included'
)
source=(
  "${pkgname}-${pkgver}.tar.gz::$url/archive/v${pkgver}.tar.gz"
)
sha512sums=('dfdd1cc8c358119df21c0da9d5867e093a68891689d49a317443ceb75c143d8fe5dd8b1666d00175213381d7bdf05f7bcb4dbd8c0df319b6aba325828254ba20')
conflicts=(xdg-desktop-portal-termfilechooser)

build() {
  cd $pkgname-$pkgver
  arch-meson build
  ninja -C build
}

package() {
  cd $pkgname-$pkgver
  DESTDIR="${pkgdir}" ninja -C build install
  install -Dm644 -t "$pkgdir/usr/share/licenses/${pkgname}" LICENSE
}
