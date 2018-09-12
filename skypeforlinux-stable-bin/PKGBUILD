# Maintainer: mark.blakeney at bullet-systems dot net
# Original Maintainer: Jameson Pugh <imntreal@gmail.com>

_pkgname=skypeforlinux
pkgname=$_pkgname-stable-bin
pkgver=8.30.0.50
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
sha256sums=('fd7c93394945135c0bb97bddb6b88367d5b48396cbc36a296246d7e9402b9884')

package() {
  tar -xJC "$pkgdir" -f data.tar.xz
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  mv "$pkgdir/usr/share/$_pkgname/LICENSES.chromium.html" \
    "$pkgdir/usr/share/licenses/$pkgname/"
  rm -rf "$pkgdir/opt"
}

# vim:set ts=2 sw=2 et:
