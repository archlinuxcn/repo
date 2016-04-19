# Maintainer: fclad <fcladera at fcladera.com>

_pkgname=plotly.py
pkgname=python-plotly
pkgver=1.6.12.r715.g20102d6
pkgrel=1
pkgdesc="An interactive, browser-based charting library for python"
arch=('i686' 'x86_64')
url="https://plot.ly/python/"
license=('MIT')
depends=('python-requests' 'python-pytz')
makedepends=('git' 'python')
source=("git+https://github.com/plotly/plotly.py.git")
md5sums=('SKIP')

pkgver() {
    cd "$srcdir/$_pkgname"
    git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cd "$srcdir/$_pkgname"

  #[ -d build ] && rm -rf build
  #mkdir build
  #cd build

  #python config.py -auto
  python setup.py build
}

package() {
  cd "$srcdir/$_pkgname"
  python setup.py install --root="${pkgdir}" --prefix=/usr
}
