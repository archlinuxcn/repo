# Maintainer: mutantmonkey <aur@mutantmonkey.mx>
# Contributor: shyokou <shyokou at gmail dot com>
# Contributor: FzerorubigD <Fzerorubigd {AT} GMail {DOT} com>
pkgname=obfs4proxy
pkgver=0.0.14
pkgrel=1
pkgdesc='The obfourscator - a pluggable transport proxy written in Go'
arch=('i686' 'x86_64' 'armv6h' 'armv7h' 'aarch64')
url='https://gitlab.com/yawning/obfs4'
license=('BSD')
makedepends=('git' 'go')
optdepends=('tor: you need tor to use this package')
source=("https://gitlab.com/yawning/obfs4/-/archive/obfs4proxy-${pkgver}/obfs4-obfs4proxy-${pkgver}.tar.bz2")
sha512sums=('a720d45250140e3ba02b176d84fd80cca55304c09d5cebbd0fda45a3f5cfd7c2e8ffb6a2588a7b98a2ce03854969b0b1f949dca0405b16de29e90842861657c1')

build()	{
  export GOPATH="$srcdir"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

  cd "${srcdir}/obfs4-obfs4proxy-${pkgver}"
  GOPATH="${srcdir}/go" go build -o obfs4proxy/obfs4proxy ./obfs4proxy
}

package()	{
  cd "${srcdir}/obfs4-obfs4proxy-${pkgver}"
  install -Dm0755 obfs4proxy/obfs4proxy "${pkgdir}/usr/bin/obfs4proxy"
  install -Dm0644 doc/obfs4proxy.1 "${pkgdir}/usr/share/man/man1/obfs4proxy.1"
  install -Dm0644 ChangeLog "${pkgdir}/usr/share/doc/${pkgname}/ChangeLog"
  install -Dm0644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}

## vim:set ts=2 sw=2 et:
