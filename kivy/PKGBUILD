# Maintainer: speps <speps at aur dot archlinux dot org>

pkgname=kivy
pkgver=1.7.1
pkgrel=2
pkgdesc="A python module for developing multi-touch enabled media rich applications."
arch=(i686 x86_64)
url="http://kivy.org/"
license=('LGPL')
depends=('python2-pygame' 'python2-opengl' 'python2-imaging'
         'gstreamer0.10-python' 'cython2' 'libgl')
makedepends=('mesa')
optdepends=('twisted: networking framework integration'
            'python2-pygments: syntax highligh'
            'python2-docutils: reStructuredText renderer'
            'python2-requests: garden utility')
source=("http://pypi.python.org/packages/source/K/Kivy/Kivy-$pkgver.tar.gz")
md5sums=('2ee737365190a1a42c4502488ce55334')

build() {
  cd "$srcdir/Kivy-$pkgver"
  python2 setup.py build
}

package() {
  cd "$srcdir/Kivy-$pkgver"
  python2 setup.py install --root="$pkgdir"

  # rename the garden utility to prevent
  # conflicts with the garder game
  mv "$pkgdir/usr/bin/garden" "$pkgdir/usr/bin/kivy-garden"

  # python2 fixes
  sed -i "s/\#\!.*python$/&2/" \
    `grep -rl "\#\!.*python$" "$pkgdir"`
}

# vim:set ts=2 sw=2 et:
