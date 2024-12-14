# Maintainer: Gesh <gesh@gesh.uni.cx>

pkgname='python-types-beautifulsoup4'
_module='types-beautifulsoup4'
_src_folder='types-beautifulsoup4-4.12.0.20240106'
pkgver='4.12.0.20240106'
pkgrel=1
pkgdesc="Typing stubs for beautifulsoup4"
url="https://github.com/python/typeshed"
depends=('python')
makedepends=(
    'python-build' 'python-installer' 'python-wheel' 'python-setuptools'
)
license=('Apache-2.0')
arch=('any')
source=("https://files.pythonhosted.org/packages/43/b4/53d66eb8f6f358f6e5bd0c8bd373844b53b77fdb508d8f0d8000fbefa0a2/types-beautifulsoup4-4.12.0.20240106.tar.gz")
sha256sums=('98d628985b71b140bd3bc22a8cb0ab603c2f2d08f20d37925965eb4a21739be8')

build() {
    cd "${srcdir}/${_src_folder}"
    python -m build --wheel --no-isolation
}

package() {

    cd "${srcdir}/${_src_folder}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
