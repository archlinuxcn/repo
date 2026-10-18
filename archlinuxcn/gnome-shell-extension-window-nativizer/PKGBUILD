# Maintainer: Gavin Luo <lunt.luo@gmail.com>

pkgname=gnome-shell-extension-window-nativizer
pkgver=0.11.0
pkgrel=1
pkgdesc='Seamlessly nativize non-native applications into the GNOME desktop'
arch=('any')
url='https://github.com/everyx/gnome-shell-extension-window-nativizer'
license=('GPL-2.0-or-later')
depends=('gnome-shell>=50' 'dconf')
makedepends=('gnome-shell' 'gettext' 'pnpm' 'nodejs')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz")
b2sums=('9ce824f6632ec5e33d215c9a1cc624c436f3496655903956ebd85df630a84091fc868ef2938fa5c6e74f3760fffac4fc662fc6f136cfb45e6ba68c18843280c8')

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
