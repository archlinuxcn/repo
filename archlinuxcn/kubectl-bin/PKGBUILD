# Maintainer: larte <lauri.arte@gmail.com>
# Contributor: Maxwell Pray a.k.a. Synthead <synthead@gmail.com>
# Contributor: gun1x <gheorghe@linux.com>

pkgname=kubectl-bin
pkgdesc="Kubernetes.io client binary"
pkgver=1.19.4
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
sha256sums_i686=('c22e52c583422be3203cfa4e06e9b68bcc1546e3316f895be69793d9a6de8bf6')
sha256sums_x86_64=('7df333f1fc1207d600139fe8196688303d05fbbc6836577808cda8fe1e3ea63f')
sha256sums_aarch64=('334ca7ce181d8b83e100b1ad4347af93bee6f261d792e9f52d9769095e970919')
sha256sums_armv7h=('4ca2dc66fb5ea5f71afbb1f769e7eae237da4c9287c875da935a6b9f15619112')
sha256sums_armv7l=('4ca2dc66fb5ea5f71afbb1f769e7eae237da4c9287c875da935a6b9f15619112')

package() {
  install -Dm 755 "$srcdir/$_kubectl_file" "$pkgdir/usr/bin/kubectl"
  install -d 755 "$pkgdir/usr/share/bash-completion/completions"
  install -d 755 "$pkgdir/usr/share/zsh/site-functions"
  "$pkgdir/usr/bin/kubectl" completion bash > "$pkgdir/usr/share/bash-completion/completions/kubectl"
  "$pkgdir/usr/bin/kubectl" completion zsh >  "$pkgdir/usr/share/zsh/site-functions/_kubectl"
}
