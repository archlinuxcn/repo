# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jove Yu <yushijun110 [at] gmail.com>

pkgname=wps-office
pkgver=10.1.0.5444_a20
_pkgver=10.1.0.5444~a20
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
source_i686=("http://kdl.cc.ksosoft.com/wps-community/download/a20/wps-office_${_pkgver}_x86.tar.xz")
source_x86_64=("http://kdl.cc.ksosoft.com/wps-community/download/a20/wps-office_${_pkgver}_x86_64.tar.xz")
sha512sums_i686=('8c87e630bfa967e5527b654b95711c4b21100947b318d054a18617081300506d10831cbfc5d6c1b2a8bbdeaaa56f68f31fbe09972c6e57c817381ae9588b1c05')
sha512sums_x86_64=('ff2b83878fa3cc76b597fa4d859c6a1e9269f5c31fc9597dfdadec79066b91172ee3b2788ee550e30fd71f5332e3a9ac228993af210ce68ea6ee6d367216cf0c')

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
