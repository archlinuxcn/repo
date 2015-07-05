# Maintainer: Marcin Kulik <m@ku1ik.com>

_pkgname=asciinema
pkgname=asciinema
pkgver=1.1.1
pkgrel=2
pkgdesc="Record and share your terminal sessions, the right way"
url="https://asciinema.org/"
license=('GPLv3')
arch=('x86_64' 'i686' 'arm')
source=("https://github.com/asciinema/asciinema/archive/v${pkgver}.tar.gz")
sha1sums=('c07d84bd0df57cae873bacec1a5c41b9ea5786bc')
makedepends=('make' 'go')

build() {
  mkdir -p "${srcdir}/go/src/github.com/asciinema"
  ln -nfs "${srcdir}/${_pkgname}-${pkgver}" "${srcdir}/go/src/github.com/asciinema/asciinema"
  cd "${srcdir}/${_pkgname}-${pkgver}"
  GOPATH="${srcdir}/go" go build -o bin/asciinema
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  PREFIX=${pkgdir}/usr make install
}
