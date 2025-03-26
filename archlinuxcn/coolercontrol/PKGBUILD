# Maintainer: Eren Simsek <18117384-caferen@users.noreply.gitlab.com>
# Maintainer: Guy Boldon <gb@guyboldon.com>

pkgname=coolercontrol
_app_id="org.$pkgname.CoolerControl"
pkgver=2.0.0
pkgrel=1
pkgdesc="A program to monitor and control your cooling devices"
arch=('x86_64')
url="https://gitlab.com/coolercontrol/coolercontrol"
license=('GPL-3.0-or-later')
depends=(
  'qt6-webengine'
  'gcc-libs'
  'glibc'
  'hicolor-icon-theme'
  'coolercontrold'
)
makedepends=(
  'cmake'
)
checkdepends=(
  'appstream-glib'
  'desktop-file-utils'
)
provides=(
  "$pkgname"
)
conflicts=(
  "$pkgname"
)
source=(
  "https://gitlab.com/coolercontrol/coolercontrol/-/archive/$pkgver/$pkgname-$pkgver.tar.gz"
)
sha256sums=(
  '92f2577a6455c1faa3bd568776902e591ff71ed26ea547b22205b6b11ea76fd7'
)

build() {
  cd "${srcdir}/$pkgname-$pkgver/coolercontrol"
  cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="/${pkgdir}/usr" 
  make -C build -j8
}

check() {
  cd "${srcdir}/$pkgname-$pkgver"
  desktop-file-validate "packaging/metadata/$_app_id.desktop"
  appstream-util validate-relax "packaging/metadata/$_app_id.metainfo.xml"
}

package() {
  cd "${srcdir}/$pkgname-$pkgver/coolercontrol"
  make install

  cd "${srcdir}/$pkgname-$pkgver"
  # desktop metadata
  install -Dm644 "packaging/metadata/$_app_id.desktop" -t "$pkgdir/usr/share/applications/"
  install -Dm644 "packaging/metadata/$_app_id.metainfo.xml" -t "$pkgdir/usr/share/metainfo/"
  install -Dm644 "packaging/metadata/$_app_id.png" -t "$pkgdir/usr/share/pixmaps/"
  install -Dm644 "packaging/metadata/$_app_id.svg" -t "$pkgdir/usr/share/icons/hicolor/scalable/apps/"

  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
