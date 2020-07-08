# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=1.2.0
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

sha256sums_x86_64=('4802361ab0cfeea4fcd37e1af102a4964d5c953fc3d136cadb3ed9f483fc0f1a')
sha256sums_i686=('9dc356b6bfaa2d6636c79b4e40edebbc457b058390aff5a625a721c506f3fd03')
sha256sums_arm=('e3f0710a7688dd455a6e6e7f7a60ba1dec2ff98ad436d3e8fa0e065ea6777ebd')
sha256sums_armv6h=('e3f0710a7688dd455a6e6e7f7a60ba1dec2ff98ad436d3e8fa0e065ea6777ebd')
sha256sums_aarch64=('e3f0710a7688dd455a6e6e7f7a60ba1dec2ff98ad436d3e8fa0e065ea6777ebd')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
