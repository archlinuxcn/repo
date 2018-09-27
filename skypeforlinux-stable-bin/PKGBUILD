# Maintainer: mark.blakeney at bullet-systems dot net
# Original Maintainer: Jameson Pugh <imntreal@gmail.com>

_pkgname=skypeforlinux
pkgname=$_pkgname-stable-bin
pkgver=8.31.0.92
pkgrel=1
pkgdesc="Skype for Linux - Stable/Release Version"
arch=("x86_64")
url="http://www.skype.com"
license=("custom")
depends=("gtk3" "libxss" "gconf" "alsa-lib" "libxtst" "libsecret" "nss" "glibc>=2.28-4")
optdepends=("gnome-keyring")
conflicts=("$_pkgname" "$_pkgname-bin" "$_pkgname-preview-bin" "$_pkgname-beta-bin" "skype")
provides=("$_pkgname" "skype")
source=(
"https://repo.skype.com/deb/pool/main/s/$_pkgname/${_pkgname}_${pkgver}_amd64.deb"
)
sha256sums=('04cfdd87f683130121c67e7e9e25b8fbaec003ff968bab0240d2f167c5cd5d7b')

package() {
  tar -xJC "$pkgdir" -f data.tar.xz
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  mv "$pkgdir/usr/share/$_pkgname/LICENSES.chromium.html" \
    "$pkgdir/usr/share/licenses/$pkgname/"
  rm -rf "$pkgdir/opt"
}

# vim:set ts=2 sw=2 et:
