# Maintainer: Fredy García <frealgagu at gmail dot com>
# Maintainer: fuero <fuerob@gmail.com>

pkgname=lazygit
pkgver=0.13
pkgrel=1
pkgdesc="A simple terminal UI for git commands"
arch=("x86_64")
url="https://github.com/jesseduffield/${pkgname}"
license=("MIT")
depends=("glibc")
makedepends=("go-pie")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/jesseduffield/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=("93ca0847cd91874228b023d9feb967aaa819532f173fd6e19e2d00b8a6242e3c")
_commit="d647a96ed55e134f1464878be8d0be3a464d996f"

prepare() {
  rm -rf "${srcdir}/gopath"
  mkdir -p "${srcdir}/src/github.com/jesseduffield"
  ln -rTsf "${srcdir}/${pkgname}-${pkgver}" "${srcdir}/src/github.com/jesseduffield/${pkgname}"
}

build () {
  cd "${srcdir}/src/github.com/jesseduffield/${pkgname}"
  GOPATH="${srcdir}" PATH="${PATH}:${GOPATH}/bin" go build -x -i -v -ldflags "-extldflags ${LDFLAGS} -X main.commit=${_commit} -X main.date=$(date -u +%Y-%m-%dT%H:%M:%SZ) -X main.buildSource=binaryRelease -X main.version=${pkgver}" -o "${pkgname}.bin"
}

package () {
  install -Dm755 "${srcdir}/${pkgname}-${pkgver}/${pkgname}.bin" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  for _file in "${srcdir}/${pkgname}-${pkgver}/"*.md "${srcdir}/${pkgname}-${pkgver}/docs/"*.md
  do
    install -Dm644 "${_file}" "${pkgdir}/usr/share/doc/${pkgname}/$(basename ${_file})"
  done
}
