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
pkgver=15.14.1
pkgrel=1
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
        CVE-2016-2334.patch
        CVE-2016-2335.patch
        natspec.patch)
sha256sums=('699db4da3621904113e040703220abb1148dfef477b55305e2f14a4f1f8f25d4'
            '632cae14095e065cb550b0f16faf39d8f822d0a8bb5b605e903f3bc7657a4ee5'
            '368870f92c658e8add261695923470855a969c0d7ecafd880ec7144ac245adbf'
            'd557e210ab392c317dc635efa2ac26739f06463b6d816348f3e8e78d3a815c38')

prepare() {
	cd "$srcdir/${_pkgname}_$pkgver"
	patch -p1 < ../natspec.patch

  if [[ $CARCH = x86_64 ]]; then
    cp makefile.linux_amd64_asm makefile.machine
  else
    cp makefile.linux_x86_asm_gcc_4.X makefile.machine
  fi

  # https://sourceforge.net/p/p7zip/discussion/383043/thread/9d0fb86b/
  patch -Np1 -i ../CVE-2016-2334.patch
  patch -Np1 -i ../CVE-2016-2335.patch
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
}

# vim:set ts=2 sw=2 et:
