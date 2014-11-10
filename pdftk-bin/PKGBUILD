# Maintainer: Florian Bruhin (The Compiler) <archlinux.org@the-compiler.org>
# Contributor: Yannik Stein <yannik.stein [at] gmail.com>
# Contributor: Dan Serban
# Contributor: flying-sheep
# Contributor: Liu Chang <goduck777@gmail.com>

pkgname=pdftk-bin
pkgver=2.02_2
pkgrel=1
pkgdesc="Swiss army knife for PDFs. Built from binary executables available in Debian repositories."
url=http://www.pdfhacks.com/pdftk
arch=(i686 x86_64)
license=(GPL)
depends=(libgcj gcc-libs)
provides=(pdftk)
conflicts=(pdftk pdfchain-all-inclusive)

if [[ $CARCH == i686 ]]; then
  _debarch=i386
  sha512sums=('44c2b700a39368a1f6f4c2e7bd2e33af718794ddcffb2d11d0b7cb6a835e697abb81c83624482a1dbb7deac2ffbc1f8a5a8daa6120c6a2725d2770d2866c2b27')
else
  _debarch=amd64
  sha512sums=('f9b061c46e3a6cb2451c8e6925e73cf2680c34169b20334374ed41516eabd1b7d4d73e8c2a66403118672cf06f672037c312b71f88af68454dfe15bd9be3b225')
fi

source=(http://ftp.debian.org/debian/pool/main/p/pdftk/pdftk_${pkgver//_/-}_${_debarch}.deb)

package() {
  tar -xf data.tar.?z -C "$pkgdir" ./usr
}

# vim:set ts=2 sw=2 ft=sh et:
