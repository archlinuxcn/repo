# Maintainer: Muhkoenig

pkgname=minikube-bin
pkgver=0.28.2
pkgrel=1
pkgdesc="Minikube is a tool that makes it easy to run Kubernetes locally"
url="https://github.com/kubernetes/minikube"
license=('Apache')
arch=('x86_64')
depends=(
  'net-tools'
)
optdepends=(
  'kubectl-bin: to manage the cluster'
  'virtualbox'
  'docker-machine-kvm'
)
makedepends=()
conflicts=('minikube')

source=(minikube_$pkgver::https://storage.googleapis.com/minikube/releases/v$pkgver/minikube-linux-amd64)
sha256sums=('3c84872ffa5ddbce472062fb548f9b3a25af72587d35243e12f18d86aaa6a085')
package() {
  cd "$srcdir"
  install -d "$pkgdir/usr/bin"
  install -m755 minikube_$pkgver "$pkgdir/usr/bin/minikube"
  install -d 755 "$pkgdir/usr/share/bash-completion/completions"
  install -d 755 "$pkgdir/usr/share/zsh/site-functions"
  "$pkgdir/usr/bin/minikube" completion bash > "$pkgdir/usr/share/bash-completion/completions/minikube"
  "$pkgdir/usr/bin/minikube" completion zsh >  "$pkgdir/usr/share/zsh/site-functions/_minikube"
}
