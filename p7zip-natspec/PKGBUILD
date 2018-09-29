# Maintainer: Taiki Sugawara <buzz.taiki@gmail.com>
# Contributor: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor: Thayer Williams <thayer@archlinux.org>
# Contributor: Hugo Doria <hugo@archlinux.org>
# Contributor: TuxSpirit<tuxspirit@archlinux.fr>  2007/11/17 21:22:36 UTC
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=p7zip-natspec
_pkgname=p7zip
pkgver=16.02
pkgrel=3
_upstream_pkgrel=5
pkgdesc="Command-line file archiver with high compression ratio, based on libnatspec patch from ubuntu zip-i18n PPA (https://launchpad.net/~frol/+archive/zip-i18n)."
arch=('x86_64')
url="http://p7zip.sourceforge.net/"
license=('LGPL' 'custom:unRAR')
depends=('gcc-libs' 'sh' 'libnatspec')
makedepends=('yasm')
conflicts=('p7zip')
provides=('p7zip')
install=$_pkgname.install
source=(https://downloads.sourceforge.net/project/$_pkgname/$_pkgname/$pkgver/${_pkgname}_${pkgver}_src_all.tar.bz2
        CVE-2016-9296.patch
        CVE-2017-17969.patch
        CVE-2018-5996.patch
        CVE-2018-10115.patch
        natspec.patch)
sha256sums=('5eb20ac0e2944f6cb9c2d51dd6c4518941c185347d4089ea89087ffdd6e2341f'
            'f9bcbf21d4aa8938861a6cba992df13dec19538286e9ed747ccec6d9a4e8f983'
            'c6af5ba588b8932a5e99f3741fcf1011b7c94b533de903176c7d1d4c02a9ebef'
            '9c92b9060fb0ecc3e754e6440d7773d04bc324d0f998ebcebc263264e5a520df'
            'c397eb6ad60bfab8d388ea9b39c0c13ae818f86746210c6435e35b35c786607f'
            'e98506a3880da2d8b54ccbafbb3acac1bbc6b8f2552de37b658a4bfac7f498ad')

prepare() {
	cd "$srcdir/${_pkgname}_$pkgver"
	patch -p1 < ../natspec.patch

  # https://sourceforge.net/p/p7zip/bugs/185/
  patch -Np1 -i ../CVE-2016-9296.patch

  # https://sourceforge.net/p/p7zip/bugs/204/
  patch -Np1 -i ../CVE-2017-17969.patch

  # Security patches from Debian
  patch -Np1 -i ../CVE-2018-5996.patch
  patch -Np1 -i ../CVE-2018-10115.patch

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

  # Remove documentation for the GUI file manager
  rm -r "$pkgdir/usr/share/doc/p7zip/DOC/MANUAL/fm"

  install -d "${pkgdir}"/usr/share/licenses/p7zip
  ln -s -t "$pkgdir/usr/share/licenses/p7zip/" \
    /usr/share/doc/p7zip/DOC/License.txt \
    /usr/share/doc/p7zip/DOC/unRarLicense.txt
}

# vim:set ts=2 sw=2 et:
