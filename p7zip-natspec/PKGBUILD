# Maintainer: Taiki Sugawara <buzz.taiki@gmail.com>
# Contributor: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor: Thayer Williams <thayer@archlinux.org>
# Contributor: Hugo Doria <hugo@archlinux.org>
# Contributor: TuxSpirit<tuxspirit@archlinux.fr>  2007/11/17 21:22:36 UTC
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgbase=p7zip-natspec
pkgname=p7zip-natspec
_pkgname=p7zip
pkgver=9.38.1
pkgrel=5
pkgdesc="Command-line file archiver with high compression ratio file archiver, based on libnatspec patch from ubuntu zip-i18n PPA (https://launchpad.net/~frol/+archive/zip-i18n)."
arch=('i686' 'x86_64')
url="http://p7zip.sourceforge.net/"
license=('LGPL' 'custom:unRAR')
depends=('gcc-libs' 'sh' 'libnatspec')
makedepends_i686=('nasm')
makedepends_x86_64=('yasm')
conflicts=('p7zip')
provides=('p7zip')
install=$_pkgname.install
source=(https://downloads.sourceforge.net/project/$_pkgname/$_pkgname/$pkgver/${_pkgname}_${pkgver}_src_all.tar.bz2
        natspec.patch)
sha256sums=('fd5019109c9a1bf34ad3257d37a6853eae8151ff50345f0a3ffba7d8c5fdb995'
            '23e73fa308603febf9cf032c86775b0b6d8baeb41d78fd904e5bf45e3f83f7a8')

prepare() {
	cd "$srcdir/${_pkgname}_$pkgver"
	patch -p1 < ../natspec.patch

  if [[ $CARCH = x86_64 ]]; then
    cp makefile.linux_amd64_asm makefile.machine
  else
    cp makefile.linux_x86_asm_gcc_4.X makefile.machine
  fi
}

build() {
  cd "$srcdir/${_pkgname}_$pkgver"
  make all3 OPTFLAGS="$CFLAGS"
}

package() {
  cd "$srcdir/${_pkgname}_$pkgver"

  make install \
    DEST_DIR="$pkgdir" \
    DEST_HOME=/usr \
    DEST_MAN=/usr/share/man

  install -d "${pkgdir}"/usr/share/licenses/p7zip
  ln -s -t "$pkgdir/usr/share/licenses/p7zip/" \
    /usr/share/doc/p7zip/DOC/License.txt \
    /usr/share/doc/p7zip/DOC/unRarLicense.txt

  chmod -R a+r,u+w,a+X "$pkgdir/usr"
}

# vim:set ts=2 sw=2 et:
