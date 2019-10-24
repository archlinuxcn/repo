# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=0.7.0
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

sha256sums_x86_64=('770ccaf2ea3ba0cb87e32aa1f47f26567058f03d9ec4525e271e51160ee57b7c')
sha256sums_i686=('a5c0b6e07734984ae31b803163b3f0c8cf4b564a736c60a4f7fdfb011a807e1e')
sha256sums_arm=('783b30f6cbed821f6f59e58d1f0a7b2811cb6e89edca9d665c9b1270cbdd3398')
sha256sums_armv6h=('783b30f6cbed821f6f59e58d1f0a7b2811cb6e89edca9d665c9b1270cbdd3398')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
