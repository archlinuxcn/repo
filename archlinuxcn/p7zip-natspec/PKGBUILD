# Maintainer: Taiki Sugawara <buzz.taiki@gmail.com>
# Contributor: Evangelos Foutras <evangelos@foutrelis.com>
# Contributor: Gaetan Bisson <bisson@archlinux.org>
# Contributor: Thayer Williams <thayer@archlinux.org>
# Contributor: Hugo Doria <hugo@archlinux.org>
# Contributor: TuxSpirit<tuxspirit@archlinux.fr>
# Contributor: Daniel J Griffiths <ghost1227@archlinux.us>

pkgname=p7zip-natspec
_pkgname=p7zip
pkgver=17.05
pkgrel=3
_upstream_pkgrel=5
pkgdesc="Command-line file archiver with high compression ratio, based on libnatspec patch from ubuntu zip-i18n PPA (https://launchpad.net/~frol/+archive/zip-i18n)."
arch=('x86_64' 'aarch64')
url="https://github.com/p7zip-project/p7zip"
license=('LGPL' 'custom:unRAR')
depends=('gcc-libs' 'sh' 'libnatspec')
conflicts=('p7zip' '7zip')
provides=('p7zip' '7zip')
source=(https://github.com/p7zip-project/p7zip/archive/v$pkgver/$_pkgname-v$pkgver.tar.gz
        natspec.patch
        do-not-gzip-man-pages.patch)
sha256sums=('d2788f892571058c08d27095c22154579dfefb807ebe357d145ab2ddddefb1a6'
            '8412de795faf1abafc5303458699f1621e4900ef854b733c7c409385d78e11ee'
            '2179e67764eb46cb414ce9b5c978a532a6499617a6a685deb323b6da122aba00')

prepare() {
  cd $_pkgname-$pkgver

  # Leave man page compression to makepkg to maintain reproducibility
  patch -Np1 -i ../do-not-gzip-man-pages.patch

  patch -p1 < ../natspec.patch
}

build() {
  cd $_pkgname-$pkgver
  make OPTFLAGS="$CPPFLAGS $CFLAGS" 7z 7zr 7za
}

package() {
  cd $_pkgname-$pkgver

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
