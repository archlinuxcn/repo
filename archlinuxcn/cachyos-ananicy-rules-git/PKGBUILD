# Maintainer: Julien Virey <julien.virey@gmail.com>

pkgname=cachyos-ananicy-rules-git
_gitname=ananicy-rules
pkgver=20230613.r319.gf139cf4
pkgrel=1
groups=('cachyos')
arch=('any')
license=('GPL')
pkgdesc='CachyOS - ananicy-rules'
url='https://github.com/CachyOS/ananicy-rules'
depends=('ananicy-cpp')
makedepends=('git')
source=("git+https://github.com/CachyOS/$_gitname")
sha256sums=('SKIP')
replaces=('ananicy-rules-git' 'cachyos-ananicy-rules')
provides=('ananicy-rules-git' 'cachyos-ananicy-rules')
conflicts=('ananicy-rules-git' 'cachyos-ananicy-rules' 'ananicy-git')
backup=(etc/ananicy.d/ananicy.conf)

pkgver() {
  cd $_gitname
  echo "$(git show --format='%cI' -q master | sed 's/T.*//g;s/-//g').r$(git rev-list --count HEAD).g$(git rev-parse --short HEAD)"
}

prepare() {
  cd $_gitname
  rm -f README.md
}

package() {
  cd $_gitname
  install -d "$pkgdir/etc/ananicy.d"
  cp -rf $srcdir/$_gitname/* "$pkgdir/etc/ananicy.d"
}
