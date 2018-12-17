# Maintainer: Fredy García <frealgagu at gmail dot com>
# Maintainer: Maxim Baz <$pkgname at maximbaz dot com>
# Contributor: Stefan Cocora <stefan dot cocora at gmail dot com>

_pkgauthor=GoogleContainerTools
_commit=9eb0dfc1bf634b97462c66b4dfb80e4cea378ade
pkgname=skaffold
pkgver=0.19.0
pkgrel=3
pkgdesc="A command line tool that facilitates continuous development for Kubernetes applications"
arch=("x86_64")
url="https://github.com/${_pkgauthor}/${pkgname}"
license=("Apache")
depends=("docker" "kubectl-bin")
makedepends=("go-pie")
optdepends=("google-cloud-sdk: To use GKE"
            "minikube: To use Minikube")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/${_pkgauthor}/${pkgname}/archive/v${pkgver}.tar.gz"
        "build_info.patch"
        "${pkgname}-${pkgver}-index.html::https://storage.googleapis.com/${pkgname}/releases/v${pkgver}/docs/index.html"
        "${pkgname}-${pkgver}-index.pdf::https://storage.googleapis.com/${pkgname}/releases/v${pkgver}/docs/index.pdf")
sha256sums=("48fee7f29e6dac4a301d3facf607796b04b7d1ee0b433fd083e3100bf38f7a38"
            "af5bd6a9a1e9e2f7d941ffdbd4aebd37e32bb390be03c52a578f3931997f220d"
            "932bb93b9d321d1e3dc974d171cea360a04f2e233d3bc759a32cc34859296285"
            "8645efc4d2da7d6a0aeb23b2bc81d069bfd490e06ff78df82aab13a36e1ab85a")

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  patch -Np1 -i "${srcdir}/build_info.patch"

  rm -rf "${srcdir}/gopath"
  mkdir -p "${srcdir}/gopath/src/github.com/${_pkgauthor}"
  ln -rTsf "${srcdir}/${pkgname}-${pkgver}" "${srcdir}/gopath/src/github.com/${_pkgauthor}/${pkgname}"
}

build() {
  cd "${srcdir}/gopath/src/github.com/${_pkgauthor}/${pkgname}"
  GOPATH="${srcdir}/gopath" PATH="${PATH}:${GOPATH}/bin" VERSION="v${pkgver}" COMMIT="${_commit}" TREE_STATE="clean" make install
}

package() {
  install -Dm755 "${srcdir}/gopath/bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}-index.html" "${pkgdir}/usr/share/doc/${pkgname}/html/index.html"
  install -Dm644 "${srcdir}/${pkgname}-${pkgver}-index.pdf" "${pkgdir}/usr/share/doc/${pkgname}/pdf/index.pdf"
}
