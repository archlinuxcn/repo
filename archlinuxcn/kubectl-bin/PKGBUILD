# Maintainer: larte <lauri.arte@gmail.com>
# Contributor: Maxwell Pray a.k.a. Synthead <synthead@gmail.com>
# Contributor: gun1x <gheorghe@linux.com>

pkgname=kubectl-bin
pkgdesc="Kubernetes.io client binary"
pkgver=1.22.0
pkgrel=1
arch=('i686' 'x86_64' 'aarch64' 'armv7h' 'armv7l')
url="https://kubernetes.io"
license=('apache')
conflicts=('kubectl' 'kubernetes>=1.4.6')
provides=('kubectl=$pkgver')
_kubectl_file=kubectl-$pkgver
source_i686=($_kubectl_file::https://storage.googleapis.com/kubernetes-release/release/v$pkgver/bin/linux/386/kubectl)
source_x86_64=($_kubectl_file::https://storage.googleapis.com/kubernetes-release/release/v$pkgver/bin/linux/amd64/kubectl)
source_aarch64=($_kubectl_file::https://storage.googleapis.com/kubernetes-release/release/v$pkgver/bin/linux/arm64/kubectl)
source_armv7h=($_kubectl_file::https://storage.googleapis.com/kubernetes-release/release/v$pkgver/bin/linux/arm/kubectl)
source_armv7l=($_kubectl_file::https://storage.googleapis.com/kubernetes-release/release/v$pkgver/bin/linux/arm/kubectl)
sha256sums_i686=('0c3a2e73dec76d75667c23215e6ef3518ecb1fcbc285bb8e079e6ef4d5a40d49')
sha256sums_x86_64=('703e70d49b82271535bc66bc7bd469a58c11d47f188889bd37101c9772f14fa1')
sha256sums_aarch64=('8d9cc92dcc942f5ea2b2fc93c4934875d9e0e8ddecbde24c7d4c4e092cfc7afc')
sha256sums_armv7h=('6d7c787416a148acffd49746837df4cebb1311c652483dc3d2c8d24ce1cc897e')
sha256sums_armv7l=('6d7c787416a148acffd49746837df4cebb1311c652483dc3d2c8d24ce1cc897e')

package() {
  install -Dm 755 "$srcdir/$_kubectl_file" "$pkgdir/usr/bin/kubectl"
  install -d 755 "$pkgdir/usr/share/bash-completion/completions"
  install -d 755 "$pkgdir/usr/share/zsh/site-functions"
  "$pkgdir/usr/bin/kubectl" completion bash > "$pkgdir/usr/share/bash-completion/completions/kubectl"
  "$pkgdir/usr/bin/kubectl" completion zsh >  "$pkgdir/usr/share/zsh/site-functions/_kubectl"
}
