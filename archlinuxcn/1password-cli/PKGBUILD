# Maintainer: Felix Seidel <felix@seidel.me>
# Maintainer: Claudia Pellegrino <aur@cpellegrino.de>
# Contributor: Liu Yuxuan <betsu@yahoo.com>

pkgname=1password-cli
pkgver=0.5.5
pkgrel=1
pkgdesc="1Password command line tool"
arch=('x86_64' 'i686' 'arm' 'armv6h')
url="https://app-updates.agilebits.com/product_history/CLI"
license=('custom')
options=('!strip' '!emptydirs')

source_x86_64=("https://cache.agilebits.com/dist/1P/op/pkg/v$pkgver/op_linux_amd64_v$pkgver.zip")
source_i686=("https://cache.agilebits.com/dist/1P/op/pkg/v$pkgver/op_linux_386_v$pkgver.zip")
source_arm=("https://cache.agilebits.com/dist/1P/op/pkg/v$pkgver/op_linux_arm_v$pkgver.zip")
source_armv6h=("${source_arm}")

sha256sums_x86_64=('143ef5ba96202137e22b06b781ef2617b1cb4b865c4752c5924f806222f71e05')
sha256sums_i686=('2d9c735cd5c3b4989a8a5058eb1e6c8a828b6754fc3f4b922fa30e983beb179f')
sha256sums_arm=('b741205653e6218d129b6c3fbd13583b9789f683dab6c9debfa56bf8cd54db4a')
sha256sums_armv6h=("${sha256sums_arm}")

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
