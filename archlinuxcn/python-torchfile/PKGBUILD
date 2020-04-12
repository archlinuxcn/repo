# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchfile
pkgver=0.1.0
pkgrel=3
pkgdesc='Deserialize torch-serialized objects from Python'
arch=(any)
url=https://github.com/bshillingford/python-torchfile
license=(BSD)
makedepends=(python-setuptools)
checkdepends=(python-flaky python-numpy python-pytest python-pytest-cov)
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/bshillingford/python-torchfile/archive/${pkgver}.tar.gz")
sha512sums=('feaab6dafe859d188a121c90f7a6c53cd1521ec76b674c4b01cec630cf159a357c244d294eff9870c06b2c93a0d94e9fc77fba292637b8a39e87672cdaa031ec')

build() {
  cd "${pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${pkgname}-${pkgver}"
  pytest -v tests.py
}

package() {
  cd "${pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
