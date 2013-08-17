pkgname=python-pillow
_appname=Pillow
pkgver=2.1.0
pkgrel=1
pkgdesc="Python Imaging Library (PIL) fork. Python3 version"
arch=(i686 x86_64)
url="https://github.com/python-imaging/Pillow"
license=('BSD')
depends=('python')
provides=('python-imaging' 'python3-imaging')
conflicts=('python-imaging' 'python3-imaging' 'python-pillow-git')
makedepends=('python-distribute')
source=("http://pypi.python.org/packages/source/P/${_appname}/${_appname}-${pkgver}.zip")
md5sums=('ec630d8ae15d4a3c4ae7b7efdeac8200')

package() {
  cd "$srcdir/$_appname-$pkgver"
  python3 setup.py install --root="$pkgdir/" --optimize=1
}

