# Maintainer: Michael Schubert <mschu.dev at gmail>
pkgname=python-llvmlite
pkgver=0.22.0
pkgrel=1
pkgdesc="Lightweight LLVM python binding for writing JIT compilers"
url="https://github.com/numba/llvmlite"
arch=('i686' 'x86_64')
license=('BSD')
depends=('python' 'llvm>=5.0.0' 'llvm<5.1.0')
makedepends=('cython')
source=("https://github.com/numba/llvmlite/archive/v$pkgver.tar.gz")
md5sums=('c5641a032d87bfdea113060e20bf2513')

build() {
  cd "$srcdir/llvmlite-$pkgver"
  python setup.py build
}

package() {
  cd "$srcdir/llvmlite-$pkgver"
  python setup.py install --skip-build --prefix=/usr --root="$pkgdir" --optimize=1

  pydir=$(python -c "from distutils.sysconfig import get_python_lib; \
    print(get_python_lib())")
  install -m755 "$srcdir"/llvmlite-$pkgver/ffi/libllvmlite.so \
    "$pkgdir/$pydir"/llvmlite/binding
}
