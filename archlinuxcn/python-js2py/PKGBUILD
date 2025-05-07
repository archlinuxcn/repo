# Maintainer:

: ${_commit:=2e017b86e2f18a6c8a842293b1687f2ce7baa12e} # 0.74

pkgname=python-js2py
pkgver=0.74
pkgrel=3
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
  "0001-js2py-pr293-opt-tzlocal.patch"
  "0002-js2py-pr299-uint32.patch"
  "0003-js2py-pr320-math-sign.patch"
  "0004-js2py-pr323-cve-2024-28397.patch"
  "0005-js2py-pr327-python3.12.patch"
  "0006-js2py-pr336-escape-unescape.patch"

  # https://github.com/a-j-albert/Js2Py/compare/0da30c83f149b15539ca3d246d5ebfb0afd7f140~1..cc64a715727f110b79310b8031e0ade9c501d5d3.diff
  "0007-js2py-xxxxx-python3.13.patch"
)
sha256sums=(
  'b362565354ffbcf4f4cc40fde179aa2abde7804572e2e4621416b21b686ca6b6'
  'ff357bb24e7ad1b278fb39e7605054df815d2f589e55bf745e4262de84aa0839'
  '98dc1e9e9579ee0371532ff530d1d72acd5ee708e21449b28c16f57ed39dab8d'
  'a3865702a81dbecac7841f4fcea7fc301d92159e068983e9383a98041ca6e04c'
  '7eb3378faf111308021734b67d670c3fd633b7e6b9901f5aaec40e949ae76217'
  '710213cea46804a949db7d655a539939d014fa9e34ae3e4c0358678cd14e6893'
  'c87cf6fe1a405081b7b0f10957156a6ca1e80863f78f1179e21953ffe7a704fe'
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
