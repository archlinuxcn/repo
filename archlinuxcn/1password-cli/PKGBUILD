# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=1.3.0
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

sha256sums_x86_64=('75c83f16d0d6c5c4c76e3b49116cbbcdabfbbbfb4910dbd15ac0126111b70a37')
sha256sums_i686=('2c9b2ac4b7449e21764f8b8f84b7ed809e3abdc9273a52f73c5ec1b811ae125b')
sha256sums_arm=('36220aa82e6b8ce014cb1dcf6dff20285273ba2ab848ba43a8a9252f3b4c9c49')
sha256sums_armv6h=('36220aa82e6b8ce014cb1dcf6dff20285273ba2ab848ba43a8a9252f3b4c9c49')
sha256sums_aarch64=('36220aa82e6b8ce014cb1dcf6dff20285273ba2ab848ba43a8a9252f3b4c9c49')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
