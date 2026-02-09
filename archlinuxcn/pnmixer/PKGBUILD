# Maintainer: Vincent PRELAT <vincent@prelat.fr>
# Contributor: Brian Bidulock <bidulock@openss7.org>
pkgname=pnmixer
pkgver=0.7.2
pkgrel=2
pkgdesc="GTK volume mixer applet that runs in the system tray."
arch=('i686' 'x86_64')
license=('GPL')
url="https://github.com/nicklan/pnmixer"
makedepends=('intltool' 'cmake')
depends=('gtk3' 'alsa-utils' 'libnotify')
source=("https://github.com/nicklan/pnmixer/releases/download/v${pkgver}/pnmixer-v${pkgver}.tar.gz" 
        "cmake3.10.diff::https://github.com/nicklan/pnmixer/commit/3a4a988f6c69abece44fe2c77eab5f0a9ae7bbd2.diff")
md5sums=('e9f17f56c50de39393030a96e343427b'
         '3149765d37e7324596dce37b8669bf80')


prepare() {
  # patch cmake_minimum_required
  # https://github.com/nicklan/pnmixer/pull/197
  cd "$pkgname-v$pkgver"
  patch --forward --strip=1 --input=${srcdir}/cmake3.10.diff
}

build() {
  cd "$pkgname-v$pkgver"
  cmake \
    -S . \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_SKIP_RPATH=ON \
    -DWITH_GTK3=ON
  make
}
package() {
  cd "$pkgname-v$pkgver"
  make DESTDIR="$pkgdir" install
}
