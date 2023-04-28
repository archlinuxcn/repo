# Maintainer: mark.blakeney at bullet-systems dot net
# Original Maintainer: Jameson Pugh <imntreal@gmail.com>

_pkgname=skypeforlinux
pkgname="$_pkgname-preview-bin"
pkgver=8.97.76.302
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
sha256sums=('cc38803eee335eeda74fc48dbdcc4c7e00ebf299a5809192ddac00d66ff20cc3')

package() {
  tar --no-same-owner -xC "$pkgdir" -f data.tar.gz
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  mv "$pkgdir/usr/share/$_pkgname/LICENSES.chromium.html" \
    "$pkgdir/usr/share/licenses/$pkgname/"
  rm -rf "$pkgdir/opt"
}

# vim:set ts=2 sw=2 et:
