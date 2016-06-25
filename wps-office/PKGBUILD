# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jove Yu <yushijun110 [at] gmail.com>

pkgname=wps-office
pkgver=10.1.0.5672_a21
_pkgver=10.1.0.5672~a21
pkgrel=1
pkgdesc="Kingsoft Office (WPS Office) is an office productivity suite"
arch=('i686' 'x86_64')
license=("custom")
url="http://wps-community.org/"
depends=('fontconfig' 'libpng12' 'glib2' 'libsm' 'libxext' 'libxrender' 'libxml2' 'desktop-file-utils' 'shared-mime-info' 'xdg-utils' 'glu')
optdepends=('cups: for printing support'
            'pango: for complex (right-to-left) text support')
conflicts=('kingsoft-office')
options=('!emptydirs')
install=${pkgname}.install
[[ "$CARCH" = "i686" ]] && _archext=x86 || _archext=x86_64
source_i686=("http://kdl.cc.ksosoft.com/wps-community/download/a21/wps-office_${_pkgver}_x86.tar.xz")
source_x86_64=("http://kdl.cc.ksosoft.com/wps-community/download/a21/wps-office_${_pkgver}_x86_64.tar.xz")
sha512sums_i686=('dbba052a025e7057e1c73bf1b9904d3c71cec99a9ee314ee0fbdd98459e8507c03b1ed7e8367e254eb6485114f00630e0abc5f1d42ac5fa1d53230b8ba07b691')
sha512sums_x86_64=('6b781d8b4db0173fb896e05508dd986ffb7d7c5e4ab452738b487d79588604b4a98f3616e0c775a1fd21ed20b6fbfbc9f81b1868c3cbfd34e770dfde8544c0c0')

PKGEXT=".pkg.tar"

prepare() {
  cd wps-office_${_pkgver}_$_archext

  sed -i 's|/opt/kingsoft/wps-office|/usr/lib|' wps wpp et
}

package() {
  cd wps-office_${_pkgver}_$_archext

  install -d "$pkgdir/usr/lib"
  cp -r office6 "$pkgdir/usr/lib"

  install -d "$pkgdir/usr/bin"
  install -m755 wps wpp et "$pkgdir/usr/bin"

  install -d "$pkgdir/usr/share/applications"
  cp -r resource/applications/* "$pkgdir/usr/share/applications"

  install -d "$pkgdir/usr/share/icons"
  cp -r resource/icons/* "$pkgdir/usr/share/icons"

  install -d "$pkgdir/usr/share/mime"
  cp -r resource/mime/* "$pkgdir/usr/share/mime"

  #cp -r "$srcdir/usr/share" "$pkgdir/usr/"

  install -d "$pkgdir/usr/share/fonts/wps-office"
  cp -r fonts/* "$pkgdir/usr/share/fonts/wps-office"

  install -Dm644 office6/mui/default/EULA.txt "$pkgdir/usr/share/licenses/$pkgname/EULA.txt"
}
