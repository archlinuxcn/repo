# Maintainer: Florian Bruhin (The Compiler) <archlinux.org@the-compiler.org>
# Contributor: Yannik Stein <yannik.stein [at] gmail.com>
# Contributor: Dan Serban
# Contributor: flying-sheep
# Contributor: Liu Chang <goduck777@gmail.com>

pkgname=pdftk-bin
pkgver=2.02_4
pkgrel=1
pkgdesc="Swiss army knife for PDFs. Built from binary executables available in Debian repositories."
url=http://www.pdfhacks.com/pdftk
arch=(i686 x86_64)
license=(GPL)
depends=(libgcj16-bin gcc-libs)
provides=(pdftk)
conflicts=(pdftk pdfchain-all-inclusive)

source_i686=(http://httpredir.debian.org/debian/pool/main/p/pdftk/pdftk_${pkgver//_/-}_i386.deb)
source_x86_64=(http://httpredir.debian.org/debian/pool/main/p/pdftk/pdftk_${pkgver//_/-}_amd64.deb)

sha1sums_i686=('0c9885996538aafddd509d0c32fc53410481a745')
sha1sums_x86_64=('9fdfec85140d544613209cf85cb99b1a5d5c6349')

package() {
  tar -xf data.tar.?z -C "$pkgdir" ./usr
}

# vim:set ts=2 sw=2 ft=sh et:
