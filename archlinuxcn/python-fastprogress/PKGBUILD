# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-fastprogress
_pkgname=fastprogress
pkgver=0.1.22
pkgrel=1
pkgdesc='Simple and flexible progress bar for Jupyter Notebook and console'
arch=('any')
url='https://github.com/dstathis/fastprocess'
license=('Apache')
makedepends=(
  'python-setuptools'
)
source=("https://github.com/fastai/fastprogress/archive/${pkgver}.tar.gz")
sha512sums=('bb2c7666523cbbadbf7ef31e4a74a8cdc96e84d152eb75704b5e210e38f70063aa13deada3edad0cc708d57b6d626da5408ca9b4a7ff074c43fa38fcd82bcdbe')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
