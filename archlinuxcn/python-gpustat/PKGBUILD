# Maintainer: Hu Butui <hot123tea123@gmail.com>
# Contributor: Grey Christoforo <first name [at] last name [dot] net>

pkgname=python-gpustat
_pkgname=gpustat
pkgver=1.0
epoch=1
pkgrel=2
pkgdesc='A simple command-line utility for querying and monitoring GPU status'
arch=('any')
url='https://github.com/wookayin/gpustat'
license=('MIT')
depends=(
  nvidia-utils
  python-blessed
  python-nvidia-ml-py
  python-psutil
  python-six
)
makedepends=(
  python-pip
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/wookayin/${_pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('c3eceff760474b0e3feb74c4e1d034167283d62d6f1e0b3813f51a1511be7bde')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}


package(){
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}

# vim:ts=2:sw=2:et:
