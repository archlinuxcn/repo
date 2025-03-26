# Maintainer: Patrick Northon <northon_patrick3@yahoo.ca>
# Contributor: Antonio Rojas <arojas@archlinux.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Igor Scabini <furester @ gmail.com>

pkgname=cython0
pkgver=0.29.37.1
pkgrel=3
pkgdesc='C-Extensions for Python (legacy version)'
arch=(x86_64)
url='https://cython.org'
license=(Apache-2.0)
depends=(python)
conflicts=(cython)
makedepends=(python python-build python-installer python-setuptools python-wheel)
source=(
  "https://github.com/cython/cython/archive/$pkgver/$pkgname-$pkgver.tar.gz"
  'cython0-python313.patch')
sha256sums=('cbd3949bec315ef1cc974c2907b69af3d36ec35dacc9b1ab258e3e9cf800b157'
            '99076be2e645bc1921899cf93a56cf5877d19a95429e456a142628af4de48eaf')

prepare() {
  cd cython-$pkgver
  patch -p1 -i '../cython0-python313.patch'
}

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
