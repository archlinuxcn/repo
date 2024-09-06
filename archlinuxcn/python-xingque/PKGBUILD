# Maintainer: weilinfox <sakurakaze.fox at gmail.com>

_pkgname=xingque
pkgname=python-xingque
pkgver=0.2.1
pkgrel=1
pkgdesc="Yet another Python binding to starlark-rust, exposing the Starlark language to your Python projects."
arch=('aarch64' 'armv7h' 'loong64' 'riscv64' 'x86_64' 'x86_64_v3')
url="https://github.com/xen0n/xingque"
license=(Apache-2.0)
depends=(
	'gcc-libs'
	'glibc'
	'python>=3.8'
)
makedepends=(
	'maturin>=1.6'
	'python-installer'
)
checkdepends=('python-pytest')
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/xen0n/xingque/archive/${pkgver}.tar.gz")
sha512sums=('be0d49d29d6fbc704e9877c20980eae079927df60b6f32a3cf57f359d5b8d33e9c8cd1c4ea06efa76f91ad307c3311e9e018a808438856b7f6550119193f12dd')

build() {
  cd "$_pkgname-$pkgver"

  maturin build --release --strip
}

check() {
  cd "$_pkgname-$pkgver"

  pyver=$(python -c "import sys; print('{}.{}'.format(*sys.version_info[:2]))")
  python -m installer --destdir="$PWD/tmp_install" target/wheels/*.whl
  PYTHONPATH="$PWD/tmp_install/usr/lib/python$pyver/site-packages" python -m pytest -v
}

package() {
  cd "$_pkgname-$pkgver"

  python -m installer --destdir="$pkgdir" target/wheels/*.whl

  install -Dm644 {CHANGELOG,README}.md -t "${pkgdir}/usr/share/doc/${pkgname}/"
  install -Dm644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
