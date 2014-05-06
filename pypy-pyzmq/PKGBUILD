# $Id: PKGBUILD 109144 2014-04-10 20:30:56Z kkeen $
# Maintainer: Kyle Keen <keenerd at gmail dot com>
pkgbase=pypy-pyzmq
true && pkgname=(pypy-pyzmq pypy3-pyzmq)
pkgname=pypy-pyzmq
pkgver=14.1.1
pkgrel=1
pkgdesc="Python bindings for zeromq, pypy version"
arch=(i686 x86_64)
url="http://www.zeromq.org/bindings:python"
license=('LGPL')
depends=(zeromq pypy)
makedepends=(pypy pypy3 zeromq)
#source=(https://github.com/zeromq/pyzmq/downloads/pyzmq-$pkgver.tar.gz)
source=(https://pypi.python.org/packages/source/p/pyzmq/pyzmq-$pkgver.tar.gz
  compiler.json)
md5sums=('bea18143c347dcde92cd0409392fbb58'
         '9222c8150542cf09e89ee0a4ebac4ce7')

build() {
  cd "$srcdir"
  cp -a pyzmq-${pkgver} py2zmq-${pkgver}
  cd "$srcdir/pyzmq-$pkgver"
  # py3 errors added in 2.2.0.1
  sed -i 's|except socket.error, e:|except socket.error as e:|' \
    zmq/eventloop/ioloop.py
  sed -i 's|except gevent.Timeout, t:|except gevent.Timeout as t:|' \
    zmq/green/core.py
  sed -i 's|^#!/usr/bin/env python$|#!/usr/bin/env pypy3|' \
    $(find ./ -name '*.py')

  cd "$srcdir/py2zmq-$pkgver"
  sed -i 's|^#!/usr/bin/env python$|#!/usr/bin/env pypy|' \
    $(find ./ -name '*.py')
}

_fix_cffi() {
  cd "${srcdir}"
  mv -v "${pkgdir}/opt/$1/site-packages/zmq/utils/compiler.json" \
    compiler.json.$1
  cp compiler.json "${pkgdir}/opt/$1/site-packages/zmq/utils/compiler.json"
  PYTHONPATH="${pkgdir}/opt/$1/site-packages" $1 -c "import $2"
  find "$pkgdir/" -name '*.o' -delete
  find "$pkgdir/" -type d -empty -delete
  mv -v compiler.json.$1 \
    "${pkgdir}/opt/$1/site-packages/zmq/utils/compiler.json"
}

package_pypy-pyzmq() {
  pkgdesc="PyPy bindings for zeromq"
  depends=(zeromq pypy)
  cd "$srcdir/py2zmq-$pkgver"
  pypy setup.py install --root="$pkgdir" --optimize=0
  (_fix_cffi pypy zmq)
}

package_pypy3-pyzmq() {
  pkgdesc="PyPy3 bindings for zeromq"
  depends=(zeromq pypy3)

  cd "$srcdir/pyzmq-$pkgver"
  pypy3 setup.py install --root="$pkgdir" --optimize=0
  (_fix_cffi pypy3 zmq)
}
