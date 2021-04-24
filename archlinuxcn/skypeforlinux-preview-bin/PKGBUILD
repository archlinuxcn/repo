# Maintainer: mark.blakeney at bullet-systems dot net
# Original Maintainer: Jameson Pugh <imntreal@gmail.com>

_pkgname=skypeforlinux
pkgname=$_pkgname-preview-bin
pkgver=8.72.76.29
pkgrel=1
pkgdesc="Skype for Linux - Preview/Insider Version"
arch=("x86_64")
url="http://www.skype.com"
license=("custom")
depends=("gtk3" "libxss" "alsa-lib" "libxtst" "libsecret" "nss"
         "glibc>=2.28-4")
makedepends=("rpmextract")
optdepends=("org.freedesktop.secrets: keyring/password support"
            "libappindicator-gtk3: systray icon support")
conflicts=("$_pkgname" "$_pkgname-bin" "$_pkgname-stable-bin"
           "$_pkgname-beta-bin" "skype")
provides=("$_pkgname" "skype")
replaces=("$_pkgname-bin")
install=install.sh
source=(
https://repo.skype.com/rpm/unstable/${_pkgname}_${pkgver}-1.x86_64.rpm
)
sha256sums=('c8813e9f8dbfc1270081d42626ea23f9849dbeb2f7bdfa701c7779a90a265fa1')

package() {
  cd $pkgdir
  rpmextract.sh $srcdir/${_pkgname}_${pkgver}-1.x86_64.rpm
  rm -rf "$pkgdir/usr/lib/.build-id"
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  mv "$pkgdir/usr/share/$_pkgname/LICENSES.chromium.html" \
     "$pkgdir/usr/share/licenses/$pkgname/"
}

# vim:set ts=2 sw=2 et:
