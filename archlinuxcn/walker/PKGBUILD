# Maintainer: Andrej Benz <hello[at]benz[dot]dev>

pkgname=walker
pkgver=0.12.30
pkgrel=1
pkgdesc='wayland application runner'
url='https://github.com/abenz1267/walker'
arch=('x86_64')
license=('MIT')
makedepends=('go' 'gobject-introspection')
depends=('gtk4-layer-shell' 'libvips' 'ffmpeg')
optdepends=('wl-clipboard: for clipboard module' 'libqalculate: for calculator module')
conflicts=('walker')
provides=('walker')
source=("${url}/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('36f2cea61c2dca0aa2fda51b32bd022d341e942c888f67e8a98ab3b34b261ec3')
b2sums=('c0267ecab3bd236abd4b29ab5069915125dc6f4f8d354de787a8aa6ac4698cdc06854d11a34e496fa54857668891f324523e6f93bc4f9ae8a7ef60570cb3db3b')

build() {
  cd ${pkgname}-${pkgver}/cmd

  go build -x -o walker
}

package() {
  cd ${pkgname}-${pkgver}/cmd
  install -Dm 755 walker -t "${pkgdir}/usr/bin"

  cd ../
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"

  cd internal/config
  install -Dm 644 config.default.toml -t "${pkgdir}/etc/xdg/walker"
  mv "${pkgdir}/etc/xdg/walker/config.default.toml" "${pkgdir}/etc/xdg/walker/config.toml"

  cd themes
  install -Dm 644 default.toml -t "${pkgdir}/etc/xdg/walker/themes"

  install -Dm 644 xdg_default.css -t "${pkgdir}/etc/xdg/walker/themes"
  mv "${pkgdir}/etc/xdg/walker/themes/xdg_default.css" "${pkgdir}/etc/xdg/walker/themes/default.css"
}
