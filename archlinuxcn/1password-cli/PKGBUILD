# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=1.2.1
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

sha256sums_x86_64=('17a8d6367c318d55e20f1dd4e841745fee8c7f6dbd79481ea1b667540bf56fe9')
sha256sums_i686=('ca32e7fd93e5577edf447fe4ae596eb5e587911ab8fcb08c4083770ac09b1d75')
sha256sums_arm=('b606727c26b1f262bcdf551a25db42c9359c125aef985db3c764ca66263aecc3')
sha256sums_armv6h=('b606727c26b1f262bcdf551a25db42c9359c125aef985db3c764ca66263aecc3')
sha256sums_aarch64=('b606727c26b1f262bcdf551a25db42c9359c125aef985db3c764ca66263aecc3')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
