# Maintainer: shinka <shinnkka1@gmail.com>
pkgname=xdg-desktop-portal-termfilechooser
pkgver=1.4.0
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
sha512sums=('a490563ac4f78bf94784894595215f6eb7eaeaedb761f6b54649c2034d4ebec7e8808a1dc23e090d9effe27657a2c4a9de0d89c7baf76549da4fd7a5c294a0b5')
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
