# Maintainer: mutantmonkey <aur@mutantmonkey.in>
# Contributor: shyokou <shyokou at gmail dot com>
# Contributor: FzerorubigD <Fzerorubigd {AT} GMail {DOT} com>
pkgname=obfs4proxy
pkgver=0.0.10
pkgrel=1
pkgdesc='The obfourscator - a pluggable transport proxy written in Go'
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url='https://gitweb.torproject.org/pluggable-transports/obfs4.git/'
license=('BSD')
makedepends=('git' 'go')
optdepends=('tor: you need tor to use this package')
source=("https://people.torproject.org/~yawning/releases/obfs4proxy/obfs4proxy-${pkgver}.tar.xz")
sha512sums=('0781ac16b3f81513c65d08cd6f0af890eaec01b99e51a3151c23f573055562d8658d41d3b90817b55bd910a75236c483f59e3733bdb1bba18178d36e0aa187bd')

build()	{
  cd "${srcdir}/"
  GOPATH="${srcdir}/go" go build -o obfs4proxy/obfs4proxy ./obfs4proxy
}

package()	{
  cd "${srcdir}/"
  install -Dm0755 obfs4proxy/obfs4proxy "${pkgdir}/usr/bin/obfs4proxy"
  install -Dm0644 doc/obfs4proxy.1 "${pkgdir}/usr/share/man/man1/obfs4proxy.1"
  install -Dm0644 ChangeLog "${pkgdir}/usr/share/doc/${pkgname}/ChangeLog"
  install -Dm0644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

## vim:set ts=2 sw=2 et:
