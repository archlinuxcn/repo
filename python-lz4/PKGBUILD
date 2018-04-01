# Maintainer: Nissar Chababy <funilrys at outlook dot com>
# Co-Maintainer: Thrasibule <guillaume dot horel at gmail dot com>
# Ex-Maintainer: David Manouchehri <manouchehri@riseup.net>
# Contributor: Vladimir Tsanev <tsachev@gmail.com>
# Contributor: Andrew Reed <reed.996@osu.edu>

pkgname=python-lz4
_pkgname=lz4
pkgver=1.0.0
pkgrel=3
pkgdesc="LZ4 Bindings for Python"
arch=('x86_64')
url="https://pypi.python.org/pypi/lz4"
license=('BSD')
makedepends=('python-distribute' 'python-setuptools')
depends=('python' 'python-deprecation')
checkdepends=('python-pytest')
source=("https://pypi.org/packages/source/${_pkgname:0:1}/$_pkgname/${_pkgname}-${pkgver}.tar.gz")
md5sums=('420e428921f02ebcb4dc8c40a9d0f484')

package() {
  cd ${srcdir}/${_pkgname}-${pkgver}
  python setup.py install --root=${pkgdir} || return 1
}
