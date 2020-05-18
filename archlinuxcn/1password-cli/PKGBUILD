# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=0.10.0
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

sha256sums_x86_64=('f1e8f371958d3b12dbefb85a41ce7cac411c9830964d0c7cbf8d2315ad55a836')
sha256sums_i686=('1f10d7d8b6f6330728c851c5099413863c9fba22c50aa80bacbe4f30a27b2d53')
sha256sums_arm=('b1d63015f5cd9a8f944fbfeb6af472c95041f48c5ea3d0524607f7476fb2c535')
sha256sums_armv6h=('b1d63015f5cd9a8f944fbfeb6af472c95041f48c5ea3d0524607f7476fb2c535')
sha256sums_aarch64=('b1d63015f5cd9a8f944fbfeb6af472c95041f48c5ea3d0524607f7476fb2c535')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
