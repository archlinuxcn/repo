# Maintainer:

: ${_commit:=2e017b86e2f18a6c8a842293b1687f2ce7baa12e} # 0.74

pkgname=python-js2py
pkgver=0.74
pkgrel=2
pkgdesc="JavaScript to Python Translator & JavaScript interpreter written in 100% pure Python"
url="https://github.com/PiotrDabkowski/Js2Py"
license=('MIT')
arch=('any')

depends=(
  'python'
  'python-pyjsparser'
  'python-six'
)
makedepends=(
  'git'
  'python-build'
  'python-installer'
  'python-setuptools'
  'python-tzlocal'
  'python-wheel'
)
checkdepends=(
  'npm'
  'python-numpy'
)
optdepends=(
  'python-tzlocal: for local timezone support'
)

_pkgsrc="js2py"
source=(
  "$_pkgsrc"::"git+$url.git#commit=$_commit"
  "0001-js2py-pr293-opt-tzlocal.patch"::"$url/pull/293.patch"
  "0002-js2py-pr327-python3.12.patch"::"$url/pull/327.patch"
  "0003-js2py-xxxxx-python3.13.patch"::"https://github.com/a-j-albert/Js2Py/compare/0da30c83f149b15539ca3d246d5ebfb0afd7f140~1..cc64a715727f110b79310b8031e0ade9c501d5d3.diff"
)
sha256sums=(
  'b362565354ffbcf4f4cc40fde179aa2abde7804572e2e4621416b21b686ca6b6'
  'ff357bb24e7ad1b278fb39e7605054df815d2f589e55bf745e4262de84aa0839'
  '710213cea46804a949db7d655a539939d014fa9e34ae3e4c0358678cd14e6893'
  '8f7a2c7d93aa6c19a09b4eb1f38a494c483eac144c92c5cbfde13e8dcf8d86da'
)

prepare() {
  cd "$_pkgsrc"
  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    src="${src%.zst}"
    if [[ $src == *.patch ]]; then
      printf '\nApplying patch: %s\n' "$src"
      patch -Np1 -F100 -i "${srcdir:?}/$src"
    fi
  done
}

build() {
  cd "$_pkgsrc"
  python -m build --wheel --no-isolation --skip-dependency-check
}

check() {
  cd "$_pkgsrc"
  python simple_test.py
}

package() {
  cd "$_pkgsrc"
  python -m installer --destdir="$pkgdir" dist/*.whl
  install -Dm644 LICENSE.md -t "$pkgdir/usr/share/licenses/$pkgname/"
}
