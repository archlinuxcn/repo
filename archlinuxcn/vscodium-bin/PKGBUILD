# Maintainer: Carson Rueter <swurl at swurl dot x y z>
# Maintainer: Icelk <main at icelk.dev>
# Contributor: Cameron Katri <katri.cameron@gmail.com>
# Contributor: Plague-doctor <plague <at>> privacyrequired <<dot>> com >
# Contributor: me at oguzkaganeren dot com dot tr
# Contributor: Rowisi < nomail <at> private <dot> com >

pkgname=vscodium-bin
_pkgname=VSCodium
pkgver=1.90.0.24158
pkgrel=1
pkgdesc="Binary releases of VS Code without MS branding/telemetry/licensing."
arch=('x86_64' 'aarch64')
url="https://github.com/VSCodium/vscodium"
license=('MIT')
depends=(
        fontconfig libxtst gtk3 python cairo alsa-lib nss gcc-libs libnotify libxss
        'glibc>=2.28-4' bash
        )
optdepends=(
        'gvfs: For move to trash functionality'
        'libdbusmenu-glib: For KDE global menu'
)
provides=('vscode' 'codium' 'vscodium')
conflicts=('vscodium')
install=$pkgname.install

sha256sums=('3a5bc109974fcf408855c13965f6d6be0997655c5b359de0bfd19a678c00844e'
            '6eef345b65bf2679c928c763529540435ab9c6e1836917319810a7a2d484ae1b'
            '01ba3d33e76804e2346d08f4eda256a29610c9eb59432e4b016d05ad93d901ba'
            '63b9f3e07dcfe92f59e851fdeeaed6ee986950672f75cc950489bce67e85d884'
            'ef5759114cb0bada639bf89b778679bc7cf4d829151dc5fbf95eb33df4addcd6')
sha256sums_x86_64=('6b7b7e0333b455c77adba7a6c4f7c1d1c0138d717ba65216ae4b5b0d9bdaaffe')
sha256sums_aarch64=('cb07fabb6feea9f91c329f1b8a77b46782ef4dbcca4b73a7ff6a25330c444858')

source=('vscodium-bin.desktop'
        'vscodium-bin-uri-handler.desktop'
        'vscodium-bin.install'
        'vscodium-bin.sh'
        'vscodium-bin-wayland.desktop')
source_x86_64=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-x64-${pkgver}.tar.gz")
source_aarch64=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-arm64-${pkgver}.tar.gz")

shopt -s extglob

package() {
  install -d -m755 "${pkgdir}/opt/${pkgname}"
  install -d -m755 "${pkgdir}/usr/bin"
  install -d -m755 "${pkgdir}/usr/share/"{applications,pixmaps}
  cp -r "${srcdir}"/!(vscodium-bin?(-uri-handler).desktop|${_pkgname}-linux-@(x|arm)64-${pkgver}.tar.gz) "${pkgdir}/opt/${pkgname}"
  ln -s "/opt/${pkgname}/bin/codium" "${pkgdir}/usr/bin/codium"
  ln -s "/opt/${pkgname}/bin/codium" "${pkgdir}/usr/bin/vscodium"
  install -D -m644 "${srcdir}/vscodium-bin.desktop" "${pkgdir}/usr/share/applications/codium.desktop"
  install -D -m644 "${srcdir}/vscodium-bin-wayland.desktop" "${pkgdir}/usr/share/applications/codium-wayland.desktop"
  install -D -m644 "${srcdir}/vscodium-bin-uri-handler.desktop" "${pkgdir}/usr/share/applications/codium-uri-handler.desktop"
  install -D -m644 "${srcdir}/resources/app/resources/linux/code.png" \
          "${pkgdir}/usr/share/pixmaps/vscodium.png"
  install -m755 "${srcdir}/${pkgname}.sh" "${pkgdir}/usr/bin/codium"

  # Symlink shell completions
  install -d -m755 "${pkgdir}/usr/share/zsh/site-functions"
  install -d -m755 "${pkgdir}/usr/share/bash-completion/completions"
  ln -s "/opt/${pkgname}/resources/completions/zsh/_codium" "${pkgdir}/usr/share/zsh/site-functions"
  ln -s "/opt/${pkgname}/resources/completions/bash/codium" "${pkgdir}/usr/share/bash-completion/completions"
}
