# Maintainer: Sean E. Russell <ser@ser1.net>
# Contributor: Fabio 'Lolix' Loli <fabio.loli@disroot.org>

pkgname=gotop-bin
pkgver=3.5.3
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

package() {
  install -Dm755 "$srcdir/gotop" "$pkgdir/usr/bin/gotop"
}
sha256sums_x86_64=('a70b6838c91d20f31ff9d78a2cddd3cf995ffa792a40350f91624dee5c6f24b2')
sha256sums_i686=('02e293c4921d4305c320ce3ff7da75bab8fc2194234002bc36ba9fb71ae79bc7')
sha256sums_arm=('e09a1a3704562c5771236d2c7766bd1a2bfaa2967be0b054ff8550fce30c7302')
sha256sums_armv6h=('f7c40d664ef8248db732373193dd5eb4da1e960329e833e0b351a6613e78d098')
sha256sums_armv7h=('074a35728aec9d936277cf806d75919052d8d21a8f975280ab88e4ec46be02c8')
sha256sums_aarch64=('5d87879fbb680ff7a29195d938cbd72ff0f8d900e10963be8e875d3fe1352f99')
