# Maintainer: Fabius
# Contributor: Angel 'angvp' Velasquez <angvp[at]archlinux.com.ve>
# Contributor: Abhishek Dasgupta <abhidg@gmail.com>

_pkgname=python-distutils-extra
pkgname=python2-distutils-extra
pkgver=2.39
pkgrel=5
pkgdesc='Enhancements to the Python build system'
arch=('any')
license=('GPL')
url='https://launchpad.net/python-distutils-extra'
depends=('intltool' 'python2')
makedepends=('python2-setuptools' 'intltool')
source=(https://launchpad.net/$_pkgname/trunk/$pkgver/+download/$_pkgname-$pkgver.tar.gz)
md5sums=('16e06db0ef73a35b4bff4b9eed5699b5')

package() {
  cd "${srcdir}/$_pkgname-$pkgver"
  python2 setup.py install --root="${pkgdir}"
}

