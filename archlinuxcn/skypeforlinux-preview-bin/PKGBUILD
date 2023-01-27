# Maintainer: mark.blakeney at bullet-systems dot net
# Original Maintainer: Jameson Pugh <imntreal@gmail.com>

_pkgname=skypeforlinux
pkgname=$_pkgname-preview-bin
pkgver=8.94.76.201
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
install=install.sh
source=(
https://repo.skype.com/rpm/unstable/${_pkgname}_${pkgver}-1.x86_64.rpm
)
sha256sums=('670f3f000c20e0632689a39d2bc87731752000a24c9c1335152837e291640b89')

package() {
  cd $pkgdir
  bsdtar -xf $srcdir/${_pkgname}_${pkgver}-1.x86_64.rpm
  rm -rf "$pkgdir/usr/lib/.build-id"
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  mv "$pkgdir/usr/share/$_pkgname/LICENSES.chromium.html" \
     "$pkgdir/usr/share/licenses/$pkgname/"
}

# vim:set ts=2 sw=2 et:
