# Maintainer: Antonio Rojas <arojas@archlinux.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Igor Scabini <furester @ gmail.com>

pkgname=cython0
pkgver=0.29.37.1
pkgrel=1
pkgdesc='C-Extensions for Python (legacy version)'
arch=(x86_64)
url='https://cython.org'
license=(APACHE)
depends=(python)
conflicts=(cython)
provides=(cython)
makedepends=(python-build python-installer python-setuptools python-wheel)
source=(https://github.com/cython/cython/archive/$pkgver/$pkgname-$pkgver.tar.gz)
sha256sums=('cbd3949bec315ef1cc974c2907b69af3d36ec35dacc9b1ab258e3e9cf800b157')

build() {
  cd cython-$pkgver
  python -m build --wheel --no-isolation
}

package() {
  cd cython-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl

  for f in cygdb cython cythonize; do
    mv "$pkgdir"/usr/bin/$f "$pkgdir"/usr/bin/${f}3
    ln -s ${f}3 "$pkgdir"/usr/bin/$f
  done
}
