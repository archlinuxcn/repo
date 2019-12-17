# Maintainer: Jerome Leclanche <jerome@leclan.ch>
# Maintainer: Chih-Hsuan Yen <yan12125@archlinux.org>

_pkgname=qtermwidget
pkgname=$_pkgname-git
pkgver=0.14.1.52.g51bfdd6
pkgrel=1
pkgdesc="A terminal widget for Qt, used by QTerminal"
arch=("x86_64")
url="https://github.com/lxqt/qtermwidget"
# Yep, it's messy when you're talking about licenses
license=("LGPL" "custom:BSD" "custom:Public Domain")
depends=("qt5-base")
makedepends=("git" "cmake" "lxqt-build-tools-git" "qt5-tools"
             "python-pyqt5" "python-sip" "sip")
provides=("$_pkgname=$pkgver")
conflicts=("$_pkgname")
optdepends=(
  'python: PyQt5 bindings'
)
source=("git+https://github.com/lxqt/$_pkgname.git"
        'pyqt5-path.diff')
sha256sums=('SKIP'
            'cbc3afac3341fa92e06af8d9f1ab3b2198fe2f53feac718865ef3dc89da19a5c')

pkgver() {
  cd $_pkgname
  git describe --always | sed "s/-/./g"
}

prepare() {
  cd $_pkgname
  # https://git.archlinux.org/svntogit/packages.git/commit/trunk?h=packages/pyqt5&id=bd544723e6262bc978d4a7680eedeef90186dc41
  # In this commit SIP modules of PyQt5 are moved. Need a proper way to find
  # out the path and upstream it.
  patch -Np1 -i ../pyqt5-path.diff
}

build() {
  mkdir -p build
  cd build
  cmake "$srcdir/$_pkgname" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DQTERMWIDGET_BUILD_PYTHON_BINDING=ON
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir" install
  install -Dm644 "$srcdir/$_pkgname/README.md" -t "$pkgdir"/usr/share/licenses/$pkgname
}
