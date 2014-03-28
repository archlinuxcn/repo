# Maintainer: Alexandre de Verteuil <claudelepoisson at gmail dot com>

pkgname=python3-stagger-svn
pkgver=106
pkgrel=4
pkgdesc="MP3 tag manipulation package for Python 3"
arch=('any')
url="http://code.google.com/p/stagger/"
license=('BSD')
depends=('python')
makedepends=('subversion' 'python-setuptools')
source=("$pkgname"::'svn+http://stagger.googlecode.com/svn/trunk/')
md5sums=('SKIP')

pkgver()
{
  cd "$srcdir/$pkgname"
  local ver="$(svnversion)"
  printf "%s" "${ver//[[:alpha:]]}"
}

build()
{
  cd "$srcdir/$pkgname"
  # Comment out lines regarding distribute_setup.
  # Use python-setuptools installed as makedepend.
  sed -i "/distribute_setup/ s/^/#/" setup.py
  python setup.py build
}

package()
{
  cd "$srcdir/$pkgname"
  python setup.py install --root=$pkgdir
}
