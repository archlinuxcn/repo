# Maintainer: uzvg <uzvg@qq.com>

pkgname=ibus-table-zhengma-git
_pkgname=${pkgname%-git}
pkgver=1.1.0.20261020.r0.gf3c7069
pkgrel=1
pkgdesc='ZhengMa input method table for IBus (git version)'
arch=('any')
url='https://github.com/uzvg/ibus-table-zhengma'
license=('GPL-3.0-or-later')
depends=('ibus-table')
makedepends=('git' 'meson' 'ninja' 'pkgconf')
provides=("$_pkgname")
conflicts=("$_pkgname")
replaces=("$_pkgname")
source=("git+$url.git")
sha256sums=('SKIP')

pkgver() {
  cd "$_pkgname"
  git describe --long --tags --abbrev=7 | sed 's/^v//; s/\([^-]*-g\)/r\1/; s/-/./g'
}

build() {
  cd "$_pkgname"
  meson setup build --prefix=/usr --buildtype=plain
  meson compile -C build
}

package() {
  cd "$_pkgname"
  DESTDIR="$pkgdir" meson install -C build
  install -Dm644 COPYING "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}
