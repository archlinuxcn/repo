# Maintainer: carstene1ns <arch carsten-teibes de> - http://git.io/ctPKG
# Contributor: Wolfen <rostov344-arch at yahoo dot fr>

pkgname=httpry
pkgver=0.1.8
pkgrel=1
pkgdesc="A specialized packet sniffer designed for displaying and logging HTTP traffic."
arch=('i686' 'x86_64')
url="http://dumpsterventures.com/jason/httpry/"
license=('GPL2')
depends=("libpcap")
optdepends=('perl: if you want to use the scripts/plugins')
source=("http://dumpsterventures.com/jason/httpry/httpry-$pkgver.tar.gz")
sha256sums=('ef53454f895f68005f7b9ab634d1b433c4df839eacea9109e4ee48d4296fb613')

build() {
  make -C $pkgname-$pkgver
}

package() {
  cd $pkgname-$pkgver

  # bin + man
  install -Dm755 httpry "$pkgdir"/usr/bin/httpry
  install -Dm644 httpry.1 "$pkgdir"/usr/share/man/man1/httpry.1

  # scripts
  install -Dm644 scripts/parse_log.pl "$pkgdir"/usr/lib/httpry/scripts/parse_log.pl
  cp -rup scripts/plugins "$pkgdir"/usr/lib/httpry/scripts/
  ln -s /usr/share/doc/httpry/perl-tools "$pkgdir"/usr/lib/httpry/scripts/perl-tools

  # docs
  install -d "$pkgdir"/usr/share/doc/httpry
  install -m644 doc/* "$pkgdir"/usr/share/doc/httpry
}
