# Maintainer: Jingbei Li <i@jingbei.li>
# Contributor: codestation <codestation404 at gmail dot com>

pkgname=wxmedit
pkgver=3.1_FIX1
pkgrel=2
pkgdesc="Cross-platform Text/Hex Editor, a fork of MadEdit with bug fixes and improvements"
arch=("i686" "x86_64")
url="https://wxmedit.github.io/"
license=('GPL')
depends=('curl' 'wxgtk')
makedepends=('boost')
source=("https://github.com/hltj/wxMEdit/archive/$pkgver.tar.gz")
sha256sums=('51dd81ddd44c83017d2e54f8b0a11a50e56075e8edc01d738865478fdddd8017')

build() {
  cd "$srcdir/wxMEdit-$pkgver"

  sed 's|boost/tr1/unordered_set.hpp|boost/unordered_set.hpp|g' -i `grep 'boost/tr1/unordered_set.hpp' . -rIl`
  sed 's|boost/tr1/unordered_map.hpp|boost/unordered_map.hpp|g' -i `grep 'boost/tr1/unordered_map.hpp' . -rIl`
  sed 's/std::tr1/boost/g' -i `grep 'std::tr1::' . -rIl`
  sed 's/UnicodeString/icu::UnicodeString/g' -i `grep 'UnicodeString' . -rIl`
  sed 's/BreakIterator/icu::BreakIterator/g' -i `grep 'BreakIterator' . -rIl`
  sed 's/LocalUCharsetDetectorPointer/icu::LocalUCharsetDetectorPointer/g' -i `grep 'LocalUCharsetDetectorPointer' . -rIl`
  sed 's/Locale/icu::Locale/g' -i src/wxmedit/wxm_lines.cpp src/wxmedit/wxmedit.cpp

  ./configure --prefix=/usr --with-wx-config=/usr/bin/wx-config
  make
}

package() {
  cd "$srcdir/wxMEdit-$pkgver"
  make DESTDIR="${pkgdir}" install
}
