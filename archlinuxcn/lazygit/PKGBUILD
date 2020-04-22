# Maintainer: Fredy García <frealgagu at gmail dot com>
# Maintainer: fuero <fuerob@gmail.com>

pkgname=lazygit
pkgver=0.20
pkgrel=1
pkgdesc="A simple terminal UI for git commands"
arch=("x86_64")
url="https://github.com/jesseduffield/${pkgname}"
license=("MIT")
depends=("glibc")
makedepends=("go-pie")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/jesseduffield/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=("36689f98b0bbb9e227cf80daa802739c77e5f8a2cc2690fdcffb3c8598a4aa95")
_commit="f05a5e531ee8271e0232db7f3bb7202ea550656e"

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
