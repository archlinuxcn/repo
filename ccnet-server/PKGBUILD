# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname=ccnet-server
pkgver=6.0.10
pkgrel=1
pkgdesc="A framework for writing networked applications in C."
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/${pkgname}"
license=('GPL2')
depends=('libevent' 'libzdb' 'libsearpc' 'libldap' 'python2')
makedepends=('vala' 'libmariadbclient')
source=("${pkgname}-v${pkgver}-server.tar.gz::${url}/archive/v${pkgver}-server.tar.gz"
        "libccnet.pc.patch")
sha256sums=('1a31a917c143c74bbb6fd67c54ee61841c343650b70f3d07dc130c990d8ffc1f'
            '66c3b02c3981db6a80819e0ae103bedadf8dfdf81405a7f75a9cba714acf973f')

prepare () {
  cd "${srcdir}/${pkgname}-${pkgver}-server"
  patch -p1 -i "${srcdir}"/libccnet.pc.patch
}

build () {
  cd "${srcdir}/${pkgname}-${pkgver}-server"
  ./autogen.sh
  ./configure --enable-ldap --enable-python --enable-console --prefix=/usr PYTHON=/usr/bin/python2
  make
}

package () {
  cd "${srcdir}/${pkgname}-${pkgver}-server"
  make DESTDIR="$pkgdir" install
}
