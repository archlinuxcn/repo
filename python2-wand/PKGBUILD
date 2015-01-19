# Maintainer: Panagiotis Mavrogiorgos (pmav99) <> (gmail)

_name=Wand
pkgname=python2-wand
pkgver=0.3.9
pkgrel=1
pkgdesc="A ctypes-based simple ImageMagick binding for Python."
arch=(any)
url="http://wand-py.org/"
license=('BSD')
depends=('python2' 'imagemagick')
optdepends=()
provides=('wand')
conflicts=()
replaces=()
backup=()
options=(!emptydirs)
source=(http://pypi.python.org/packages/source/W/Wand/$_name-$pkgver.tar.gz)
md5sums=('edd5086fa43afdb6795187f31cc7657f')



package()
{
  # Install using setup.py
  cd "$srcdir/$_name-$pkgver"
  python2 setup.py install --root="${pkgdir}/" --optimize=1

  # The README file conflicts with the README file of the python3-wand package.
  mv $pkgdir/usr/README.rst README-wand2.rst

}
# vim: sw=2 ts=2 et:
