# Maintainer: Husam Bilal <husam212@gmail.com>
# Contributer: Manuel <manuel.bua@gmail.com>

pkgname=komorebi
pkgver=2.1
pkgrel=2
pkgdesc="Parallax backgrounds manager"
url="https://github.com/iabem97/komorebi"
depends=("desktop-file-utils" "glib2>=2.38" "gtk3>=3.14" "hicolor-icon-theme" "libgtop" "libgee" "libwnck" "clutter" "clutter-gtk" "clutter-gst" "webkit2gtk")
makedepends=("git" "cmake" "vala" "gendesk")
provides=("komorebi")
license=("GPL")
arch=("x86_64" "i686")
md5sums=("2fd707711373f77c45ea4583a40e56aa")
source=("https://github.com/iabem97/${pkgname}/archive/v${pkgver}.tar.gz")

prepare() {
  gendesk -f -n --pkgname "$pkgname" --pkgdesc "$pkgdesc" --exec="/usr/bin/komorebi"
  gendesk -f -n --pkgname "$pkgname-wallpaper-creator" --pkgdesc "$pkgdesc (wallpaper creator)" --exec="/usr/bin/komorebi-wallpaper-creator"
}

build() {
  _base_dir="${srcdir}/${pkgname}-${pkgver}"
  cd "$_base_dir"

  sed -i '/$ENV{HOME}/d' CMakeLists.txt
  find . -type f -exec sed -i 's|/System/Applications/|/usr/bin/|g' {} \;
  find . -type f -exec sed -i 's|/System/Resources/|/usr/share/|g' {} \;

  mkdir -p "$_base_dir/build"
  cd "$_base_dir/build"

  cmake "$_base_dir"
  make
}

package() {
  _base_dir="${srcdir}/${pkgname}-${pkgver}"

  cd "$_base_dir/build"
  make DESTDIR="$pkgdir/" install

  install -Dm644 "$_base_dir/data/Icons/komorebi.svg" "${pkgdir}/usr/share/pixmaps/${pkgname}.svg"
  install -Dm644 "${srcdir}/${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
}
