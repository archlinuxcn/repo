# Maintainer: Claudia Pellegrino <aur ät cpellegrino.de>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: Douglas Soares de Andrade <dsa@aur.archlinux.org>
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>

pkgname=python-numpy1
pkgver=1.26.4
pkgrel=5
pkgdesc="Scientific tools for Python"
arch=('x86_64')
license=('LicenseRef-custom')
url="https://www.numpy.org/"
depends=('cblas' 'lapack' 'python')
optdepends=('blas-openblas: faster linear algebra')
makedepends=('python-build' 'python-installer' 'meson-python' 'cmake' 'gcc-fortran' 'cython')
checkdepends=('python-pytest' 'python-hypothesis' 'python-setuptools')
provides=("python-numpy=$pkgver")
conflicts=('python-numpy')
source=("https://github.com/numpy/numpy/releases/download/v$pkgver/numpy-$pkgver.tar.gz"
        'github-pr-26364.patch'
        'tests-skipif-python-3.13.patch')
sha512sums=('f7121ab4099fa0686f9c095d456baa4a5869d651d7b7a06385f885f329cf08f11024b5df5e7b4ee705970062a8102ec4f709512eabbfd5c9fccce4ef83b9c208'
            'ee5b380c3530b7a466433c899bff084ff27c8eb5c18aee6638a069867ffc8d8fe4b4c3ccb98800284867f975edb9755c2fd4b21ffe723956fc0117957d52ef7b'
            'a5d850792fc26540735a44df6defffa814b2163a59420a72746e3ca6e9588cdd837bf4f7e4a37cbd13eb3d502808e16f5e61956066051ce0175dad1948ee2999')

prepare() {
  cd numpy-$pkgver

  # Unpin the build system requirement to meson-python, so this package
  # can be compatible to extra/meson-python, which is already on 0.16.0.
  # The pin was never relevant for Linux anyway, as the reason upstream
  # originally added the pin was to shotgun-debug a macOS build issue [1].
  # [1]: https://github.com/numpy/numpy/pull/26365/files#r1586347845
  sed -i -e 's/\(meson-python\)>[^"]*/\1/' pyproject.toml

  # Backport GitHub PR [2] for Python 3.13 compatibility
  # [2]: https://github.com/numpy/numpy/pull/26364
  patch -p1 < ../github-pr-26364.patch

  # Patch out tests that fail due to gh-81283 [3] on Python 3.13
  # [3]: https://github.com/python/cpython/issues/81283
  patch -p1 < ../tests-skipif-python-3.13.patch
}

build() {
  cd numpy-$pkgver
  CFLAGS+=" -ffat-lto-objects" \
  CXXFLAGS+=" -ffat-lto-objects" \
  python -m build --wheel --no-isolation \
    -Csetup-args="-Dblas=cblas" \
    -Csetup-args="-Dlapack=lapack"
}

check() {
  local site_packages
  site_packages=$(python -c "import site; print(site.getsitepackages()[0])")

  cd numpy-$pkgver
  python -m installer --destdir="$PWD/tmp_install" dist/*.whl
  cd "$PWD/tmp_install"
  PATH="$PWD/usr/bin:$PATH" PYTHONPATH="$PWD/$site_packages:$PYTHONPATH" \
    python -c 'import sys; import numpy; sys.exit(not numpy.test())'
}

package() {
  cd numpy-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -D -m644 LICENSE.txt -t "$pkgdir"/usr/share/licenses/python-numpy1/
}
