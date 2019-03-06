# Maintainer: Fredy García <frealgagu at gmail dot com>
# Maintainer: Maxim Baz <${pkgname} at maximbaz dot com>
# Contributor: Stefan Cocora <stefan dot cocora at gmail dot com>

pkgname=skaffold
pkgver=0.24.0
pkgrel=1
pkgdesc="A command line tool that facilitates continuous development for Kubernetes applications"
arch=("x86_64")
url="https://github.com/GoogleContainerTools/${pkgname}"
license=("Apache")
depends=("docker" "kubectl")
makedepends=("go-pie")
optdepends=("google-cloud-sdk: To use GKE"
            "minikube: To use Minikube")
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/GoogleContainerTools/${pkgname}/archive/v${pkgver}.tar.gz"
        "build_info.patch")
sha256sums=("847131473f7cbacbd7811defea3b675769eb8cba6c2bb32553a1f9b8f05af0b9"
            "39b1e127a29979ef559e0a92cd721b23d6eac4251c703befd882b8667ac9789e")
_commit="6a829c4b29e3a102b0b14c4584cd174f780402e9"

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  patch -Np1 -i "${srcdir}/build_info.patch"

  rm -rf "${srcdir}/gopath"
  mkdir -p "${srcdir}/gopath/src/github.com/GoogleContainerTools"
  ln -rTsf "${srcdir}/${pkgname}-${pkgver}" "${srcdir}/gopath/src/github.com/GoogleContainerTools/${pkgname}"
}

build() {
  cd "${srcdir}/gopath/src/github.com/GoogleContainerTools/${pkgname}"
  GOPATH="${srcdir}/gopath" PATH="${PATH}:${GOPATH}/bin" VERSION="v${pkgver}" COMMIT="${_commit}" TREE_STATE="clean" make install
}

package() {
  install -Dm755 "${srcdir}/gopath/bin/${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
}
