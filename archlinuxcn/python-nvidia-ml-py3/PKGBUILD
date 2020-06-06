# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-nvidia-ml-py3
_name=nvidia-ml-py3
pkgver=7.352.0
pkgrel=2
pkgdesc='Python Bindings for the NVIDIA Management Library'
arch=('any')
url='https://github.com/nicolargo/nvidia-ml-py3'
license=('BSD')
depends=(
  cuda
)
makedepends=(
  python-setuptools
)
source=(
  "${_name}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
  "LICENSE::https://github.com/nicolargo/nvidia-ml-py3/raw/master/README.txt"  
)
sha512sums=('ade63f279e74338a4b6a529071e677b12dab7420ce8df96804c4fae9f529bab26239be311f32c7e4aeaa54c6dd7d7d855af16c7d20496c361dc83913bf99f430'
            'cfce62036b67b31a118154aa92ad664a914fada56805222fcc371a97264dc6ac791e0447a2f2848244c2d76c9d3038e5ceb10ddf283bd353c9d82319696872c1')

build() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_name}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
