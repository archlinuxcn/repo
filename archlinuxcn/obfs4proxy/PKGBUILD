# Maintainer: mutantmonkey <aur@mutantmonkey.in>
# Contributor: shyokou <shyokou at gmail dot com>
# Contributor: FzerorubigD <Fzerorubigd {AT} GMail {DOT} com>
pkgname=obfs4proxy
_gitname=obfs4
pkgver=0.0.8
pkgrel=1
pkgdesc='The obfourscator - a pluggable transport proxy written in Go'
arch=('i686' 'x86_64')
url='https://gitweb.torproject.org/pluggable-transports/obfs4.git/'
license=('BSD')
makedepends=('git' 'go')
optdepends=('tor: you need tor to use this package')
source=("https://people.torproject.org/~yawning/releases/obfs4proxy/obfs4proxy-${pkgver}.tar.xz")
sha512sums=('2b92fd3353184f9aa4fc08e9415b92908c10bbd462d8a7576fa81bc67636d49aa645b1efef64f948bad2c4ee67f4b74d68c3e289b4da66128f3d94f8d9987bc1')

build()	{
  cd "${srcdir}/${_gitname}/obfs4proxy"
  GOPATH="$srcdir" GOBIN="$PWD" go get -v
}

package()	{
  cd "${srcdir}/${_gitname}"
  install -Dm0755 obfs4proxy/obfs4proxy "${pkgdir}/usr/bin/obfs4proxy"
  install -Dm0644 doc/obfs4proxy.1 "${pkgdir}/usr/share/man/man1/obfs4proxy.1"
  install -Dm0644 ChangeLog "${pkgdir}/usr/share/doc/${pkgname}/ChangeLog"
  install -Dm0644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

## vim:set ts=2 sw=2 et:
