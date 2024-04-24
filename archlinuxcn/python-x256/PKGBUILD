# Maintainer: Mark Wagie <mark dot wagie at proton dot me>
pkgname=python-x256
_name=${pkgname#python-}
pkgver=0.0.3
pkgrel=1
pkgdesc="Find the nearest xterm 256 color index for an RGB."
arch=('any')
url="https://github.com/magarcia/python-x256"
license=('MIT')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-setuptools' 'python-wheel')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/$_name/$_name-$pkgver.tar.gz"
        "https://github.com/magarcia/python-x256/raw/main/LICENSE")
sha256sums=('f855dbccd91e53f5890283d8203855743827e7eed595d5cf19544ba3d212e001'
            'd4024ec3d57d5c02bb53e89ddeb92b72e8c26b5593acd0573b8993d224c39dba')

build() {
  cd "$_name-$pkgver"
  python -m build --wheel --no-isolation
}

package() {
  cd "$_name-$pkgver"
  python -m installer --destdir="$pkgdir" dist/*.whl

  install -Dm644 "$srcdir/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname/"
}
