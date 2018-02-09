# Maintainer: Jonathan Kotta <jpkotta at gmail dot com>
# Contributor: Andreas Theodosiou <andreasabu at gmail dot com>
# Contributor: Jarek Sedlacek <jareksedlacek at gmail dot com>

pkgname=3to2
pkgver=1.1.1
pkgrel=2
pkgdesc="Script to convert python3 code to python2. Counterpart to 2to3"
arch=('any')
license=('Apache')
url='https://pypi.python.org/pypi/3to2'
depends=('python')
makedepends=()
# files.pythonhosted.org URL as suggested by Arch Wiki doesn't work
source=('https://pypi.python.org/packages/8f/ab/58a363eca982c40e9ee5a7ca439e8ffc5243dde2ae660ba1ffdd4868026b/3to2-1.1.1.zip')
md5sums=('cbeed28e350dbdaef86111ace3052824')

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  sed -i 's/Exception, err:/Exception as err:/' lib3to2/build.py
  python ./setup.py install --root="${pkgdir}" --optimize=1
  rm -rf "${pkgdir}"/usr/lib/python*/site-packages/lib3to2/tests/
}
