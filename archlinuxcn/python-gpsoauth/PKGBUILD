# Maintainer: robertfoster

pkgbase=python-gpsoauth
pkgname=python-gpsoauth
_module='gpsoauth'
pkgver='0.4.2rc.2'
_ver="0.4.2-rc.2"
pkgrel=1
pkgdesc="A python client library for Google Play Services OAuth."
url="https://github.com/simon-weber/gpsoauth"
depends=('python' 'python-requests' 'python-pycryptodomex')
makedepends=('python-setuptools')
license=('MIT')
arch=('any')
source=("https://github.com/simon-weber/gpsoauth/archive/${_ver}.tar.gz")

build() {
    cd "${srcdir}/${_module}-${_ver}"
    python setup.py build
}

package() {
    cd "${srcdir}/${_module}-${_ver}"
    python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}

md5sums=('a4313519ef32e8e0ac708fa870f379fc')

