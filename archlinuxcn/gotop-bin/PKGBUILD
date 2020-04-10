# Maintainer: Sean E. Russell <ser@ser1.net>
# Contributor: Fabio 'Lolix' Loli <fabio.loli@disroot.org>

pkgname=gotop-bin
pkgver=3.5.1
pkgrel=1
pkgdesc="A terminal based graphical activity monitor inspired by gtop and vtop"
arch=(x86_64 i686 arm armv6h armv7h aarch64)
url="https://github.com/xxxserxxx/gotop"
license=("AGPL3")
provides=("gotop")
conflicts=("gotop")
depends=("glibc")
source_x86_64=("https://github.com/xxxserxxx/gotop/releases/download/v$pkgver/gotop_v${pkgver}_linux_amd64.tgz")
source_i686=("https://github.com/xxxserxxx/gotop/releases/download/v$pkgver/gotop_v${pkgver}_linux_386.tgz")
source_arm=("https://github.com/xxxserxxx/gotop/releases/download/v$pkgver/gotop_v${pkgver}_linux_arm5.tgz")
source_armv6h=("https://github.com/xxxserxxx/gotop/releases/download/v$pkgver/gotop_v${pkgver}_linux_arm6.tgz")
source_armv7h=("https://github.com/xxxserxxx/gotop/releases/download/v$pkgver/gotop_v${pkgver}_linux_arm7.tgz")
source_aarch64=("https://github.com/xxxserxxx/gotop/releases/download/v$pkgver/gotop_v${pkgver}_linux_arm64.tgz")
sha256sums_x86_64=('bd6dff0d946b0c0bb146ad95130a4fd2471fd5dc9aa2099573913f797349a6ac')
sha256sums_i686=('eb5837a89f110a74eb357fc4a7ae4ba2114d26e508fa293349562654e258ef07')
sha256sums_arm=('2dbc2188efd42e75c2349c41ee19863653168585f4a13af96bf6665c844046ed')
sha256sums_armv6h=('ff9577f01b42a95b86a8b23c3d7ecc62f595df97a7f6bb295b2b75c69cf64085')
sha256sums_armv7h=('1ccab85046993ec5044d525462e626a620b74cc2c3094850efb1672702e3fa33')
sha256sums_aarch64=('980d1468ec473f9b7130da6ce4f67090ea6b2cfeeae1bf5f392b1cca265e1b48')

package() {
  install -Dm755 "$srcdir/gotop" "$pkgdir/usr/bin/gotop"
}
