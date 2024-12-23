# Maintainer:  JP-Ellis <josh@jpellis.me>
pkgname='python-habanero'
_module='habanero'
_src_folder='habanero-1.2.6'
pkgver='1.2.6'
pkgrel=4
pkgdesc="A low level client for Crossref's Search API"
url="https://github.com/sckott/habanero"
depends=(
  'python'
  'python-requests'
  'python-tqdm'
)
makedepends=(
  'python-build'
  'python-installer'
  'python-wheel'
  'python-setuptools'
  'python-setuptools-scm'
)
optdepends=(
  'python-bibtexparser: attempt to fix misformatted bibtex'
)
license=('LicenseRef-MIT')
arch=('any')
source=("https://files.pythonhosted.org/packages/3d/17/885ee33738a7ecb29d487ca42043378804d0c47945d24ee040cfaa35beeb/habanero-1.2.6.tar.gz")
sha256sums=('b206d49f44f41c2289f0ad731f259a50d4376c747d8ecbb219a73874d45309d4')

build() {
    cd "${srcdir}/${_src_folder}"
    python -m build --wheel --no-isolation
}

package() {
    cd "${srcdir}/${_src_folder}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
    install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/"${pkgname}"/LICENSE
}

# vim:set ts=2 sw=2 et:
