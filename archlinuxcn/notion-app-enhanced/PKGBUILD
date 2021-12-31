# Maintainer: Jaime Martínez Rincón <jaime@jamezrin.name>

pkgname=notion-app-enhanced
pkgver="2.0.18"
pkgrel=1
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

notion_repackaged_ver="2.0.18-1"

source_x86_64=("${url}/releases/download/v${notion_repackaged_ver}/notion-app-enhanced-${notion_repackaged_ver}.pacman")
source_aarch64=("${url}/releases/download/v${notion_repackaged_ver}/notion-app-enhanced-${notion_repackaged_ver}-aarch64.pacman")
sha256sums_x86_64=('aba41faada6db57fdaeff3ef2f1e866da5a59eb698bf3acbc14095f1b1976b56')
sha256sums_aarch64=('b625742ab9ecdf3e0365a23754e48f2c9ea872a22e7c2871ed20c8d539fd5f86')

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

