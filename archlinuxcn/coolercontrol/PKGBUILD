# Maintainer: Guy Boldon <gb@guyboldon.com>

pkgname=coolercontrol
_app_id="org.$pkgname.CoolerControl"
pkgver=1.3.0
pkgrel=4
pkgdesc="A program to monitor and control your cooling devices"
arch=('x86_64')
url="https://gitlab.com/coolercontrol/coolercontrol"
license=('GPL3')
depends=(
  'gcc-libs'
  'glibc'
  'gtk3'
  'hicolor-icon-theme'
  'libappindicator-gtk3'
  'liquidctl'
  'python'
  'python-setproctitle'
  'python-fastapi'
  'python-pydantic'
  'python-urllib3'
  'uvicorn'
  'webkit2gtk'
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
  'python-build'
  'python-installer'
  'python-setuptools'
  'python-wheel'
  'webkit2gtk'
  'libdrm'
)
checkdepends=(
  'appstream-glib'
  'desktop-file-utils'
)
optdepends=(
  'nvidia-utils: NVIDIA GPU support'
)
provides=(
  "$pkgname"
)
conflicts=(
  "$pkgname" coolero
)
# lto is handled by cargo and can conflict with makepkg settings
options=(
  !lto
)
source=(
  "https://gitlab.com/coolercontrol/coolercontrol/-/archive/$pkgver/$pkgname-$pkgver.tar.gz"
)
sha256sums=(
  '7b5cd13fdede7f125d4349bd06597315b1ea430835ff609e65a07370fd702d46'
)

build() {
  cd "${srcdir}/$pkgname-$pkgver/coolercontrol-liqctld"
  python -m build --wheel --no-isolation
  cd "${srcdir}/$pkgname-$pkgver/coolercontrol-ui"
  npm ci
  npm run build
  cp -r dist/* "${srcdir}/$pkgname-$pkgver/coolercontrold/resources/app/"
  cd "${srcdir}/$pkgname-$pkgver/coolercontrold"
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
  cargo build --release --locked
  cd "${srcdir}/$pkgname-$pkgver/coolercontrol-ui/src-tauri"
  cargo build --release --locked -F custom-protocol
}

check() {
  cd "${srcdir}/$pkgname-$pkgver"
  desktop-file-validate "packaging/metadata/$_app_id.desktop"
  appstream-util validate-relax "packaging/metadata/$_app_id.metainfo.xml"
  cd "${srcdir}/$pkgname-$pkgver/coolercontrol-liqctld"
  python -m coolercontrol_liqctld --version
  cd "${srcdir}/$pkgname-$pkgver/coolercontrold/target/release"
  ./coolercontrold --version
  # This UI check will fail in a docker environment without a graphical environment:
  # cd "${srcdir}/$pkgname-$pkgver/coolercontrol-ui/src-tauri/target/release"
  # ./coolercontrol --version
}

package() {
  cd "${srcdir}/$pkgname-$pkgver/coolercontrol-liqctld"
  python -m installer --destdir="$pkgdir" dist/*.whl
  cd "${srcdir}/$pkgname-$pkgver/coolercontrold"
  install -Dm755 "target/release/coolercontrold" -t "$pkgdir/usr/bin"
  cd "${srcdir}/$pkgname-$pkgver/coolercontrol-ui/src-tauri"
  install -Dm755 "target/release/coolercontrol" -t "$pkgdir/usr/bin"

  cd "${srcdir}/$pkgname-$pkgver"
  # systemd service files
  install -Dm644 "packaging/systemd/${pkgname}d.service" -t "$pkgdir/usr/lib/systemd/system/"
  install -Dm644 "packaging/systemd/${pkgname}-liqctld.service" -t "$pkgdir/usr/lib/systemd/system/"

  # desktop metadata
  install -Dm644 "packaging/metadata/$_app_id.desktop" -t "$pkgdir/usr/share/applications/"
  install -Dm644 "packaging/metadata/$_app_id.metainfo.xml" -t "$pkgdir/usr/share/metainfo/"
  install -Dm644 "packaging/metadata/$_app_id.png" -t "$pkgdir/usr/share/pixmaps/"
  install -Dm644 "packaging/metadata/$_app_id.svg" -t "$pkgdir/usr/share/icons/hicolor/scalable/apps/"

  install -Dm644 README.md -t "$pkgdir/usr/share/doc/$pkgname"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
