# Maintainer: George Raven <GeorgeRavenCommunity PLUS kubeadmbin AT pm DOT me>
# Contributor: larte <lauri.arte@gmail.com>
# Contributor: Maxwell Pray a.k.a. Synthead <synthead@gmail.com>
# Contributor: gun1x <gheorghe@linux.com>


pkgname=kubectl-bin
pkgdesc="Kubernetes.io kubectl binary"
pkgver=1.31.3 # renovate: datasource=github-tags depName=kubernetes/kubernetes
pkgrel=1
arch=('x86_64' 'armv7l' 'armv7h' 'aarch64')
url="http://kubernetes.io"
license=('apache')
depends=()
conflicts=('kubectl')
provides=('kubectl')
source=()
b2sums=('86592fbabe3d37436f9cd2d6ab9e31ce4183329258f57455f2436347bc3f15391953c2e97292585e9e4149cf5bb677beeb29b3b0a1ab94a20075c38e6dfaf13f')

# if CARCH is not set default to x86_64
# https://stackoverflow.com/a/11362364/11164973
: "${CARCH:=x86_64}"

case "$CARCH" in
  x86_64) _pkgarch="amd64"
    ;;
  arm*) _pkgarch="arm"
    ;;
  aarch64) _pkgarch="arm64"
    ;;
esac

source+=(${pkgname}-${pkgver}-${_pkgarch}::"https://dl.k8s.io/release/v${pkgver}/bin/linux/${_pkgarch}/kubectl")

package() {
  # Kubectl Binary
  install -D -m 0755 "${pkgname}-${pkgver}-${_pkgarch}" "${pkgdir}/usr/bin/kubectl"
  # Shell Completions
  mkdir -p completions
  ${pkgdir}/usr/bin/kubectl completion bash > completions/kubectl
  ${pkgdir}/usr/bin/kubectl completion zsh  > completions/_kubectl
  ${pkgdir}/usr/bin/kubectl completion fish > completions/kubectl.fish
  install -D -m 0644 completions/kubectl ${pkgdir}/usr/share/bash-completion/completions/kubectl
  install -D -m 0644 completions/_kubectl ${pkgdir}/usr/share/zsh/site-functions/_kubectl
  install -D -m 0644 completions/kubectl.fish ${pkgdir}/usr/share/fish/vendor_completions.d/kubectl.fish
}
