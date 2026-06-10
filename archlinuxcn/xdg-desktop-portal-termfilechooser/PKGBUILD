# Maintainer: shinka <shinnkka1@gmail.com>
pkgname=xdg-desktop-portal-termfilechooser
pkgver=1.4.2
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
sha512sums=('453646d1f5c33c54c8334b42f0c7375eda90c26f29b9ceff36a5122be749d743d45a41fb57f0cbdee0137c29aa17e21a76e47aba441ebfd486f9735e010248ee')
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
