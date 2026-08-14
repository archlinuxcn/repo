# Maintainer: Groctel <aur@taxorubio.com>
# shellcheck disable=SC2034,SC2154,SC2164

_name=condense_json

pkgname=python-condense-json
pkgver=1.1
pkgrel=1
pkgdesc="Python function for condensing JSON using replacement strings"

arch=("x86_64")
license=("Apache-2.0")
url='https://pypi.org/project/condense-json/'

source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name//-/_}/${_name//-/_}-$pkgver.tar.gz")
sha256sums=('c455b54bbbab89a69f598b09f2003a89b738df20d30e6aa341c495401ec5b349')

depends=()
makedepends=(
  "python-build"
  "python-installer"
  "python-setuptools"
  "python-wheel"
)
checkdepends=(
    "python-hypothesis"
    "python-pytest"
)

build () {
    cd "$srcdir/$_name-$pkgver" || exit
    python -m build --wheel --no-isolation
}

check () {
    cd "$srcdir/$_name-$pkgver"
    PYTHONPATH=$PYTHONPATH:. pytest
}

package() {
    cd "$srcdir/$_name-$pkgver" || exit
    python -m installer --destdir="$pkgdir" dist/*.whl
    install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
