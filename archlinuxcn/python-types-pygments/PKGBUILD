# Maintainer: Gesh <gesh@gesh.uni.cx>

pkgname='python-types-pygments'
_module='types-Pygments'
_src_folder='types-Pygments-2.17.0.20240106'
pkgver='2.17.0.20240106'
pkgrel=1
pkgdesc="Typing stubs for Pygments"
url="https://github.com/python/typeshed"
depends=('python')
makedepends=(
    'python-build' 'python-installer' 'python-wheel' 'python-setuptools'
)
license=('Apache-2.0')
arch=('any')
source=("https://files.pythonhosted.org/packages/b6/5e/6a651aa79d2e9e1153ee468c1f5097bf011d0ba72761e8ae5eb262b771b3/types-Pygments-2.17.0.20240106.tar.gz")
sha256sums=('92e62ac37793e567cd2b0f64f1456c24fccce4041d9c5f869697a6739fde4fce')

build() {
    cd "${srcdir}/${_src_folder}"
    python -m build --wheel --no-isolation
}

package() {

    cd "${srcdir}/${_src_folder}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
