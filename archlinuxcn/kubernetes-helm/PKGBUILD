# Maintainer: Lukas Grossar <lukas.grossar@gmail.com>
# Contributor: Ivan Shapovalov <intelfx@intelfx.name>
# Contributor: Wayne Cheng <waynethecheng@gmail.com>
# Contributor: Matthias Lisin <ml@visu.li>

pkgname=kubernetes-helm
pkgver=3.1.1
_commit=afe70585407b420d0097d07b21c47dc511525ac8
pkgrel=5
pkgdesc="A tool to manage Kubernetes charts"
arch=('i686' 'x86_64' 'arm' 'aarch64')
url="https://github.com/helm/helm"
depends=('glibc')
makedepends=('go' 'git')
conflicts=('helm' 'kubernetes-helm')
license=('Apache')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/helm/helm/archive/v${pkgver}.tar.gz")
sha256sums=('d3e4920f58ceec28bb3916e0c453427273f63db701a354701663cc149e63ea28')

build() {
  cd "$srcdir/helm-${pkgver}"
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
