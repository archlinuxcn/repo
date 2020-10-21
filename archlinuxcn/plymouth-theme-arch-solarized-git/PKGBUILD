# Maintainer: Kyle Sferrazza <kyle.sferrazza@gmail.com>

_themename=arch-solarized
_pkgname="plymouth-theme-${_themename}"
pkgname="${_pkgname}-git"
pkgver=r14.f1749f6
pkgrel=1
pkgdesc='A Plymouth theme with a solarized-dark arch linux logo.'
arch=('any')
url="https://github.com/kylesferrazza/${_pkgname}/"
depends=('plymouth')
makedepends=('git')
source=($_pkgname::"git+https://github.com/kylesferrazza/${_pkgname}.git")
sha256sums=('SKIP')

pkgver() {
  cd "$_pkgname"
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
  cd $_pkgname

  _themedir="$pkgdir/usr/share/plymouth/themes/${_themename}"

  install -Dm644 img/bg.png "${_themedir}/img/bg.png"
  install -Dm644 "${_themename}.plymouth" "${_themedir}/${_themename}.plymouth"
  install -Dm644 "${_themename}.script" "${_themedir}/${_themename}.script"
  install -Dm644 img/box.png "${_themedir}/img/box.png"
  install -Dm644 img/bullet.png "${_themedir}/img/bullet.png"
  install -Dm644 img/entry.png "${_themedir}/img/entry.png"
  install -Dm644 img/lock.png "${_themedir}/img/lock.png"
}
