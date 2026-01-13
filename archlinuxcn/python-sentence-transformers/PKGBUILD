# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=sentence-transformers
pkgname=python-${_base}
pkgver=5.2.0
pkgrel=1
pkgdesc="Embeddings, Retrieval, and Reranking"
arch=(any)
url="https://github.com/UKPLab/${_base}"
license=(Apache-2.0)
depends=(python-transformers python-tqdm python-pytorch python-scikit-learn
  python-scipy python-huggingface-hub python-pillow python-typing_extensions)
makedepends=(python-build python-installer python-setuptools python-wheel)
# checkdepends=(python-pytest)
source=(${_base}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz)
sha512sums=('a276d5edda2ec526eae1fe54f3ae15770e77449bc95b6becfb211d432c327ef922dc6496f68984c25c1800ba3118037ff2e51588232336cc23a654160c875002')

build() {
  cd ${_base}-${pkgver}
  python -m build --wheel --skip-dependency-check --no-isolation
}

# check() {
#   cd ${_base}-${pkgver}
#   python -m venv --system-site-packages test-env
#   test-env/bin/python -m installer dist/*.whl
#   test-env/bin/python -m pytest tests
# }

package() {
  cd ${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
