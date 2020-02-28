# Maintainer: Sean E. Russell <ser@ser1.net>
# Contributor: Fabio 'Lolix' Loli <fabio.loli@disroot.org>

pkgname=gotop-bin
pkgver=3.3.2
pkgrel=1
pkgdesc="A terminal based graphical activity monitor inspired by gtop and vtop"
arch=(x86_64 i686 arm armv6h armv7h aarch64)
url="https://github.com/xxxserxxx/gotop"
license=("AGPL3")
provides=("gotop")
conflicts=("gotop")
source_x86_64=("https://github.com/xxxserxxx/gotop/releases/download/v$pkgver/gotop_${pkgver}_linux_amd64.tgz")
source_i686=("https://github.com/xxxserxxx/gotop/releases/download/v$pkgver/gotop_${pkgver}_linux_386.tgz")
source_arm=("https://github.com/xxxserxxx/gotop/releases/download/v$pkgver/gotop_${pkgver}_linux_arm_v5.tgz")
source_armv6h=("https://github.com/xxxserxxx/gotop/releases/download/v$pkgver/gotop_${pkgver}_linux_arm_v6.tgz")
source_armv7h=("https://github.com/xxxserxxx/gotop/releases/download/v$pkgver/gotop_${pkgver}_linux_arm_v7.tgz")
source_aarch64=("https://github.com/xxxserxxx/gotop/releases/download/v$pkgver/gotop_${pkgver}_linux_arm64.tgz")
sha256sums_x86_64=('768766ed3a366f48412498314bbe1b341629dde09de18121f787b52d5f52775b')
sha256sums_i686=('51cd6fd3dc68c64881e6484d7019044ac743e9d24a6c604934a4e1bff5814c2a')
sha256sums_arm=('7bbeef4ade43366f9295e95f84856533a878c198353369ad9ab2bfd0ec172969')
sha256sums_armv6h=('5aa81644698143e073efabf5c4e5b7127593f6f31007864d1a6bbee3a50e6310')
sha256sums_armv7h=('0cf5ff900043157a0f9f0bcd781a6a2a34c2574903ab2fa9bd0b46f7b5387f8f')
sha256sums_aarch64=('c35dda56d49ea785b596952d1ea9f1102366c97d05fbb1cf2087709f27a25839')

package() {
  install -Dm755 "$srcdir/gotop" "$pkgdir/usr/bin/gotop"
}
