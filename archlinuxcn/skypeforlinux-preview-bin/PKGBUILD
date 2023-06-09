# Maintainer: mark.blakeney at bullet-systems dot net
# Original Maintainer: Jameson Pugh <imntreal@gmail.com>

_pkgname=skypeforlinux
pkgname="$_pkgname-preview-bin"
pkgver=8.99.76.102
pkgrel=1
pkgdesc="Skype for Linux - Preview/Insider Version"
arch=("x86_64")
url="http://www.skype.com"
license=("custom")
depends=("gtk3" "libxss" "alsa-lib" "libxtst" "libsecret" "nss"
         "glibc>=2.28-4")
optdepends=("org.freedesktop.secrets: keyring/password support"
            "libappindicator-gtk3: systray icon support")
conflicts=("$_pkgname" "$_pkgname-bin" "$_pkgname-stable-bin"
           "$_pkgname-beta-bin" "skype")
provides=("$_pkgname" "skype")
replaces=("$_pkgname-bin")
install="$pkgname-install"
source=(
"https://repo.skype.com/deb/pool/main/s/$_pkgname/${_pkgname}_${pkgver}_amd64.deb"
)
sha256sums=('a868e53b326cf1a72088ad21a445e2a1221e18673b5d8f7d2d985e83768c513c')

package() {
  tar --no-same-owner -xC "$pkgdir" -f data.tar.gz
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  mv "$pkgdir/usr/share/$_pkgname/LICENSES.chromium.html" \
    "$pkgdir/usr/share/licenses/$pkgname/"
  rm -rf "$pkgdir/opt"
}

# vim:set ts=2 sw=2 et:
