# Maintainer: Dobroslaw Kijowski [dobo] <dobo90_at_gmail.com>

pkgname=lief
pkgver=0.10.1
pkgrel=2
pkgdesc='Library to instrument executable formats'
arch=(x86_64)
url='https://lief.quarkslab.com/'
license=(APACHE)
depends=(python)
makedepends=(git cmake python-setuptools)
source=("git+https://github.com/lief-project/LIEF#tag=${pkgver}")
md5sums=(SKIP)

build() {
  cd "${srcdir}/LIEF"
  mkdir build

  cmake . -B build -DCMAKE_BUILD_TYPE=Release
  make -C build
  python setup.py build --build-temp=build
}

package() {
  cd "${srcdir}/LIEF"

  make -C build DESTDIR="${pkgdir}" install
  python setup.py install --optimize=1 --root="${pkgdir}" --skip-build
}
