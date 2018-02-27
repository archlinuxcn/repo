# Maintainer: eolianoe <eolianoe [at] gmail [DoT] com>
# Contributor: Aaron Lindsay <aaron@aclindsay.com>
# Contributor: Edvinas Valatka <edacval@gmail.com>
# Contributor: Adrian Hühn <adrian.huehn@web.de>

pkgname=ccnet-server
pkgver=6.2.5
pkgrel=4
pkgdesc="Internal communication framework and user/group management for seafile server"
arch=('i686' 'x86_64' 'armv7h' 'armv6h' 'aarch64')
url="https://github.com/haiwen/${pkgname}"
license=('GPL2')
depends=('libevent' 'libsearpc' 'libldap' 'libmariadbclient' 'postgresql-libs')
makedepends=('vala')
conflicts=('ccnet')
source=("${pkgname}-v${pkgver}-server.tar.gz::${url}/archive/v${pkgver}-server.tar.gz"
        "libccnet.pc.patch"
        "openssl-1.1.diff")
sha256sums=('e7094278cf1ffdda852e18acb7d968200916c187517fc41284ec2f759aa8abeb'
            '66c3b02c3981db6a80819e0ae103bedadf8dfdf81405a7f75a9cba714acf973f'
            'f98a17d467214984d11ddf819e02d54b2b88e89ebafec1955922e43c123800d4')

prepare () {
  cd "${srcdir}/${pkgname}-${pkgver}-server"
  patch -p1 -i "${srcdir}"/libccnet.pc.patch
  patch -p1 -i "${srcdir}"/openssl-1.1.diff
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
