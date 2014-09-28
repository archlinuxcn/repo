pkgbase='pypy-mako'
pkgname=('pypy3-mako' 'pypy-mako')
pkgver=1.0.0
pkgrel=1
pkgdesc="Hyperfast and lightweight templating for the Python platform"
arch=('any')
url="http://www.makotemplates.org/"
license=('MIT')
makedepends=('pypy-setuptools' 'pypy3-setuptools' 'python>=3.4' # for 2to3
  'pypy-markupsafe' 'pypy3-markupsafe' 'pypy-beaker' 'pypy3-beaker')
source=(https://pypi.python.org/packages/source/M/Mako/Mako-$pkgver.tar.gz{,.asc})
sha1sums=('580b3a8043833e3c3340d4b661a33f6ccc6a35d5'
          'SKIP')
options=('!emptydirs')

prepare() {
    cp -r Mako-$pkgver python2-Mako-$pkgver
}

build() {
    cd Mako-$pkgver
    pypy3 setup.py build

    cd ../python2-Mako-$pkgver
    pypy setup.py build
}

package_pypy3-mako() {
    depends=('pypy3-markupsafe' 'pypy3-beaker' 'pypy3')

    cd Mako-$pkgver
    pypy3 setup.py install --skip-build --root="$pkgdir" --optimize=1
    install -D LICENSE "$pkgdir/usr/share/licenses/pypy3-mako/COPYING"
    install -m755 -d "${pkgdir}/usr/bin/"
    mv "${pkgdir}"/opt/pypy3/bin/mako-render \
      "${pkgdir}/usr/bin/pypy3-mako-render"
}

package_pypy-mako() {
    depends=('pypy-markupsafe' 'pypy-beaker' 'pypy')

    cd python2-Mako-$pkgver
    pypy setup.py install --skip-build --root="$pkgdir" --optimize=1
    install -D LICENSE "$pkgdir/usr/share/licenses/pypy-mako/COPYING"
    install -m755 -d "${pkgdir}/usr/bin/"
    mv "${pkgdir}"/opt/pypy/bin/mako-render \
      "${pkgdir}/usr/bin/pypy-mako-render"
}
