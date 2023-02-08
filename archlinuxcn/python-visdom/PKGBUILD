# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-visdom
_name=${pkgname#python-}
pkgver=0.2.4
pkgrel=1
pkgdesc='A flexible tool for creating, organizing, and sharing visualizations of live, rich data. Supports Torch and Numpy.'
arch=(any)
url=https://github.com/facebookresearch/visdom
license=(CC-BY-NC-4.0)
depends=(
  python-jsonpatch
  python-numpy 
  python-pytorch 
  python-pyzmq 
  python-six 
  python-scipy 
  python-torchfile
  python-tornado 
  python-tqdm
  python-websocket-client
)
makedepends=(python-setuptools)
source=(
  "${pkgname}-${pkgver}.tar.gz"::"https://files.pythonhosted.org/packages/source/${_name::1}/${_name}/${_name}-${pkgver}.tar.gz"
  "LICENSE"::"https://github.com/facebookresearch/visdom/raw/master/LICENSE"
)
sha512sums=('007aa1c70f3335fec3c811a9492e85610c75b79e9295a8d5eb4539fcb75b3ea00bd453adf7404113644bfc431f77223f7d524c6c6c07b970366fb3523a1b83b9'
            '31cc38066678c030e8f6378dcae59add64566a977f92983c3a4c929c9b76424291915ea4283e1367ece50b9537f8d51970aa8fd5ce063037aa3a7c45f0677d25')

build() {
  cd "${_name}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_name}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
