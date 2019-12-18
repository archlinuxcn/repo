# Maintainer: Lukas Grossar <lukas.grossar@gmail.com>
# Contributor: Ivan Shapovalov <intelfx@intelfx.name>
# Contributor: Wayne Cheng <waynethecheng@gmail.com>

pkgname=kubernetes-helm
pkgver=3.0.2
pkgrel=1
pkgdesc="A tool to manage Kubernetes charts"
arch=('i686' 'x86_64' 'arm' 'aarch64')
url="https://github.com/helm/helm"
makedepends=('git' 'go')
depends=('socat')
optdepends=(
  'kubectl: check cluster status'
  'kubectl-bin: check cluster status - binary package'
)
provides=(kubernetes-helm)
conflicts=(
  'kubernetes-helm-bin'
  'kubernetes-helm'
  'kubernetes-helm-git'
)
license=('Apache')
source=("git+https://github.com/helm/helm#tag=v${pkgver}")
md5sums=('SKIP')

build() {
  cd "$srcdir/helm"
  make build
}

package() {
  install -Dm755 "$srcdir/helm/bin/helm" -t "$pkgdir/usr/bin"

  "$pkgdir/usr/bin/helm" completion bash | install -Dm644 /dev/stdin "$pkgdir/usr/share/bash-completion/completions/helm"
  "$pkgdir/usr/bin/helm" completion zsh | install -Dm644 /dev/stdin "$pkgdir/usr/share/zsh/site-functions/_helm"
}
