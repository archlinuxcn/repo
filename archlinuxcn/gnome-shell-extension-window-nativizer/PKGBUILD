# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=gnome-shell-extension-window-nativizer
pkgver=0.11.2
pkgrel=1
pkgdesc='Seamlessly nativize non-native applications into the GNOME desktop'
arch=('any')
url='https://github.com/everyx/gnome-shell-extension-window-nativizer'
license=('GPL-2.0-or-later')
depends=('gnome-shell>=50' 'dconf')
makedepends=('gnome-shell' 'gettext' 'pnpm' 'nodejs')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('0bab6dd1819518ad8755ff04463b4ff0c526e55cc4ba9b7d2512bf1f1dd8828644866de3fee7c5b032f55d8591a23519cd8cded0b5a92f8eb1808a754f09fbcf')

build() {
    cd "${pkgname}-${pkgver}"

    pnpm install --prod --ignore-scripts
    pnpm run build
}

package() {
    cd "${pkgname}-${pkgver}"

    local _uuid='window-nativizer@everyx.github.io'
    local _ext_dir="${pkgdir}/usr/share/gnome-shell/extensions/${_uuid}"

    install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}/"

    install -d "${_ext_dir}"
    bsdtar --uid 0 --gid 0 -xf "dist/${_uuid}.shell-extension.zip" -C "${_ext_dir}"

    install -Dm644 "${_ext_dir}/schemas/"*.gschema.xml -t "${pkgdir}/usr/share/glib-2.0/schemas/"
    rm -rf "${_ext_dir}/schemas"

    mv "${_ext_dir}/locale" "${pkgdir}/usr/share/locale"
}
