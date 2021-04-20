# Maintainer: George Rawlinson <george@rawlinson.net.nz>
# Contributor: Arthur Darcet <arthur.darcet at m4x.org>
# Contributor: Techlive Zheng <techlivezheng at gmail.com>

pkgname=libiconv
pkgver=1.16
pkgrel=3
pkgdesc='GNU charset conversion library'
arch=('i686' 'x86_64')
url='http://www.gnu.org/software/libiconv/'
license=('LGPL')
depends=(glibc)
provides=(libcharset.so libiconv.so)
source=("https://ftp.gnu.org/pub/gnu/${pkgname}/${pkgname}-${pkgver}.tar.gz"{,.sig})
sha512sums=('365dac0b34b4255a0066e8033a8b3db4bdb94b9b57a9dca17ebf2d779139fe935caf51a465d17fd8ae229ec4b926f3f7025264f37243432075e5583925bb77b7'
            'SKIP')
options=(!libtool)
# NOTE: Below key has expired, package was signed before it expired and
# upstream does not consider this an issue. Hopefully the next release is
# signed with a new PGP key.
validpgpkeys=(
  '68D94D8AAEEAD48AE7DC5B904F494A942E4616C2' # Bruno Haible <bruno@clisp.org>
)

build() {
  cd "${pkgname}-${pkgver}"
  ./configure \
    --prefix=/usr \
    --docdir=/usr/share/doc/libiconv

  # workaround for insecure rpath
  sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
  sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

  make
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install

  # move references from iconv to libiconv
  mv -v "$pkgdir"/usr/include/{iconv.h,libiconv.h}
  mv -v "$pkgdir"/usr/bin/{iconv,libiconv}
  mv -v "$pkgdir"/usr/share/man/man1/{,lib}iconv.1
  mv -v "$pkgdir"/usr/share/man/man3/{,libiconv_}iconv.3
  mv -v "$pkgdir"/usr/share/man/man3/{,libiconv_}iconvctl.3
  mv -v "$pkgdir"/usr/share/man/man3/{,libiconv_}iconv_open.3
  mv -v "$pkgdir"/usr/share/man/man3/{,libiconv_}iconv_close.3
  mv -v "$pkgdir"/usr/share/man/man3/{,libiconv_}iconv_open_into.3
}
