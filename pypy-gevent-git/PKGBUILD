pkgname=pypy-gevent-git
pkgver=1.0.0.157.gadb7b83
pkgrel=1
arch=('i686' 'x86_64')
pkgdesc="Python network library that uses greenlet and libev for easy and scalable concurrency"
license=("MIT")
url="http://www.gevent.org/"
depends=('pypy>=2.4' 'pypy<2.5')
makedepends=('git' 'pypy-setuptools')
source=("git://github.com/surfly/gevent.git"
  0001-use-system-install-path-for-ffi.verify.patch
  cc)
md5sums=('SKIP'
         '07988b40275d9a6b15afdafaddcd3a96'
         '10b3d7f87030bb9afe66e7ff5bb37647')
options=('debug' 'strip' '!emptydirs')

pkgver() {
  cd gevent
  git describe --tags | sed 's/-/.0./;s/-/./g'
}

prepare() {
  cd gevent
  patch -Np1 < ../0001-use-system-install-path-for-ffi.verify.patch
}

package() {
  cd gevent

  export __GEVENT_PKGDIR="${pkgdir}/opt/pypy/site-packages/gevent"
  export __GEVENT_PKGDIR2="${srcdir}/gevent/gevent/"
  export PATH="${srcdir}:${PATH}"
  LIBEV_EMBED=1 \
    CARES_EMBED=1 \
    PYTHON=pypy \
    pypy setup.py build
  pypy setup.py install -O1 --root="$pkgdir"
  install -Dm0644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
  find "$pkgdir" -name '*.c' -exec rm {} \;
  find "$pkgdir" -name '*.o' -exec rm {} \;
  find "$pkgdir/opt/pypy/site-packages/gevent/libev" -type f \
    \( -name '*.py*' -o -exec rm {} \; \)
}
