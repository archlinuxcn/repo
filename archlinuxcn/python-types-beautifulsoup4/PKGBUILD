# Maintainer: Gesh <gesh@gesh.uni.cx>

pkgname='python-types-beautifulsoup4'
pkgver='4.12.0.20241020'
_name=${pkgname#python-}
# For some reason, of all typing stub packages I've investigated, pypi leaves
# this one intact
# _name="${_name//-/_}"
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
sha256sums=('158370d08d0cd448bd11b132a50ff5279237a5d4b5837beba074de152a513059')

build() {
    cd "${srcdir}/${_src_folder}"
    python -m build --wheel --no-isolation
}

package() {

    cd "${srcdir}/${_src_folder}"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
