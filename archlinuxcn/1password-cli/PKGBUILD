# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=1.5.0
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

sha256sums_x86_64=('1acb66e8e8aa9af87f28a59b19a05a9c053001c9a3872c7775f4cc07c872ee3b')
sha256sums_i686=('68b4303b56ffc4a5139f67a66e3104cf78e2d84e2f97d125a85abda700bd91cf')
sha256sums_arm=('8fd803feb012332e6db1f542077a0a5976e52e94e3476f5c1b93cb625ffb6d25')
sha256sums_armv6h=('8fd803feb012332e6db1f542077a0a5976e52e94e3476f5c1b93cb625ffb6d25')
sha256sums_aarch64=('8fd803feb012332e6db1f542077a0a5976e52e94e3476f5c1b93cb625ffb6d25')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
