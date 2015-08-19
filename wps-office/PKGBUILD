# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jove Yu <yushijun110 [at] gmail.com>

pkgname=wps-office
pkgver=9.1.0.4975_a19p1
_pkgver=9.1.0.4975~a19p1
pkgrel=1
pkgdesc="Kingsoft Office (WPS Office) is an office productivity suite"
arch=('i686' 'x86_64')
license=("custom")
url="http://wps-community.org/"
depends=('fontconfig' 'libpng12' 'glib2' 'libsm' 'libxext' 'libxrender' 'libxml2' 'desktop-file-utils' 'shared-mime-info' 'xdg-utils')
optdepends=('cups: for printing support'
            'pango: for complex (right-to-left) text support')
conflicts=('kingsoft-office')
options=('!emptydirs')
install=${pkgname}.install
[[ "$CARCH" = "i686" ]] && _archext=x86 || _archext=x86_64
source_i686=("http://kdl.cc.ksosoft.com/wps-community/download/a19/wps-office_${_pkgver}_x86.tar.xz")
source_x86_64=("http://kdl.cc.ksosoft.com/wps-community/download/a19/wps-office_${_pkgver}_x86_64.tar.xz")
sha512sums_i686=('17b5108e35cd6e01072f8a45accc915c987225236a80afdcdf58b8f8cc02e5fcae6f0930f28fa073092f9cc92950aff2745297ec218a994aba769f185c35b560')
sha512sums_x86_64=('80d36c3b5e8db6771f78dce9a1c23a00a6938d19aeccc43640fab0a1d9759ab501d5221b7c5da1f5f6ea3c0621735a3521ddf5864197a16c3bbbc9950378b8d0')

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
  install -m755 wps wpp et wps_error_check.sh "$pkgdir/usr/bin"

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
