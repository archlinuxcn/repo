# Maintainer: larte <lauri.arte@gmail.com>
# Contributor: Maxwell Pray a.k.a. Synthead <synthead@gmail.com>
# Contributor: gun1x <gheorghe@linux.com>

pkgname=kubectl-bin
pkgdesc="Kubernetes.io client binary"
pkgver=1.20.2
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
sha256sums_i686=('6e9824c2978b799c3b3b8a84e38085d98bf78e4ddce4526432a10c633ee1c26a')
sha256sums_x86_64=('2583b1c9fbfc5443a722fb04cf0cc83df18e45880a2cf1f6b52d9f595c5beb88')
sha256sums_aarch64=('37fdba9fcd43cafba11ac4f82692e41aca41b59f44fd968fd84c263d71af580f')
sha256sums_armv7h=('a8d5b7e974200ae94a0eb3873773ec4ceffa99283f1843960d0a1b4448c2aa42')
sha256sums_armv7l=('a8d5b7e974200ae94a0eb3873773ec4ceffa99283f1843960d0a1b4448c2aa42')

package() {
  install -Dm 755 "$srcdir/$_kubectl_file" "$pkgdir/usr/bin/kubectl"
  install -d 755 "$pkgdir/usr/share/bash-completion/completions"
  install -d 755 "$pkgdir/usr/share/zsh/site-functions"
  "$pkgdir/usr/bin/kubectl" completion bash > "$pkgdir/usr/share/bash-completion/completions/kubectl"
  "$pkgdir/usr/bin/kubectl" completion zsh >  "$pkgdir/usr/share/zsh/site-functions/_kubectl"
}
