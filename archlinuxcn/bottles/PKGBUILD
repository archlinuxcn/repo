# Maintaner: Francesco Masala <mail@francescomasala.me>
# Contributor: Francesco Masala <mail@francescomasala.me>

pkgname=bottles
pkgver=51.11
pkgrel=2
epoch=2
pkgdesc='Easily manage wine and proton prefix'
arch=('x86_64')
url="https://github.com/bottlesdevs/Bottles"
license=('GPL3')
depends=(
  'cabextract'
  'dconf'
  'fvs'
  'gtk4'
  'gtksourceview5'
  'hicolor-icon-theme'
  'icoextract'
  'imagemagick'
  'lib32-gnutls'
  'libadwaita'
  'libhandy'
  'libportal-gtk4'
  'p7zip'
  'patool'
  'python'
  'python-chardet'
  'python-gobject'
  'python-markdown'
  'python-orjson'
  'python-pathvalidate'
  'python-pycurl'
  'python-requests'
  'python-steamgriddb'
  'python-yaml'
  'webkit2gtk'
  'xorg-xdpyinfo'
  'vkbasalt-cli'
)
optdepends=(
  'gamemode'
  'gvfs' 
  'lib32-vkd3d' 
  'lib32-vulkan-icd-loader' 
  'vkd3d'
  'vulkan-icd-loader'
  'wine'
)
makedepends=('meson' 'ninja' 'blueprint-compiler')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/bottlesdevs/Bottles/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('3e438e98fdc3821e250a0c583e74d203e7c05511c0892587a5a29dd886392f3c')

build() {
  if [[ -d Bottles ]]; then 
        rm -rf Bottles
  fi;
  mv Bottles*/ Bottles/
  cd "Bottles"
  meson --prefix='/usr' build
  ninja -C build
}

package() {
  cd "Bottles"
  DESTDIR="${pkgdir}" ninja -C build install
}
