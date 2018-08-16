# Maintainer: mark.blakeney at bullet-systems dot net
# Original Maintainer: Jameson Pugh <imntreal@gmail.com>

_pkgname=skypeforlinux
pkgname=$_pkgname-preview-bin
pkgver=8.29.76.16
pkgrel=1
pkgdesc="Skype for Linux - Preview/Insider Version"
arch=("x86_64")
url="http://www.skype.com"
license=("custom")
depends=("gtk3" "libxss" "gconf" "alsa-lib" "libxtst" "libsecret" "nss")
optdepends=("gnome-keyring")
makedepends=("patchelf")
options=("!strip" "staticlibs")
conflicts=("$_pkgname" "$_pkgname-bin" "$_pkgname-stable-bin" "$_pkgname-beta-bin" "skype")
provides=("$_pkgname" "skype")
replaces=("$_pkgname-bin")
source=(
"https://repo.skype.com/deb/pool/main/s/$_pkgname/${_pkgname}_${pkgver}_amd64.deb"
"https://archive.archlinux.org/packages/g/glibc/glibc-2.27-3-${CARCH}.pkg.tar.xz"
)
noextract=("glibc-2.27-3-${CARCH}.pkg.tar.xz")
sha256sums=('0323599694f293c7063b785ad533ac1cf8981bfd875cce896df956e63004c72f'
            'a9e1b18d7f613be660556dbd6883781e88a0f5113230147e230d3e2f268792dc')

package() {
  _ldir="/usr/share/$_pkgname"
  _pdir="$pkgdir/$_ldir"
  _pexe="$_pdir/$_pkgname"
  tar -xJC "$pkgdir" -f data.tar.xz
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  mv "$_pdir/LICENSES.chromium.html" "$pkgdir/usr/share/licenses/$pkgname/"
  rm -rf "$pkgdir/opt"
  mkdir -p "$_pdir/glibc"
  tar -xJC "$_pdir/glibc" -f "glibc-2.27-3-$CARCH.pkg.tar.xz"
  rm "$_pdir/glibc/"{.BUILDINFO,.INSTALL,.MTREE,.PKGINFO}
  patchelf --set-interpreter "$_ldir/glibc/usr/lib/ld-linux-x86-64.so.2" "$_pexe"
  patchelf --set-rpath "$_ldir:$_ldir/glibc/usr/lib" "$_pexe"
}

# vim:set ts=2 sw=2 et:
