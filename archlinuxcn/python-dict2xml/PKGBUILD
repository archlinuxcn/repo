# Maintainer: Roald Clark <roaldclark@gmail.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=python-dict2xml
_pkgname=${pkgname#python-}
pkgver=1.7.7
pkgrel=1
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
sha256sums=('ae47873a584921430d3b74f0f63db98b59f6cafc038b14619c65e83cf717608f')
b2sums=('9956e30eaa379209320f3e155549788dbe9cd156167dfec175a9a8e38d161fa2b5492508fb23861896dd716edb2f5bd98895f63e12e06f9c99eca09bfc01bd31')

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
