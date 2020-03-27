# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=0.9.4
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

sha256sums_x86_64=('02ecf34ea840552926d3273bcf07f08658c3c5481e8f1630b48eb7c841f4ed8b')
sha256sums_i686=('1f05c745612a5bee822a421f59503ca0b18b03902ff10a4c2f9fe18c089c8269')
sha256sums_arm=('41b69bc5b3146039c7b2fd6672a7bbf5fda825f394353de00e5e3eec5c233f82')
sha256sums_armv6h=('41b69bc5b3146039c7b2fd6672a7bbf5fda825f394353de00e5e3eec5c233f82')
sha256sums_aarch64=('41b69bc5b3146039c7b2fd6672a7bbf5fda825f394353de00e5e3eec5c233f82')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
