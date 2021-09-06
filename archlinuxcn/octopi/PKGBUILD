# Maintainer: MatMoul <matmoul@gmail.com>

_pkggit=octopi
_gitcommit=5b8dfb0388aeb471bb4ab5652a651ec1345a1ed5
_gitsha256='4c34bfb33e733dd23d42a13a3814d64c7c25de41ce01680a456514a471520729'

pkgbase=octopi
pkgname='octopi'
pkgver=0.11.0
pkgrel=2
pkgdesc="This is Octopi, a powerful Pacman frontend using Qt libs"
arch=('i686' 'x86_64')
url="https://tintaescura.com/projects/octopi/"
license=('GPL2')
depends=('alpm_octopi_utils' 'pkgfile' 'qtermwidget' 'sudo')
makedepends=('qt5-tools')
optdepends=('octopi-notifier-qt5: Notifier for Octopi using Qt5 libs'
            'octopi-notifier-frameworks: Notifier for Octopi with Knotifications support'
            'pacaur: for AUR support'
            'pikaur: for AUR support'
            'trizen: for AUR support'
            'yay: for AUR support'
            'pacmanlogviewer: to view pacman log files')
provides=('octopi' 'octopi-repoeditor' 'octopi-cachecleaner')
conflicts=('octopi')
source=("octopi-${pkgver}-${pkgrel}.tar.gz::https://github.com/aarnt/octopi/archive/${_gitcommit}.tar.gz")
sha256sums=(${_gitsha256})

_subdirs=(helper repoeditor cachecleaner sudo)

prepare() {
  cd "${srcdir}/${_pkggit}-${_gitcommit}"
  cp resources/images/octopi_green.png resources/images/octopi.png
}

build() {
  cd "${srcdir}/${_pkggit}-${_gitcommit}"

  echo "Starting build..."
  qmake-qt5 PREFIX=/usr QMAKE_CFLAGS="${CFLAGS}" QMAKE_CXXFLAGS="${CXXFLAGS}" QMAKE_LFLAGS="${LDFLAGS}" octopi.pro
  make

  for _subdir in ${_subdirs[@]}; do
    pushd $_subdir
    echo "Building octopi-$_subdir..."
    qmake-qt5 PREFIX=/usr QMAKE_CFLAGS="${CFLAGS}" QMAKE_CXXFLAGS="${CXXFLAGS}" QMAKE_LFLAGS="${LDFLAGS}" "octopi-$_subdir.pro"
    make
    popd
  done
}

package() {
  cd "${srcdir}/${_pkggit}-${_gitcommit}"
  
  make INSTALL_ROOT="${pkgdir}" install
  
  for _subdir in ${_subdirs[@]}; do
    pushd $_subdir
    make INSTALL_ROOT="${pkgdir}" install
    popd
  done
}
