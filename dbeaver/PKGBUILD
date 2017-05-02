# Maintainer: Arne Hoch <arne@derhoch.de>

pkgname=dbeaver
pkgver=4.0.6
pkgrel=1
pkgdesc="A free universal database tool for developers and database administrators"
arch=('i686' 'x86_64')
url="http://dbeaver.jkiss.org/"
license=("ASL 2.0")
depends=('java-runtime>=8' 'gtk2' 'gtk-update-icon-cache')
makedepends=('maven' 'java-environment>=8')
source=("https://github.com/serge-rider/dbeaver/archive/${pkgver}.tar.gz"
        'dbeaver.desktop')
sha256sums=('ff12c264fab8f8ab24a0a7cabd7b317142f73ed0de4f28ab1e6959675ca0fa85'
            'd6890b86f1ece47d2bc6f039f89a90eba985376ccb117d832fcddd9a103f6689')

build() {
    cd "${srcdir}/${pkgname}-${pkgver}/"
    mvn package
}

package() {
  if [ "${CARCH}" = x86_64 ]; then
    _64="_64"
  fi

  cd "${pkgdir}"
  mkdir -p opt/
  mkdir -p usr/bin
  mkdir -p usr/share/applications
  mkdir -p usr/share/icons/hicolor/48x48/apps

  cp -r "${srcdir}/${pkgname}-${pkgver}/product/standalone/target/products/org.jkiss.dbeaver.core.product/linux/gtk/x86${_64}/dbeaver" opt/
  cp opt/dbeaver/icon.xpm usr/share/icons/hicolor/48x48/apps/dbeaver.xpm
  ln -s /opt/dbeaver/dbeaver usr/bin/dbeaver
  install -m 644 "${srcdir}/dbeaver.desktop" "${pkgdir}/usr/share/applications/"
}
