# Maintainer : Felix Yan <felixonmars@gmail.com>
_name=repoze.profile
pkgname=python2-$_name
pkgver=1.4
pkgrel=1
pkgdesc="Aggregate profiling for WSGI requests"
arch=('any')
license=('BSD' 'custom')
url="http://docs.repoze.org/profile/"
depends=('python2')
makedepends=('python2-distribute')
source=(http://pypi.python.org/packages/source/r/$_name/$_name-$pkgver.tar.gz)
md5sums=('8f91d26cbb967213e36fe55c68f31024')

build() {
  cd "${srcdir}/${_name}-${pkgver}"

  python2 setup.py install --root="${pkgdir}"
  rm -fr ${pkgdir}/usr/lib/python*/site-packages/repoze/debug/tests
}
