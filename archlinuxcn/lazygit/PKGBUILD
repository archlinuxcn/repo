# Maintainer: Fredy García <frealgagu at gmail dot com>
# Maintainer: fuero <fuerob@gmail.com>

pkgname=lazygit
pkgver=0.17.4
pkgrel=1
pkgdesc="A simple terminal UI for git commands"
arch=("x86_64")
url="https://github.com/jesseduffield/${pkgname}"
license=("MIT")
depends=("glibc")
makedepends=("go-pie")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/jesseduffield/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=("75b8ee9d22d7b910704a4ab7012efcc2e9c24d1ba51488ef99a236a9bcb61cad")
_commit="5d460e1e5e002ae3f4deb6b75e77b5916d672cc5"

prepare() {
  mkdir -p "${srcdir}/src/github.com/jesseduffield"
  ln -rTsf "${srcdir}/${pkgname}-${pkgver}" "${srcdir}/src/github.com/jesseduffield/${pkgname}"
}

build () {
  cd "${srcdir}/src/github.com/jesseduffield/${pkgname}"
  GOPATH="${srcdir}" PATH="${PATH}:${GOPATH}/bin" go build -x -i -v -ldflags "-extldflags ${LDFLAGS} -X main.commit=${_commit} -X main.date=$(date -u +%Y-%m-%dT%H:%M:%SZ) -X main.buildSource=binaryRelease -X main.version=${pkgver}" -o "${pkgname}.bin"
  # To avoid issues deleting directories next time
  GOPATH="${srcdir}" go clean --modcache
}

package () {
  install -Dm755 "${srcdir}/${pkgname}-${pkgver}/${pkgname}.bin" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  for _file in "${srcdir}/${pkgname}-${pkgver}/"*.md "${srcdir}/${pkgname}-${pkgver}/docs/"*.md
  do
    install -Dm644 "${_file}" "${pkgdir}/usr/share/doc/${pkgname}/$(basename ${_file})"
  done
}
