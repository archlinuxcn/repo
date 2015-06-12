# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jove Yu <yushijun110 [at] gmail.com>

pkgname=wps-office
pkgver=9.1.0.4961_a18p1
_pkgver=9.1.0.4961~a18p1
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
source_i686=("http://kdl.cc.ksosoft.com/wps-community/download/a18/wps-office_${_pkgver}_x86.tar.xz")
source_x86_64=("http://kdl.cc.ksosoft.com/wps-community/download/a18/wps-office_${_pkgver}_x86_64.tar.xz")
sha512sums_i686=('ecb1d3663eb3a37a79bf646dda7ae9f7c739536203047097d34edcfbe5c2ddd3b277900b2569ece24ddfc371fcbc9e6efc2d6581506a7a7b0ed2bd964dbe68d9')
sha512sums_x86_64=('c035a7ebbe05d51d8800d36084040fa983308637b88e14d394c3172acf8cde47c5bf4bccf8a0520cbfb5266019bc62c329d9d5429128b5c3f49d083c2286a89a')

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
