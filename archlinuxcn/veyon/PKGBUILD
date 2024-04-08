# Maintainer: sgar <swhaat in github>

pkgname=veyon
pkgver=4.8.3
pkgrel=1
pkgdesc="Cross-platform computer monitoring and classroom management"
arch=('x86_64')
url="https://veyon.io/"
license=('GPL2')
depends=('hicolor-icon-theme' 'libfakekey' 'libjpeg-turbo' 'libldap' 'libsasl'
         'libvncserver' 'libxcomposite' 'libxcursor' 'libxdamage' 'libxext'
         'libxfixes' 'libxinerama' 'libxrandr' 'libxtst' 'lzo' 'openssl' 'pam'
         'procps-ng' 'qca-qt6' 'qt6-base')
makedepends=('clang' 'cmake' 'git' 'qt6-declarative' 'qt6-httpserver' 'qt6-tools')
optdepends=('kldap: KDE support')
_commit=fd8f0ba1e5c1025e71abcebec5f17a186096b610  # tags/v4.8.3
source=("git+https://github.com/veyon/veyon.git#commit=${_commit}"
        'git+https://github.com/veyon/ultravnc.git'
        'git+https://invent.kde.org/pim/kldap.git'
        'git+https://github.com/veyon/libvncserver.git'
        'git+https://github.com/veyon/x11vnc.git'
        'git+https://github.com/veyon/libfakekey.git'
        'git+https://github.com/veyon/qthttpserver.git'
        'git+https://github.com/nodejs/http-parser.git'
        'git+https://github.com/novnc/noVNC.git'
        )
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

pkgver() {
  cd "$srcdir/$pkgname"
  git describe --tags | sed 's/^v//;s/-/+/g'
}

prepare() {
  cd "$srcdir/$pkgname"
  git submodule init
  git config submodule.3rdparty/ultravnc.url "$srcdir/ultravnc"
  git config submodule.3rdparty/kldap.url "$srcdir/kldap"
  git config submodule.3rdparty/libvncserver.url "$srcdir/libvncserver"
  git config submodule.3rdparty/x11vnc.url "$srcdir/x11vnc"
  git config submodule.3rdparty/libfakekey.url "$srcdir/libfakekey"
  git config submodule.3rdparty/qthttpserver.url "$srcdir/qthttpserver"
  git config submodule.3rdparty/kldap-qt-compat.url "$srcdir/kldap"
  git -c protocol.file.allow=always submodule update

  pushd 3rdparty/qthttpserver
  git submodule init
  git config submodule.src/3rdparty/http-parser.url "$srcdir/http-parser"
  git -c protocol.file.allow=always submodule update
  popd

  pushd 3rdparty/libvncserver
  git config submodule.webclients/novnc.url "$srcdir/noVNC"
  git -c protocol.file.allow=always submodule update
  popd
}

build() {
  cmake -B build -S "$pkgname" \
    -DCMAKE_BUILD_TYPE='RelWithDebInfo' \
    -DCMAKE_INSTALL_PREFIX='/usr' \
    -DSYSTEMD_SERVICE_INSTALL_DIR='/usr/lib/systemd/system' \
    -DWITH_QT6=ON -DVEYON_DEBUG=ON \
    -Wno-dev
  cmake --build build
}

package_veyon() {
  DESTDIR="$pkgdir" cmake --install build
}
