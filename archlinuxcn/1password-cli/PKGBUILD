# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=0.9.2
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

sha256sums_x86_64=('f0c90be124c59ea141179794f0846689ac6b2354c805cd0b5ecd73456358733b')
sha256sums_i686=('fc990a1986fab61c6624c2d6d6f37a6492dc61fab7e63e0f2b93fb7b071696d2')
sha256sums_arm=('998e91b64117308d25d911ddf924ec3193dcaa39b8a2b539b77087d7a1a63e61')
sha256sums_armv6h=('998e91b64117308d25d911ddf924ec3193dcaa39b8a2b539b77087d7a1a63e61')
sha256sums_aarch64=('998e91b64117308d25d911ddf924ec3193dcaa39b8a2b539b77087d7a1a63e61')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
