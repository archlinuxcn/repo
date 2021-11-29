# Maintainer: Jaime Martínez Rincón <jaime@jamezrin.name>

pkgname=notion-app-enhanced
pkgver="2.0.16"
pkgrel=7
pkgdesc="The all-in-one workspace for your notes and tasks, but enhanced"
arch=('x86_64' 'aarch64')
url="https://github.com/notion-enhancer/notion-repackaged"
license=('MIT')

depends=(
  'c-ares'
  'ffmpeg'
  'gtk3'
  'http-parser'
  'libevent'
  'libvpx'
  'libxslt'
  'libxss'
  'minizip'
  'nss'
  're2'
  'snappy'
  'libnotify'
  'libappindicator-gtk3'
)
makedepends=()
provides=('notion-app')
conflicts=('notion-app')

notion_repackaged_ver="2.0.16-5"

source_x86_64=("${url}/releases/download/v${notion_repackaged_ver}/notion-app-enhanced-${notion_repackaged_ver}.pacman")
source_aarch64=("${url}/releases/download/v${notion_repackaged_ver}/notion-app-enhanced-${notion_repackaged_ver}-aarch64.pacman")
sha256sums_x86_64=('31d9cc4a8219241086fb2913d88d956567d220c4abe51573d357ac57b0b364c2')
sha256sums_aarch64=('712260918b4d1555e4ecdbc1d60930b7e25cc046ee771decb7d9bbda18d45032')

install=${pkgname}.install

package() {
  product_name="Notion Enhanced"
  package_name="notion-app-enhanced"  

  install -d "${pkgdir}/usr/bin"
  install -d "${pkgdir}/opt/${product_name}"

  cp -r "${srcdir}/opt/${product_name}" "${pkgdir}/opt/"

  icons_dir_path="usr/share/icons/hicolor"
  desktop_file_path="usr/share/applications/${package_name}.desktop"

  for icon_size_name in $(ls ${srcdir}/${icons_dir_path}); do
    icon_size_path="${icons_dir_path}/${icon_size_name}/apps"
    install -d "${pkgdir}/${icon_size_path}"
    install -m644 "${srcdir}/${icon_size_path}/${package_name}.png" \
                  "${pkgdir}/${icon_size_path}/${package_name}.png"
  done

  install -Dm644 "${srcdir}/${desktop_file_path}" "${pkgdir}/${desktop_file_path}"
}

