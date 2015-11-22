# Maintainer: Adam Reichold <adam.reichold@t-online.de>

pkgname=qpdfview
pkgver=0.4.16
pkgrel=2
pkgdesc='A tabbed PDF viewer using the poppler library.'
arch=('i686' 'x86_64' 'armv7h')
url='https://launchpad.net/qpdfview'
license=('GPL2')
depends=('libcups' 'poppler-qt5' 'qt5-svg' 'desktop-file-utils' 'hicolor-icon-theme')
optdepends=('libspectre: for PostScript support (required at build time)' 'djvulibre: for DjVu support (required at build time)')
makedepends=('qt5-tools')
install='qpdfview.install'
source=("https://launchpad.net/$pkgname/trunk/$pkgver/+download/$pkgname-$pkgver.tar.gz")
sha256sums=('fad416e8fefc3057fa1b8d12d964c7eccd16dffe0307a0d6e9d55a543294da7f')

build() {
  cd "$srcdir/$pkgname-$pkgver"
  
  if ! pkg-config --exists libspectre; then
    local config="$config without_ps"
  fi
  
  if ! pkg-config --exists ddjvuapi; then
    local config="$config without_djvu"
  fi

  lrelease-qt5 qpdfview.pro
  qmake-qt5 "CONFIG+=$config" qpdfview.pro
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"

  make "INSTALL_ROOT=$pkgdir" install
}

