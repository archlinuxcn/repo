pkgname=libui-sh
pkgver=1348562664.47a118f
pkgrel=1
pkgdesc='A shell library providing useful UI functions.'
arch=('any')
url='https://github.com/Dieterbe/libui-sh'
license=('unknown')
groups=()
depends=(bash)
makedepends=(git)
sha1sums=('SKIP')

_gitroot='https://github.com/Dieterbe/libui-sh.git'
_gitname='libui-sh'

source=("${_gitname}::git+${_gitroot}")

pkgver() {
  if [ -d "$srcdir"/$_gitname ]; then
    cd "$srcdir"/$_gitname
    git log --pretty=format:"%ad.%h" --date=format:"%s" -1
  fi
}

package() {
  cd "$srcdir"/$_gitname
  make DESTDIR="$pkgdir" install
}
