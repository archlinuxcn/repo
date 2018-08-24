# Maintainer: Fredy García <frealgagu at gmail dot com>
# Maintainer: fuero <fuerob@gmail.com>

pkgname=lazygit
pkgver=0.1.79
pkgrel=1
pkgdesc="A simple terminal UI for git commands"
arch=("x86_64")
url="https://github.com/jesseduffield/${pkgname}"
license=("MIT")
depends=("glibc")
makedepends=("go-pie")
provides=("lazygit")
conflicts=("lazygit-git")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/jesseduffield/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=("eed9516d1b944ce4528a5d308d1dd49ee7932cf1d8ec6955556cc4dfe737f9a3")
_commit="22de5e7b235389bcbb32e132ddc86c8726516268"

build () {
  echo "Linking to repository path..."
  mkdir -p "${srcdir}/src/github.com/jesseduffield"
  ln -s "${srcdir}/${pkgname}-${pkgver}" "${srcdir}/src/github.com/jesseduffield/${pkgname}"
  cd "${srcdir}/src/github.com/jesseduffield/${pkgname}"
  
  echo "Building..."
  GOPATH="${srcdir}" PATH="${PATH}:${GOPATH}/bin" go build -x -i -v -ldflags "-X main.commit=${_commit:0:7} -X main.date=$(date -u +%Y%m%d.%H%M%S) -X main.version=${pkgver}" -o "${pkgname}.bin"
  
  echo "Removing link..."
  rm -rf "${srcdir}/src"
}

package () {
  install -Dm755 "${srcdir}/${pkgname}-${pkgver}/${pkgname}.bin" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}/LICENSE" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  for _file in ${srcdir}/${pkgname}-${pkgver}/*.md ${srcdir}/${pkgname}-${pkgver}/docs/*.md
  do
    install -Dm644 "${_file}" "${pkgdir}/usr/share/doc/${pkgname}/$(basename ${_file})"
  done
}
