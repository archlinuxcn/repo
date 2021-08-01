# Maintainer: larte <lauri.arte@gmail.com>
# Contributor: Maxwell Pray a.k.a. Synthead <synthead@gmail.com>
# Contributor: gun1x <gheorghe@linux.com>

pkgname=kubectl-bin
pkgdesc="Kubernetes.io client binary"
pkgver=1.21.3
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
sha256sums_i686=('78464d7d0775b1d6d0181316049e97769f2e06e0fa75215c85a4f915121191c3')
sha256sums_x86_64=('631246194fc1931cb897d61e1d542ef2321ec97adcb859a405d3b285ad9dd3d6')
sha256sums_aarch64=('2be58b5266faeeb93f38fa72d36add13a950643d2ae16a131f48f5a21c66ef23')
sha256sums_armv7h=('603b6e57c5546c079faee6b606014e83b95ea076146fbf73329f3069968f83bf')
sha256sums_armv7l=('603b6e57c5546c079faee6b606014e83b95ea076146fbf73329f3069968f83bf')

package() {
  install -Dm 755 "$srcdir/$_kubectl_file" "$pkgdir/usr/bin/kubectl"
  install -d 755 "$pkgdir/usr/share/bash-completion/completions"
  install -d 755 "$pkgdir/usr/share/zsh/site-functions"
  "$pkgdir/usr/bin/kubectl" completion bash > "$pkgdir/usr/share/bash-completion/completions/kubectl"
  "$pkgdir/usr/bin/kubectl" completion zsh >  "$pkgdir/usr/share/zsh/site-functions/_kubectl"
}
