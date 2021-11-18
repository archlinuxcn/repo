# Maintainer: larte <lauri.arte@gmail.com>
# Contributor: Maxwell Pray a.k.a. Synthead <synthead@gmail.com>
# Contributor: gun1x <gheorghe@linux.com>

pkgname=kubectl-bin
pkgdesc="Kubernetes.io client binary"
pkgver=1.22.4
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
sha256sums_i686=('5aa1cb3c622479275ca4ec573bce7eb45bdec430b22efeec3a7e98a714bc2678')
sha256sums_x86_64=('21f24aa723002353eba1cc2668d0be22651f9063f444fd01626dce2b6e1c568c')
sha256sums_aarch64=('3fcec0284c0fdfc22e89a5b73ebd7f51120cc3505a11a4f6d6f819d46a40b26a')
sha256sums_armv7h=('9ea171e868aeb64b187a039edd79b2c7ea2bedbd752c76e1c5e44c2486d21f72')
sha256sums_armv7l=('9ea171e868aeb64b187a039edd79b2c7ea2bedbd752c76e1c5e44c2486d21f72')

package() {
  install -Dm 755 "$srcdir/$_kubectl_file" "$pkgdir/usr/bin/kubectl"
  install -d 755 "$pkgdir/usr/share/bash-completion/completions"
  install -d 755 "$pkgdir/usr/share/zsh/site-functions"
  "$pkgdir/usr/bin/kubectl" completion bash > "$pkgdir/usr/share/bash-completion/completions/kubectl"
  "$pkgdir/usr/bin/kubectl" completion zsh >  "$pkgdir/usr/share/zsh/site-functions/_kubectl"
}
