# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
_base=sentence-transformers
pkgname=python-${_base}
pkgver=5.4.0
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
sha512sums=('c9bdc7ef1c10317b7d50f9510b06589f06c84174e8110825624ada9081829a2c53898c5926aa7e57fccab7cc63c85f6d628d2ee3da787235d135c782294581b2')

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
