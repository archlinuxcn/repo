# Maintainer: mark.blakeney at bullet-systems dot net
# Original Maintainer: Jameson Pugh <imntreal@gmail.com>

_pkgname=skypeforlinux
pkgname=$_pkgname-bin
pkgver=8.10.76.7
pkgrel=1
pkgdesc="Skype for Linux - Insider/Preview Version"
arch=("x86_64")
url="http://www.skype.com"
license=("custom")
depends=("gtk2" "libxss" "gconf" "alsa-lib" "libxtst" "libsecret" "nss")
optdepends=("gnome-keyring")
conflicts=("$_pkgname" "$_pkgname-beta-bin")
provides=("$_pkgname")
source=("https://repo.skype.com/deb/pool/main/s/$_pkgname/${_pkgname}_${pkgver}_amd64.deb")
sha256sums=('182cc956408b55f2487426af84b8cc32ad96ee982acf45391ff4514d1fcb00da')

package() {
  tar -xJC "$pkgdir" -f data.tar.xz
  install -d "$pkgdir/usr/share/licenses/$pkgname"
  mv "$pkgdir/usr/share/$_pkgname/LICENSES.chromium.html" \
    "${pkgdir}/usr/share/licenses/$pkgname/"
  rm -rf "$pkgdir/opt"
  # Patch wrong WM class until this is fixed.
  sed -i "/^StartupWMClass=/s/ Preview//" \
    "$pkgdir/usr/share/applications/$_pkgname.desktop"
}

# vim:set ts=2 sw=2 et:
