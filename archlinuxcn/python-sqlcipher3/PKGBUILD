# Maintainer: Chih-Hsuan Yen <base64_decode("eXUzYWN0eHQydHR0ZmlteEBjaHllbi5jYwo=")>

pkgname=python-sqlcipher3
pkgver=0.5.4
pkgrel=1
pkgdesc='Python 3 bindings for SQLCipher'
arch=(x86_64)
url='https://github.com/coleifer/sqlcipher3'
# https://github.com/coleifer/sqlcipher3/blob/0.5.2/setup.py#L154 says zlib/libpng, while texts in
# https://github.com/coleifer/sqlcipher3/blob/0.5.2/LICENSE looks more like zlib
# https://spdx.org/licenses/Zlib.html
license=('Zlib')
depends=(python glibc sqlcipher)
makedepends=(python-build python-installer python-setuptools python-wheel)
checkdepends=(python-pytest)
source=("https://github.com/coleifer/sqlcipher3/archive/refs/tags/$pkgver/$pkgname-$pkgver.zip")
sha256sums=('245619d456f65bc3f4ad9967ae72d0ad48fed69a1f511b9cf084ebfd46a41eb1')

build() {
  cd sqlcipher3-$pkgver
  python -m build --wheel --no-isolation
}

check() {
  cd sqlcipher3-$pkgver

  pyver=$(python -c "import sys; print('{}{}'.format(*sys.version_info[:2]))")
  # see https://github.com/coleifer/sqlcipher3/blob/0.5.3/.github/workflows/tests.yaml#L24
  PYTHONPATH="$PWD/build/lib.linux-$CARCH-cpython-$pyver:$PWD" python tests/
}

package() {
  cd sqlcipher3-$pkgver
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -D -m644 LICENSE -t "$pkgdir"/usr/share/licenses/$pkgname
}
