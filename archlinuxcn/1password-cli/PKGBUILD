# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=0.9.3
pkgrel=1
pkgdesc="1Password command line tool"
arch=('x86_64' 'i686' 'arm' 'armv6h' 'aarch64')
url="https://app-updates.agilebits.com/product_history/CLI"
license=('custom')
options=('!strip' '!emptydirs')

source_x86_64=("https://cache.agilebits.com/dist/1P/op/pkg/v${pkgver}/op_linux_amd64_v${pkgver}.zip")
source_i686=("https://cache.agilebits.com/dist/1P/op/pkg/v${pkgver}/op_linux_386_v${pkgver}.zip")
source_arm=("https://cache.agilebits.com/dist/1P/op/pkg/v${pkgver}/op_linux_arm_v${pkgver}.zip")
source_armv6h=("${source_arm}")
source_aarch64=("${source_arm}")

sha256sums_x86_64=('0277ad08817ab4c63d46edcc66127202ff524726830ebd6cb93b98df294b1f88')
sha256sums_i686=('f3e158484846cd36984cb78b0a0fa7deadba2620ff11af55ba18e25d77a8c837')
sha256sums_arm=('c7a5e3223b19a3f7fc05adfe7def8f6b004f9a73ab591c5fbcf7997f2569ed2a')
sha256sums_armv6h=('c7a5e3223b19a3f7fc05adfe7def8f6b004f9a73ab591c5fbcf7997f2569ed2a')
sha256sums_aarch64=('c7a5e3223b19a3f7fc05adfe7def8f6b004f9a73ab591c5fbcf7997f2569ed2a')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
