# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=1.1.0
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

sha256sums_x86_64=('73b4756f61385f19a5db79d925ca747178702a3f1c6fdf4d2166cffc98790281')
sha256sums_i686=('9a55f7ee6b271f8c6d6e0db6dc91da1fcc5efa0bb27eb0029e408fe73c3b9cd6')
sha256sums_arm=('d25b682d1ec584c8fe0e13451d3d9bcf5e8a650679e32b2f5dea2d45823adf17')
sha256sums_armv6h=('d25b682d1ec584c8fe0e13451d3d9bcf5e8a650679e32b2f5dea2d45823adf17')
sha256sums_aarch64=('d25b682d1ec584c8fe0e13451d3d9bcf5e8a650679e32b2f5dea2d45823adf17')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
