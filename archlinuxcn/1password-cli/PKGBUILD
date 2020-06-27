# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=1.1.1
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

sha256sums_x86_64=('b612b11ef0c21a62c71f2ce4a21c6621784837ce6f59ca264eb377efcddc4f8e')
sha256sums_i686=('8f107bc03a2bfa56acb7076594668d24c3b4b0624367cf9749b624f85f6b3fe9')
sha256sums_arm=('5721d6791c960539f31844c3de0e5769e8731535296ebdbde51540eca2e87848')
sha256sums_armv6h=('5721d6791c960539f31844c3de0e5769e8731535296ebdbde51540eca2e87848')
sha256sums_aarch64=('5721d6791c960539f31844c3de0e5769e8731535296ebdbde51540eca2e87848')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
