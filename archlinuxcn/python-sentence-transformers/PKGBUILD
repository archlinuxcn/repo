# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=sentence-transformers
pkgname=python-${_base}
pkgver=5.1.2
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
sha512sums=('0f47ed6371be5723a8b5f0325bed150ff6b8ac90df966792a0eb048b4c43fce150f03a2f04862559d6101329864137c7be3c29731bbd1a3116cd43f828cb1fae')

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
