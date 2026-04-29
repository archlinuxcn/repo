# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Achmad Fathoni<fathoni.id(at)gmail.com>

pkgname=python-types-pyyaml
pkgver=6.0.12.20260408
pkgrel=1
pkgdesc='Typing stubs for PyYAML'
arch=(any)
url='https://pypi.org/project/types-PyYAML'
license=('Apache-2.0')
depends=('python')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
_name=${pkgname#python-}
__name=${_name//-/_}
source=("https://files.pythonhosted.org/packages/source/${_name::1}/${__name}/${__name}-$pkgver.tar.gz")
sha512sums=('e6313b3dd4e0fec52d90f6fd072824d1c5c263a8e603c8bcfaab1aabcc7a4181fb8c7a4db08bb0cd10cf3b60db0576562973f3bff73144e13d71f4784b8f61a9')

build() {
    cd ${__name}-${pkgver}
    python -m build --wheel --no-isolation
}

package() {
    cd ${__name}-${pkgver}
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
