# Maintainer: Lukas Grossar <lukas.grossar@gmail.com>
# Contributor: Ivan Shapovalov <intelfx@intelfx.name>
# Contributor: Wayne Cheng <waynethecheng@gmail.com>
# Contributor: Matthias Lisin <ml@visu.li>

pkgname=kubernetes-helm
pkgver=3.1.2
_commit=d878d4d45863e42fd5cff6743294a11d28a9abce
pkgrel=2
pkgdesc="A tool to manage Kubernetes charts"
arch=('i686' 'x86_64' 'arm' 'aarch64')
url="https://github.com/helm/helm"
depends=('glibc')
makedepends=('go' 'git')
license=('Apache')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/helm/helm/archive/v${pkgver}.tar.gz")
sha256sums=('06c7a43be1841b07c4737999d90c1d194b80b55c6d80829349121e8e95f4a1e1')

build() {
  cd helm-${pkgver}
  go build -o bin/helm \
    -buildmode=pie \
    -trimpath \
    -ldflags "\
      -X 'helm.sh/helm/v3/internal/version.version=v${pkgver}' \
      -X 'helm.sh/helm/v3/internal/version.gitCommit=${_commit}' \
      -X 'helm.sh/helm/v3/internal/version.gitTreeState=clean' \
      -extldflags ${LDFLAGS}" \
    ./cmd/helm
}

package() {
  install -Dm755 "$srcdir/helm-${pkgver}/bin/helm" -t "$pkgdir/usr/bin"

  "$pkgdir/usr/bin/helm" completion bash | install -Dm644 /dev/stdin "$pkgdir/usr/share/bash-completion/completions/helm"
  "$pkgdir/usr/bin/helm" completion zsh | install -Dm644 /dev/stdin "$pkgdir/usr/share/zsh/site-functions/_helm"
}
