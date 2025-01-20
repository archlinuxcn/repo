# Maintainer: Gesh <gesh@gesh.uni.cx>

pkgname='python-types-pygments'
pkgver='2.19.0.20250107'
_name=${pkgname#python-}
_name="${_name//-/_}"
_src_folder="${_name}-${pkgver}"
pkgrel=1
pkgdesc='Typing stubs for Pygments'
url="https://github.com/python/typeshed"
depends=('python')
makedepends=(
    'python-build' 'python-installer' 'python-wheel' 'python-setuptools'
)
license=('Apache-2.0')
arch=('any')
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz")
sha256sums=('94de72c7f09b956c518f566e056812c698272a7a03a9cd81f0065576c6bd3219')

build() {
    cd "${srcdir}/${_src_folder}"
    python -m build --wheel --no-isolation
}

package() {

    cd "${srcdir}/${_src_folder}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
