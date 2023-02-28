# Maintainer: jzbor <zborof at posteo dot de>
pkgname=python-accelerate
_name=${pkgname#python-}
pkgver=0.16.0
pkgrel=2
pkgdesc="Train and use PyTorch models with multi-GPU, TPU, mixed-precision"
arch=(any)
url="https://github.com/huggingface/$_name"
license=('MIT')
groups=()
depends=(python)
makedepends=(python-build python-installer python-wheel python-setuptools)
# checkdepends=(
#   "python-pytest"
#   "python-datasets"
#   "python-evaluate"
#   "python-transformers"
#   "python-scipy"
#   "python-scikit-learn"
#   "python-deepspeed"
#   "python-tqdm"
# )
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
noextract=()
sha512sums=('55486e4e74b4aeee725539aefdacf067cf4584d726a57fcedaeba683f771f7dd33201f754b8d5df8eabc1ebbd360b48a0749f0911938094cd85edf9c4d349c9a')
validpgpkeys=()

build() {
    cd "$_name-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$_name-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

# check() {
#     cd "$_name-$pkgver"
#     pytest tests
# }
