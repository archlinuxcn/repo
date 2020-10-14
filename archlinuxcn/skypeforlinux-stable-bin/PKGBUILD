# Maintainer: mark.blakeney at bullet-systems dot net
# Original Maintainer: Jameson Pugh <imntreal@gmail.com>

_pkgname=skypeforlinux
pkgname=$_pkgname-stable-bin
pkgver=8.65.0.78
pkgrel=1
pkgdesc="Skype for Linux - Stable/Release Version"
arch=("x86_64")
url="http://www.skype.com"
license=("custom")
depends=("gtk3" "libxss" "alsa-lib" "libxtst" "libsecret" "nss"
         "glibc>=2.28-4")
optdepends=("org.freedesktop.secrets: keyring/password support"
            "libappindicator-gtk3: systray icon support")
conflicts=("$_pkgname" "$_pkgname-bin" "$_pkgname-preview-bin"
           "$_pkgname-beta-bin" "skype")
provides=("$_pkgname" "skype")
install=install.sh
source=(
"https://repo.skype.com/deb/pool/main/s/$_pkgname/${_pkgname}_${pkgver}_amd64.deb"
)
sha256sums=('9026f043697d7d0783e7232701a868229d9a91e91dc0ae86509732c1c7bf0c13')

package() {
  tar --no-same-owner -xJC "$pkgdir" -f data.tar.xz
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  mv "$pkgdir/usr/share/$_pkgname/LICENSES.chromium.html" \
    "$pkgdir/usr/share/licenses/$pkgname/"
  rm -rf "$pkgdir/opt"
}

# vim:set ts=2 sw=2 et:
