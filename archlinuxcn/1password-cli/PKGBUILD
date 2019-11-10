# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=0.8.0
pkgrel=1
pkgdesc="1Password command line tool"
arch=('x86_64' 'i686' 'arm' 'armv6h')
url="https://app-updates.agilebits.com/product_history/CLI"
license=('custom')
options=('!strip' '!emptydirs')

source_x86_64=("https://cache.agilebits.com/dist/1P/op/pkg/v${pkgver}/op_linux_amd64_v${pkgver}.zip")
source_i686=("https://cache.agilebits.com/dist/1P/op/pkg/v${pkgver}/op_linux_386_v${pkgver}.zip")
source_arm=("https://cache.agilebits.com/dist/1P/op/pkg/v${pkgver}/op_linux_arm_v${pkgver}.zip")
source_armv6h=("${source_arm}")

sha256sums_x86_64=('29b70379db8c4787e491ab127422acb183267916b989eee81631e08b10742c0a')
sha256sums_i686=('d49918bfdb35d7bc23c53ff7e6caacabe3aaf2ad294c8e673446dab43b042a34')
sha256sums_arm=('5aa42870cac5941491844e6382c88ad711ef029832b8e8234e2688b5ab8cdbd1')
sha256sums_armv6h=('5aa42870cac5941491844e6382c88ad711ef029832b8e8234e2688b5ab8cdbd1')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
