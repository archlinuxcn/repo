# Maintainer: slurpee <aur@lylat.io>
# Contributors: Felix Seidel, Claudia Pellegrino, Liu Yuxuan

pkgname=1password-cli
pkgver=1.6.0
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

sha256sums_x86_64=('4f95ce6b0f9a727ab90d1de6b6f01020b3102789fb0acecb63e27b6f02270687')
sha256sums_i686=('1c844d7577d8e51df3c079b3a1c6cb439782166dc8f8b7b71f210a06df239787')
sha256sums_arm=('a42aa22490381b3c70e653d58d5fa44002c736e464780d8a31c82623bb3dbf73')
sha256sums_armv6h=('a42aa22490381b3c70e653d58d5fa44002c736e464780d8a31c82623bb3dbf73')
sha256sums_aarch64=('a42aa22490381b3c70e653d58d5fa44002c736e464780d8a31c82623bb3dbf73')

check() {
  if (( ! SKIPPGPCHECK )); then
    gpg --verify-files ${srcdir}/op.sig
  fi
}

package() {
  install -Dm755 op "$pkgdir/usr/bin/op"
}

# vim:set ts=2 sw=2 et:
