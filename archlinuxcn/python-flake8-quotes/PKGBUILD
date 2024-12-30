# Maintainer: Dmytro Meleshko <qzlgeb.zryrfuxb@tznvy.pbz(rot13)>
# Contributor: acxz <akashpatel2008@yahoo.com>

pkgname=python-flake8-quotes
_pkgname=flake8-quotes
pkgver=3.3.2
pkgrel=4
pkgdesc="Flake8 lint for quotes"
arch=('any')
url="https://github.com/zheller/${_pkgname}"
license=('MIT')
depends=('flake8')
checkdepends=('python-pytest')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/zheller/${_pkgname}/archive/${pkgver}.tar.gz")
sha256sums=('884d027b6126b6216bdb9fa95a9841c4f07f600569a4a41f3d0cdbf71afe6bcb')

build() {
    cd "${_pkgname}-${pkgver}"
    python -m build --wheel --no-isolation
}

check() {
    cd "${_pkgname}-${pkgver}"
    python -m pytest -k 'not test_stdin'
}

package() {
    cd "${_pkgname}-${pkgver}"
    python -m installer --destdir="${pkgdir}" dist/*.whl

    install -Dm 644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
