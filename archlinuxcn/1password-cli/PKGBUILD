# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=0.7.1
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

sha256sums_x86_64=('643ddee704c69a9361752e7239426333a60cd1a8b64781f43e1d931eee6873e2')
sha256sums_i686=('ef55cf13fa55bbc3aa7d7d42ea4d3d391ef3fe00f8a112d0f040570b86d88afb')
sha256sums_arm=('7200d77acd475d6b6cc0e3b0e22794cca5850d2b795a33676edbbd0cdfb56130')
sha256sums_armv6h=('7200d77acd475d6b6cc0e3b0e22794cca5850d2b795a33676edbbd0cdfb56130')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
