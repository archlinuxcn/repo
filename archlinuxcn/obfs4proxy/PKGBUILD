# Maintainer: mutantmonkey <aur@mutantmonkey.in>
# Contributor: shyokou <shyokou at gmail dot com>
# Contributor: FzerorubigD <Fzerorubigd {AT} GMail {DOT} com>
pkgname=obfs4proxy
pkgver=0.0.11
pkgrel=1
pkgdesc='The obfourscator - a pluggable transport proxy written in Go'
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url='https://gitweb.torproject.org/pluggable-transports/obfs4.git/'
license=('BSD')
makedepends=('git' 'go')
optdepends=('tor: you need tor to use this package')
source=("https://people.torproject.org/~yawning/releases/obfs4proxy/obfs4proxy-${pkgver}.tar.xz")
sha512sums=('7d7fef951bcebd4433dfb638896d4be15dc090d38a3b54c9a9d34ea264b006cff75a42da1b97b6af998cfbc3b44919770cd8cb519ada351486a247faf47c656f')

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
