# Maintainer: Martin Diehl <aur@martin-diehl.net>
# Contributor: Achmad Fathoni<fathoni.id(at)gmail.com>

pkgname=python-types-pyyaml
pkgver=6.0.12.20250915
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
sha512sums=('0c4354814f53d044b58063f010a370f5b1fa503e21e4b431eb4af4554d9f9b9a404c6a91a476383434d12d1ebf741b5fcc0738db568f15a9a563cf91b1bd856c')

build() {
    cd ${__name}-${pkgver}
    python -m build --wheel --no-isolation
}

package() {
    cd ${__name}-${pkgver}
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
