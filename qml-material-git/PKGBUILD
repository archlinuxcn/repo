# Maintainer: Riley Trautman <asonix.dev@gmail.com>
# Contributor: Michael Spencer <sonrisesoftware@gmail.com>

_pkgname=qml-material
pkgname=$_pkgname-git
pkgver=0.2.0.r0.g803035d
pkgrel=1
pkgdesc="A UI framework for QtQuick implementing Material Design"
arch=("i686" "x86_64")
url="https://github.com/papyros/qml-material"
license=("LGPL")
depends=("qt5-base" "qt5-declarative" "qt5-quickcontrols" "qt5-svg"
"qt5-graphicaleffects")
makedepends=("git")
provides=("$_pkgname")
conflicts=("$_pkgname")
source=("$_pkgname::git+https://github.com/papyros/qml-material.git#branch=develop")
sha256sums=("SKIP")

pkgver() {
  cd "$_pkgname"
  # cutting off 'foo-' prefix that presents in the git tag
  git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  mkdir -p build
}

build() {
  cd build
  qmake "$srcdir/$_pkgname"
  make
}

package() {
  cd build
  make INSTALL_ROOT="$pkgdir" install
}

# Additional functions to generate a changelog

changelog() {
  cd "$_pkgname"
  git log $1..HEAD --no-merges --format=" * %s"
}

gitref() {
  cd "$_pkgname"
  git rev-parse HEAD
}
