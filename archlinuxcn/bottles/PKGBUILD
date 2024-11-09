# Maintaner: Francesco Masala <mail@francescomasala.me>
# Contributor: lotation <xlapsiu@gmail.com>

pkgname=bottles
pkgver=51.15
pkgrel=2
epoch=2
pkgdesc='Easily manage wine and proton prefix'
arch=(any)
url="https://github.com/bottlesdevs/Bottles"
license=('GPL-3.0-only')
depends=(
  'cabextract'
  'dconf'
  'gtk4'
  'gtksourceview5'
  'hicolor-icon-theme'
  'icoextract'
  'imagemagick'
  'libadwaita'
  'libportal-gtk4'
  'p7zip'
  'patool'
  'python'
  'python-chardet'
  'python-fvs'
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
  'lib32-gnutls'
  'lib32-vkd3d' 
  'lib32-vulkan-icd-loader' 
  'vkd3d'
  'vulkan-icd-loader'
  'wine'
)
makedepends=('meson' 'ninja' 'blueprint-compiler')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/bottlesdevs/Bottles/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('f31cc20c10242a1e4df462de28a353429154e2f62e7ed0a36b62740fecb47360')

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

