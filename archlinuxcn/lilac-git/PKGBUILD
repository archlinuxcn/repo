# Maintainer: malacology
# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

_pkgname=lilac
pkgname=$_pkgname-git
pkgver=r874.b991d69
pkgrel=2
pkgdesc='The build bot for archlinuxcn'
arch=(any)
url='https://github.com/archlinuxcn/lilac'
license=(GPL3)
depends=(python git devtools nvchecker gnupg pid_children fakeroot bubblewrap pacman-contrib
         python-requests python-lxml python-yaml python-toml pyalpm
         python-structlog python-prctl)
makedepends=(python-setuptools-scm)
optdepends=(
  'smtp-forwarder: for sending error reports'
)
checkdepends=(python-pytest)
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")
source=('git+https://github.com/archlinuxcn/lilac.git')
sha256sums=('SKIP')

pkgver() {
  cd $_pkgname
  printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd $_pkgname
  python setup.py build
}

check() {
  cd $_pkgname
  pytest
}

package() {
  cd $_pkgname
  python setup.py install --root="$pkgdir" --optimize=1 --skip-build
  install -Dm644 config.toml.sample -t "$pkgdir"/usr/share/doc/lilac
}
