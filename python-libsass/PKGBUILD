# Maintainer: Peter Cai <peter at typeblog.net>

_name=libsass
pkgname=python-libsass
pkgver=0.12.3
pkgrel=1
pkgdesc="A straightforward binding of libsass for Python."
arch=('x86_64')
url="https://pypi.python.org/pypi/libsass/"
license=("MIT")
source=(
  "https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
  "0000-use-system-libsass.patch"
)
md5sums=('b2b0735a975731e1d07804fd4e7251c2'
         'b81c742608baa51b75dc9cf994f0974f')
depends=(
  "libsass"
  "python"
  "python-six"
)
makedepends=(
  "python-setuptools"
  "gcc"
)

build() {
  cd "$srcdir/$_name-$pkgver"
  patch -Np1 -i "$srcdir/0000-use-system-libsass.patch"
  python setup.py build
}

package() {
  cd "$srcdir/$_name-$pkgver"
  python setup.py install --root="$pkgdir/" --optimize=1
}
