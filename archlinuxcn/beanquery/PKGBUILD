# Maintainer: Zhuoyun Wei <wzyboy@wzyboy.org>

pkgname=beanquery
pkgdesc='A customizable light-weight SQL query tool that works on tabular data, including Beancount'
pkgver=0.2.0
pkgrel=1
arch=("any")
url="https://github.com/beancount/beanquery"
license=('GPL')
source=("https://files.pythonhosted.org/packages/source/${pkgname::1}/${pkgname}/${pkgname}-${pkgver}.tar.gz")
b2sums=('2b9c389fcafe5186beba9c2b0cb1178fa78e7cb415c0f9e72c23f88ef947f8bfe8971f27fc87c4675d85ff965c8d6d5181cf23f8607f298e58a0354841a9b6d8')
# NOTE: The Python package technically does not require beancount 3.x but it
# provides /usr/bin/bean-query which conflicts with beancount 2.x and so we
# require beancount 3.x here.
depends=("python" "beancount>=3" "python-click" "python-tatsu-lts")
makedepends=("python-build" "python-installer" "python-wheel" "python-setuptools")

build() {
  cd "${pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  rm -r ${pkgdir}/usr/lib/python3*/site-packages/docs
}
