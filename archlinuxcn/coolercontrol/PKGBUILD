# Maintainer: Eren Simsek <18117384-caferen@users.noreply.gitlab.com>
# Maintainer: Guy Boldon <gb@guyboldon.com>

pkgname=coolercontrol
_app_id="org.$pkgname.CoolerControl"
pkgver=1.4.4
pkgrel=1
pkgdesc="A program to monitor and control your cooling devices"
arch=('x86_64')
url="https://gitlab.com/coolercontrol/coolercontrol"
license=('GPL-3.0-or-later')
depends=(
  'gcc-libs'
  'glibc'
  'gtk3'
  'hicolor-icon-theme'
  'libappindicator-gtk3'
  'webkit2gtk-4.1'
  'coolercontrold'
  'coolercontrol-liqctld'
)
makedepends=(
  'appmenu-gtk-module'
  'cargo'
  'gtk3'
  'libappindicator-gtk3'
  'librsvg'
  'libvips'
  'nodejs>=18'
  'npm'
  'openssl'
  'webkit2gtk-4.1'
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
# lto is handled by cargo and can conflict with makepkg settings
options=(
  !lto
)
source=(
  "https://gitlab.com/coolercontrol/coolercontrol/-/archive/$pkgver/$pkgname-$pkgver.tar.gz"
)
sha256sums=(
  'acf5a27111122230d243e66eae85212f9c01a402b12028a8918fc785414bb713'
)

build() {
  cd "${srcdir}/$pkgname-$pkgver/coolercontrol-ui"
  npm ci
  npm run build
  cd "${srcdir}/$pkgname-$pkgver/coolercontrol-ui/src-tauri"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --release --locked -F custom-protocol
}

check() {
  cd "${srcdir}/$pkgname-$pkgver"
  desktop-file-validate "packaging/metadata/$_app_id.desktop"
  appstream-util validate-relax "packaging/metadata/$_app_id.metainfo.xml"
  # This UI check will fail in a docker environment without a graphical environment:
  # cd "${srcdir}/$pkgname-$pkgver/coolercontrol-ui/src-tauri/target/release"
  # ./coolercontrol --version
}

package() {
  cd "${srcdir}/$pkgname-$pkgver/coolercontrol-ui/src-tauri"
  install -Dm755 "target/release/coolercontrol" -t "$pkgdir/usr/bin"

  cd "${srcdir}/$pkgname-$pkgver"
  # desktop metadata
  install -Dm644 "packaging/metadata/$_app_id.desktop" -t "$pkgdir/usr/share/applications/"
  install -Dm644 "packaging/metadata/$_app_id.metainfo.xml" -t "$pkgdir/usr/share/metainfo/"
  install -Dm644 "packaging/metadata/$_app_id.png" -t "$pkgdir/usr/share/pixmaps/"
  install -Dm644 "packaging/metadata/$_app_id.svg" -t "$pkgdir/usr/share/icons/hicolor/scalable/apps/"

  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
