# Maintainer: Gesh <gesh@gesh.uni.cx>

pkgname='python-types-beautifulsoup4'
pkgver=4.12.0.20250204
_name=${pkgname#python-}
_name="${_name//-/_}"
_src_folder="${_name}-${pkgver}"
pkgrel=3
pkgdesc="Typing stubs for beautifulsoup4"
url="https://github.com/python/typeshed"
depends=('python')
makedepends=(
    'python-build' 'python-installer' 'python-setuptools'
)
license=('Apache-2.0')
arch=('any')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('f083d8edcbd01279f8c3995b56cfff2d01f1bb894c3b502ba118d36fbbc495bf')

build() {
    cd "${srcdir}/${_src_folder}"
    python -m build --wheel --no-isolation
}

package() {

    cd "${srcdir}/${_src_folder}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
