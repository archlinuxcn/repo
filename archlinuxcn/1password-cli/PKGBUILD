# Maintainer: Felix Seidel <felix@seidel.me>
# Maintainer: Claudia Pellegrino <aur@cpellegrino.de>
# Contributor: Liu Yuxuan <betsu@yahoo.com>

pkgname=1password-cli
pkgver=0.5.6_003
pkgrel=1
pkgdesc="1Password command line tool"
arch=('x86_64' 'i686' 'arm' 'armv6h')
url="https://app-updates.agilebits.com/product_history/CLI"
license=('custom')
options=('!strip' '!emptydirs')
_pkgver_upstream="${pkgver//_/-}"

source_x86_64=("https://cache.agilebits.com/dist/1P/op/pkg/v${_pkgver_upstream}/op_linux_amd64_v${_pkgver_upstream}.zip")
source_i686=("https://cache.agilebits.com/dist/1P/op/pkg/v${_pkgver_upstream}/op_linux_386_v${_pkgver_upstream}.zip")
source_arm=("https://cache.agilebits.com/dist/1P/op/pkg/v${_pkgver_upstream}/op_linux_arm_v${_pkgver_upstream}.zip")
source_armv6h=("${source_arm}")

sha256sums_x86_64=('c59890ed352ecb9b8f90c5ade339ce0738a591e0310b522d028e560aaeed9b89')
sha256sums_i686=('140c6ef6403bd92e17de9158cec37fd7aa12bac594f6811335797c525e36c990')
sha256sums_arm=('5501456c8205ad79b8efe2e9d47612ad06b6e2ed6bc901e66d0f7933a6b7716d')
sha256sums_armv6h=("${sha256sums_arm}")

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
