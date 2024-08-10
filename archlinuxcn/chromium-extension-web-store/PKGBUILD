# Maintainer: Jerry Xiao <aur@mail.jerryxiao.cc>

_id=ocaahdebbfolfmndjeplogmgcagdmblk
pkgname=chromium-extension-web-store
pkgver=1.5.4.3
pkgrel=1
pkgdesc="chromium web store extension (for ungoogled-chromium)"
arch=('any')
url="https://github.com/NeverDecaf/chromium-web-store"
license=('MIT')
optdepends=("ungoogled-chromium")
source=("${pkgname}-${pkgver}.crx::${url}/releases/download/v${pkgver}/Chromium.Web.Store.crx")
noextract=("${pkgname}-${pkgver}.crx")
sha256sums=('80a01caef9f12e1f6032b693157e3346c52e6b8388fa56a4e75829208dbd77c8')
install=chromium-extension-web-store.install

prepare() {
    # Create extension json
    cat << EOF > "${_id}".json
{
    "external_crx": "/usr/lib/${pkgname}/${pkgname}-${pkgver}.crx",
    "external_version": "${pkgver}"
}
EOF
}

package() {
    install -Dm644 -t "${pkgdir}/usr/share/chromium/extensions/" "${_id}.json"
    install -Dm644 -t "${pkgdir}/usr/lib/${pkgname}/" "${pkgname}-${pkgver}.crx"
}
