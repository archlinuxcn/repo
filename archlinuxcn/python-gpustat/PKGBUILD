# Maintainer: Hu Butui <hot123tea123@gmail.com>
# Contributor: Grey Christoforo <first name [at] last name [dot] net>

pkgname=python-gpustat
_pkgname=gpustat
pkgver=1.0.0
pkgrel=1
pkgdesc='A simple command-line utility for querying and monitoring GPU status'
arch=('any')
url='https://github.com/wookayin/gpustat'
license=('MIT')
depends=(
  nvidia-utils
  python-blessings
  python-nvidia-ml-py3
  python-psutil
  python-six
)
makedepends=(
  python-pip
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/wookayin/${_pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('d40e2c7f42caa83162b600a7e032165202b4ab9cb64c38f22b684221009b3179')

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
