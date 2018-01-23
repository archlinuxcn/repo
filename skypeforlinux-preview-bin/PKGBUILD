# Maintainer: mark.blakeney at bullet-systems dot net
# Original Maintainer: Jameson Pugh <imntreal@gmail.com>

_pkgname=skypeforlinux
pkgname=$_pkgname-preview-bin
pkgver=8.14.76.4
pkgrel=2
pkgdesc="Skype for Linux - Preview/Insider Version"
arch=("x86_64")
url="http://www.skype.com"
license=("custom")
depends=("gtk2" "libxss" "gconf" "alsa-lib" "libxtst" "libsecret" "nss")
optdepends=("gnome-keyring")
conflicts=("$_pkgname" "$_pkgname-bin" "$_pkgname-stable-bin" "$_pkgname-beta-bin")
provides=("$_pkgname")
replaces=("$_pkgname-bin")
source=("https://repo.skype.com/deb/pool/main/s/$_pkgname/${_pkgname}_${pkgver}_amd64.deb")
sha256sums=('8d5a82b3623625eaa2e7f8218dccebe5084925918a97fb8f328c2b17472f7813')

package() {
  tar -xJC "$pkgdir" -f data.tar.xz
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  mv "$pkgdir/usr/share/$_pkgname/LICENSES.chromium.html" \
    "${pkgdir}/usr/share/licenses/$pkgname/"
  rm -rf "$pkgdir/opt"
}

# vim:set ts=2 sw=2 et:
