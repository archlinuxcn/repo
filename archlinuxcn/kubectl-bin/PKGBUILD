# Maintainer: George Raven <GeorgeRavenCommunity PLUS kubeadmbin AT pm DOT me>
# Contributor: larte <lauri.arte@gmail.com>
# Contributor: Maxwell Pray a.k.a. Synthead <synthead@gmail.com>
# Contributor: gun1x <gheorghe@linux.com>


pkgname=kubectl-bin
pkgdesc="Kubernetes.io kubectl binary"
pkgver=1.27.3
pkgrel=1
arch=('x86_64' 'armv7l' 'armv7h' 'aarch64')
url="http://kubernetes.io"
license=('apache')
depends=()
conflicts=('kubectl')
provides=('kubectl')
source=()
b2sums=()

case "$CARCH" in
  x86_64) _pkgarch="amd64"
    b2sums+=('f3cb667688d79ee22491b96258e09e97b0a6e707eb8640fc3a3304a62605e5a83d017b91f67e1d028e838d268b312b9f7eade3f57a5134499c0e8eeaf298cba0')
    ;;
  arm*) _pkgarch="arm"
    b2sums+=('c55eeda6b2e6e8f9aff1ccbabaf346fcc5ae020a1c55d8139ed84475cb7e2020695b4e236b14469d2b827887f94507f87fdc69d1463172a3b044c2214b0c5e43')
    ;;
  aarch64) _pkgarch="arm64"
    b2sums+=('c43bdb34d8d765e9d463baadc477e80f29a92ec9c94eee9ac3a0466dc5c0ca5c127da9ae3b80b8655cb1b8de8cd72d61654d276e64f8fef2103934deca74ce1f')
    ;;
esac

source+=(${pkgname}-${pkgver}-${_pkgarch}::"https://storage.googleapis.com/kubernetes-release/release/v${pkgver}/bin/linux/${_pkgarch}/kubectl")

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
