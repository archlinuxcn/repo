# Maintainer: Cedric Girard <girard.cedric@gmail.com>
# Contributor: N30N <archlinux@alunamation.com>

pkgname=unarchiver
epoch=1
pkgver=1.8.1
pkgrel=1
pkgdesc="unar and lsar: Objective-C tools for uncompressing archive files"
arch=('x86_64' 'i686')
url="http://unarchiver.c3.cx/"
license=('LGPL2.1')
depends=('gnustep-base' 'openssl' 'bzip2' 'icu' 'gcc-libs' 'zlib')
makedepends=('gcc-objc')
source=("http://theunarchiver.googlecode.com/files/unar${pkgver}_src.zip"
        "native_obj_exceptions.patch")
sha1sums=('fe052cd7042651cccc7ba0e9c4d6d7dba5102fd4'
          'b8024026607dc2de758479b73d8b01ca6f692b59')

prepare(){
  cd "$srcdir/The Unarchiver"

  patch -p1 < ../native_obj_exceptions.patch

}

build() {
  cd "$srcdir/The Unarchiver/XADMaster"

  . /usr/share/GNUstep/Makefiles/GNUstep.sh
  make -f Makefile.linux
}

package() {
  cd "$srcdir/The Unarchiver/XADMaster"
  install -d "$pkgdir/usr/bin/"
  install -m755 unar lsar "$pkgdir/usr/bin/"

  cd "$srcdir/The Unarchiver/Extra"
  install -d "$pkgdir/usr/share/man/man1"
  gzip -c lsar.1 > "$pkgdir/usr/share/man/man1"/lsar.1.gz
  gzip -c unar.1 > "$pkgdir/usr/share/man/man1"/unar.1.gz
  install -d "$pkgdir/usr/share/bash-completion/completions/"
  install -m644 unar.bash_completion "$pkgdir/usr/share/bash-completion/completions/unar"
  install -m644 lsar.bash_completion "$pkgdir/usr/share/bash-completion/completions/lsar"
}

# vim:set ts=2 sw=2 et:
