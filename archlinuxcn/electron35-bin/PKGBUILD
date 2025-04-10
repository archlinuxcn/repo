# Maintainer: zxp19821005 <zxp19821005 at 163 dot com>
# Co-maintainer: Yurii Kolesnykov <root@yurikoles.com>
# Based on extra/electron* by
# Bruno Pagani <archange@archlinux.org>
# Caleb Maclennan <caleb@alerque.com>
_projectname=electron
_major=35
_pkgname="${_projectname}${_major}"
pkgname="${_pkgname}-bin"
_subver='1.5'
_pkgver="${_major}.${_subver}"
pkgver="${_pkgver/-}"
pkgrel=1
pkgdesc="Build cross platform desktop apps with web technologies — prebuilt"
arch=(
    'aarch64'
    'armv7h'
    'x86_64'
)
url='https://electronjs.org'
_ghurl="https://github.com/electron/electron"
license=(
    'MIT'
    'LicenseRef-custom'
)
provides=(
    "${_pkgname}=${pkgver}"
)
conflicts=("${_pkgname}")
depends=(
    'alsa-lib'
    'gtk3'
    'nss'
)
optdepends=(
    'kde-cli-tools: file deletion support (kioclient5)'
    'pipewire: WebRTC desktop sharing under Wayland'
    'qt6-base: enable Qt6 with --enable-features=AllowQt'
    'gtk4: for --gtk-version=4 (GTK4 IME might work better on Wayland)'
    'trash-cli: file deletion support (trash-put)'
    "xdg-utils: open URLs with desktop's default (xdg-email, xdg-open)"
)
noextract=(
    "${_pkgname}-chromedriver-${pkgver}-${CARCH}.zip"
    "${_pkgname}-${pkgver}-${CARCH}.zip"
)
source_aarch64=(
    "${_pkgname}-chromedriver-${pkgver}-aarch64.zip::${_ghurl}/releases/download/v${_pkgver}/chromedriver-v${_pkgver}-linux-arm64.zip"
    "${_pkgname}-${pkgver}-aarch64.zip::${_ghurl}/releases/download/v${_pkgver}/electron-v${_pkgver}-linux-arm64.zip"
)
source_armv7h=(
    "${_pkgname}-chromedriver-${pkgver}-armv7h.zip::${_ghurl}/releases/download/v${_pkgver}/chromedriver-v${_pkgver}-linux-armv7l.zip"
    "${_pkgname}-${pkgver}-armv7h.zip::${_ghurl}/releases/download/v${_pkgver}/electron-v${_pkgver}-linux-armv7l.zip"
)
source_x86_64=(
    "${_pkgname}-chromedriver-${pkgver}-x86_64.zip::${_ghurl}/releases/download/v${_pkgver}/chromedriver-v${_pkgver}-linux-x64.zip"
    "${_pkgname}-${pkgver}-x86_64.zip::${_ghurl}/releases/download/v${_pkgver}/electron-v${_pkgver}-linux-x64.zip"
)
sha256sums_aarch64=('4d6d45aa412b208778b96e32f962280daaadb9665dc741de65b1a843dbf293fa'
                    '9c987b7c2eb1fab7088164203fa639878f96354f3ed71cfe6dca83449589d4b4')
sha256sums_armv7h=('823a47c6ba61833bba0cf19fe9f708559a9278c00ae45f3cf69b2f857f6401ac'
                   '261c43e4a2c174753803ac1e1a008408c5911db4c40fa26905decf213edbc814')
sha256sums_x86_64=('d727308b69df75bdfdf893f39128f68b8bbac31ad292536cf0480b6e38e0488d'
                   'c535af79229be495900cf6b3a3ea0c0e76676d49743e68cfa1b9e76f602c62c7')
prepare() {
    install -Dm755 -d "${srcdir}/${_pkgname}"
    bsdtar -xf "${srcdir}/${_pkgname}-${pkgver}-${CARCH}.zip" -C "${srcdir}/${_pkgname}"
    bsdtar -xf "${srcdir}/${_pkgname}-chromedriver-${pkgver}-${CARCH}.zip" -C "${srcdir}/${_pkgname}"
    rm -rf "${srcdir}/${_pkgname}/"{gen,chromedriver.debug}
    chmod u+s "${srcdir}/${_pkgname}/chrome-sandbox"
}
package() {
    install -Dm755 -d "${pkgdir}/usr/"{bin,lib}
    cp -r --no-preserve=ownership --preserve=mode "${srcdir}/${_pkgname}" "${pkgdir}/usr/lib"
    ln -nfs "/usr/lib/${_pkgname}/${_projectname}" "${pkgdir}/usr/bin/${_pkgname}"
    install -Dm644 "${srcdir}/${_pkgname}/LICENSE"* -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
