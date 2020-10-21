# Maintainer: Jiri Tyr <jiri.tyr@gmail.com>

_pkgname=plymouth-theme-arch-breeze
pkgname="${_pkgname}-git"
pkgver=r4.f7789af
pkgrel=1
pkgdesc='Plymouth theme for Arch Linux inspired by KDE Breeze.'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h')
url="https://github.com/jtyr/${_pkgname}/"
license=('MIT')
install="${pkgname}.install"
depends=('plymouth')
makedepends=('git')
source=("git+https://github.com/jtyr/$_pkgname.git")
sha256sums=('SKIP')

pkgver() {
  cd "$_pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd "$_pkgname"

  _themedir="$pkgdir/usr/share/plymouth/themes/arch-breeze"

  for N in *.png arch-breeze.plymouth script; do
    install -Dm644 $N "${_themedir}/$N"
  done

  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  install -Dm644 README.md "$pkgdir/usr/share/doc/$pkgname/README.md"
}

# vim:set ts=2 sw=2 et:
