# Maintainer: drakkan <nicola.murino at gmail dot com>
# Contributor: Pierre Carrier <pierre at gcarrier dot fr>
pkgname=wrk
pkgver=4.1.0
pkgrel=4
pkgdesc="Modern HTTP benchmarking tool"
arch=(i686 x86_64 aarch64)
url="https://github.com/wg/wrk/"
license=(Apache)
depends=('openssl' 'luajit')
source=("https://github.com/wg/$pkgname/archive/${pkgver}.tar.gz")
sha256sums=('6fa1020494de8c337913fd139d7aa1acb9a020de6f7eb9190753aa4b1e74271e')
options=('!makeflags'
         '!buildflags')

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  if [ -d "/usr/include/luajit-2.0" ]
  then
    sed -i "s/[(]WITH_LUAJIT[)]\/include/\(WITH_LUAJIT\)\/include\/luajit-2.0/" Makefile
  elif [ -d "/usr/include/luajit-2.1" ]
  then
    sed -i "s/[(]WITH_LUAJIT[)]\/include/\(WITH_LUAJIT\)\/include\/luajit-2.1/" Makefile
  fi
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  make WITH_OPENSSL=/usr WITH_LUAJIT=/usr
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -Dm755 wrk "${pkgdir}/usr/bin/wrk"
  install -Dm644 LICENSE "${pkgdir}"/usr/share/licenses/wrk/LICENSE
  install -Dm644 NOTICE "${pkgdir}"/usr/share/licenses/wrk/NOTICE
  install -d -m755 "${pkgdir}"/usr/share/doc/wrk/examples/
  install -Dm644 README.md "${pkgdir}"/usr/share/doc/wrk/README
  install -Dm644 SCRIPTING "${pkgdir}"/usr/share/doc/wrk/SCRIPTING
  install -Dm644 CHANGES "${pkgdir}"/usr/share/doc/wrk/CHANGES
  install -Dm644 scripts/*.lua "${pkgdir}"/usr/share/doc/wrk/examples/
}

# vim:set ts=2 sw=2 et:

