# Maintainer: fuero <fuerob@gmail.com>
pkgname=shef
# renovate: datasource=github-releases depName=eduardoagarcia/shef
pkgver=0.3.2
pkgrel=1
pkgdesc='directory and filename linter'
arch=('x86_64')
_repo_prefix='github.com/eduardoagarcia'
_repo_name="${pkgname%-git}"
url="https://${_repo_prefix}/${_repo_name}"
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('47ade6be39885936d68db155bef8989b2e58628b5c4ad3e9fe4ce16f2a7134aa')
license=('MIT')
depends=('glibc')
makedepends=('go-pie')
conflicts=("${_repo_name}-git")
provides=("${_repo_name}")

clean() {
  echo rm -rf ${srcdir}
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  go build -x -v \
    -ldflags "-extldflags '${LDFLAGS}' -X main.commit=$(git rev-parse --short HEAD) -X main.date=$(date -u +%Y%m%d.%H%M%S) -X main.version=${version}" \
    -o "${_repo_name}.bin" \
    .
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -Dm0755 "${_repo_name}.bin" "${pkgdir}/usr/bin/${_repo_name}"
  for _file in *.md
  do
    install -Dm644 "${_file}" "${pkgdir}/usr/share/doc/${pkgname}/$(basename ${_file})"
  done
}
