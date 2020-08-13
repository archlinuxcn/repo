# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=1.4.0
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

sha256sums_x86_64=('86d63a493b4aa7226ae9536f257d5abb9c7389132744e17b838ef10d5e2218fa')
sha256sums_i686=('87dc33589833becbe5218276599eb331e6364583cf9323a9436ea5dbfb3a66e5')
sha256sums_arm=('14ab0ffd92239593efbb4ddbe021c3e77d8e7c544c48e37fa58ad3224c488b82')
sha256sums_armv6h=('14ab0ffd92239593efbb4ddbe021c3e77d8e7c544c48e37fa58ad3224c488b82')
sha256sums_aarch64=('14ab0ffd92239593efbb4ddbe021c3e77d8e7c544c48e37fa58ad3224c488b82')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
