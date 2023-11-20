# Maintainer: Evgenii Alekseev
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Manuel Schneider  <manuelschneid3r at googles mail>

pkgname=albert
pkgver=0.22.16
pkgrel=1
pkgdesc="A sophisticated standalone keyboard launcher"
arch=('x86_64')
url="https://github.com/albertlauncher"
license=('GPL')
depends=('hicolor-icon-theme' 'qt6-5compat' 'qt6-declarative' 'qt6-scxml' 'qt6-shadertools' 'qt6-svg')
makedepends=('cmake' 'git' 'libqalculate' 'pybind11' 'python')
optdepends=('ddgr: duckduckgo search plugin'
            'libarchive: documentation plugin'
            'libqalculate: calculator plugin'
            'python: python extension'
            'python-docker: docker plugin'
            'python-googletrans: google translate plugin'
            'python-pylatexenc: TeX plugin'
            'python-urllib3: python web plugins'
            'python-virtualbox: virtualbox plugin')
source=("https://github.com/albertlauncher/albert/releases/download/v${pkgver}/v${pkgver}.tar.gz")

build() {
  mkdir -p build
  cd build

  cmake ../$pkgname \
    -DCMAKE_BUILD_TYPE=MinSizeRel \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_LIBDIR=lib \
    -DCMAKE_FIND_PACKAGE_RESOLVE_SYMLINKS=ON \
    -DQHOTKEY_INSTALL=OFF \
    -DBUILD_APPLICATIONS_XDG=ON \
    -DBUILD_CALCULATOR_QALCULATE=ON \
    -DBUILD_CHROMIUM=ON \
    -DBUILD_CLIPBOARD=ON \
    -DBUILD_DATETIME=ON \
    -DBUILD_DEBUG=OFF \
    -DBUILD_FILES=ON \
    -DBUILD_HASH=ON \
    -DBUILD_PYTHON=ON \
    -DBUILD_QMLBOXMODEL=ON \
    -DBUILD_SNIPPETS=ON \
    -DBUILD_SSH=ON \
    -DBUILD_SYSTEM=ON \
    -DBUILD_TEMPLATE=OFF \
    -DBUILD_TERMINAL=ON \
    -DBUILD_URLHANDLER=ON \
    -DBUILD_WEBSEARCH=ON \
    -DBUILD_WIDGETSBOXMODEL=ON

  make
}


package() {
  cd build

  make DESTDIR="$pkgdir/" install
}

sha512sums=('25dba1482b6113dd08bb03b59a3687c2d18e604008f29f0e435633fe50564e388cb76008e42818155f9cdc7b340ace0a9ba00fc0a821bb6be233e07e4727a9e3')
