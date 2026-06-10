# Maintainer: shinka <shinnkka1@gmail.com>
pkgname=xdg-desktop-portal-termfilechooser
pkgver=1.4.1
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
sha512sums=('b66d561fed77b7793fff2c48b843a4cc41347801cefb8fa262605762c4a7504615ab4cc27120fe38fbb5ea860bb0843e10c7187ed5c2dc4d17e01ff71fe8d5db')
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
