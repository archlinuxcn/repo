# Maintainer: Roald Clark <roaldclark@gmail.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=python-dict2xml
_pkgname=${pkgname#python-}
pkgver=1.7.6
pkgrel=3
pkgdesc="Small utility to convert a python dictionary into an XML string"
arch=('any')
url="https://github.com/delfick/${pkgname}"
license=('MIT')
depends=('python')
makedepends=(
    'python-build'
    'python-hatchling'
    'python-installer'
)
checkdepends=(
    'python-noseofyeti'
    'python-pytest'
)
source=("https://files.pythonhosted.org/packages/source/${_pkgname:0:1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz")
sha256sums=('3e4811f4ef7fca86dede6acf382268ff9bc5735a4aa0e21b465f6eb0c4e81732')
b2sums=('86ed48b2dc857efd58294c23f0708102ac66dab50e7f50ae149185f3fb707f72ef67008921ea641ed1bd96a91b25b39a92ddc796eadb64560ff29b82cd1ef07e')

build() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

check() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    pytest -v
}

package() {
    cd "${srcdir}/${_pkgname}-${pkgver}"
    install -Dm0644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"
    python -m installer --destdir="${pkgdir}" dist/*.whl
}
