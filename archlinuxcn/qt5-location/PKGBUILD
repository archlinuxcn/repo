# Maintainer: Felix Yan <felixonmars@archlinux.org>
# Contributor: Andrea Scarpino <andrea@archlinux.org>

pkgname=qt5-location
_basever=5.15.18
pkgver=5.15.18+kde+r7
pkgrel=2
_commit=ba48a8b5cedd157d972c08d371ac2581db166bf7
arch=('x86_64')
url='https://www.qt.io'
license=('GPL3' 'LGPL3' 'FDL' 'custom')
pkgdesc='Provides access to position, satellite and area monitoring classes'
depends=('qt5-declarative')
makedepends=('git')
groups=('qt5')
_pkgfqn=${pkgname/5-/}
source=(kde-$_pkgfqn::git+https://invent.kde.org/qt/qt/$_pkgfqn#commit=$_commit
        git+https://invent.kde.org/qt/qt/qtlocation-mapboxgl.git)
sha256sums=('4a6bfee705b322f4cd044949be217f822b9f697e5e1ec228fdc3f31c29558e13'
            'SKIP')

pkgver() {
  cd kde-$_pkgfqn
  echo "$_basever+kde+r"`git rev-list --count v$_basever-lts-lgpl..$_commit` | sed -e 's|+kde+r0||'
}

prepare() {
  mkdir -p build

  cd kde-$_pkgfqn
  git submodule init
  git submodule set-url src/3rdparty/mapbox-gl-native "$srcdir"/qtlocation-mapboxgl
  git -c protocol.file.allow=always submodule update
}

build() {
  cd build

  qmake ../kde-$_pkgfqn
  make
}

package() {
  cd build
  make INSTALL_ROOT="$pkgdir" install

  # Drop QMAKE_PRL_BUILD_DIR because reference the build dir
  find "$pkgdir/usr/lib" -type f -name '*.prl' \
    -exec sed -i -e '/^QMAKE_PRL_BUILD_DIR/d' {} \;

  install -d "$pkgdir"/usr/share/licenses
  ln -s /usr/share/licenses/qt5-base "$pkgdir"/usr/share/licenses/${pkgname}
}
