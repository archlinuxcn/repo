# Maintainer: Andrew Steinke <rkcf@rkcf.me>
# Contributor: Philip Goto <philip.goto@gmail.com>

_pkgname=face_recognition
pkgname=python-$_pkgname
pkgver=1.3.0
pkgrel=1
pkgdesc="The world's simplest facial recognition api for Python and the command line"
url="https://github.com/ageitgey/face_recognition"
depends=('python-click'
         'python-dlib'
         'python-face_recognition_models'
         'python-numpy'
         'python-pillow'
         'python-scipy')
makedepends=('python-setuptools')
license=(MIT)
arch=(any)
source=("https://files.pythonhosted.org/packages/source/f/$_pkgname/$_pkgname-$pkgver.tar.gz")
md5sums=('4e54f245f8fe4751a9f0ef5301a7cd40')

build(){
  cd $srcdir/$_pkgname-$pkgver
  python setup.py build
}

package(){
  cd $srcdir/$_pkgname-$pkgver
  python setup.py install --skip-build --root="$pkgdir" --optimize=1
  install -Dm644 LICENSE "$pkgdir/usr/share/license/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
