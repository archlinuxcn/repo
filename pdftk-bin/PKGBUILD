# Maintainer: Florian Bruhin (The Compiler) <archlinux.org@the-compiler.org>
# Contributor: Yannik Stein <yannik.stein [at] gmail.com>
# Contributor: Dan Serban
# Contributor: flying-sheep
# Contributor: Liu Chang <goduck777@gmail.com>

pkgname=pdftk-bin
pkgver=2.02_3
pkgrel=2
pkgdesc="Swiss army knife for PDFs. Built from binary executables available in Debian repositories."
url=http://www.pdfhacks.com/pdftk
arch=(i686 x86_64)
license=(GPL)
depends=(libgcj15-bin gcc-libs)
provides=(pdftk)
conflicts=(pdftk pdfchain-all-inclusive)

source_i686=(http://httpredir.debian.org/debian/pool/main/p/pdftk/pdftk_${pkgver//_/-}_i386.deb)
source_x86_64=(http://httpredir.debian.org/debian/pool/main/p/pdftk/pdftk_${pkgver//_/-}_amd64.deb)

sha1sums_i686=('c6fb143ea725dc60bdab95c02abf2c02090b1b43')
sha1sums_x86_64=('db1117f58d5f225fb3ecc313086f9184c23ca94b')

package() {
  tar -xf data.tar.?z -C "$pkgdir" ./usr
}

# vim:set ts=2 sw=2 ft=sh et:
