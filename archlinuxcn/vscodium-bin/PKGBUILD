# Maintainer: Carson Rueter <roachh at proton mail dot com>
# Maintainer: Icelk <main at icelk.dev>
# Contributor: Cameron Katri <katri.cameron@gmail.com>
# Contributor: Plague-doctor <plague <at>> privacyrequired <<dot>> com >
# Contributor: me at oguzkaganeren dot com dot tr
# Contributor: Rowisi < nomail <at> private <dot> com >

pkgname=vscodium-bin
_pkgname=VSCodium
pkgver=1.80.1.23194
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

sha256sums=('eb5a62f83c034d10e2806b33003bfe4d27fdc28c663eb0b4c8a5e29faa14a7c7'
            '6eef345b65bf2679c928c763529540435ab9c6e1836917319810a7a2d484ae1b'
            'f746113e779ab0f5a21a7a2326ec43b0dc76b15cc38d06439f478326eb6609be'
            '741112ccfe1bfc5010f06031d7e4e4383e90ccd63965b464485d7f826f1942a6'
            '8a140c592e17063db1ccd6d232a66d5f8f8ec3d26c11928c69eb5e36a66da25b')
sha256sums_x86_64=('404f736e87866a8cc88a7a162dad5ac631af9849d05f936a30a67b955936dee9')
sha256sums_aarch64=('14674c67d1e6cf48f11b57c8393b6c03bd3fb9b1cfc6690a556c05bc2dae1427')
source=('vscodium-bin.desktop'
        'vscodium-bin-uri-handler.desktop'
        'vscodium-bin.install'
        'vscodium-bin.sh'
        'vscodium-bin-wayland.desktop')
source_x86_64=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-x64-${pkgver}.tar.gz")
source_aarch64=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-arm64-${pkgver}.tar.gz")

shopt -s extglob

package() {
  install -d -m755 ${pkgdir}/opt/${pkgname}
  install -d -m755 ${pkgdir}/usr/bin
  install -d -m755 ${pkgdir}/usr/share/{applications,pixmaps}
  cp -r ${srcdir}/!(vscodium-bin?(-uri-handler).desktop|${_pkgname}-linux-@(x|arm)64-${pkgver}.tar.gz) ${pkgdir}/opt/${pkgname}
  ln -s /opt/${pkgname}/bin/codium ${pkgdir}/usr/bin/codium
  ln -s /opt/${pkgname}/bin/codium ${pkgdir}/usr/bin/vscodium
  install -D -m644 ${srcdir}/vscodium-bin.desktop ${pkgdir}/usr/share/applications/codium.desktop
  install -D -m644 ${srcdir}/vscodium-bin-wayland.desktop ${pkgdir}/usr/share/applications/codium-wayland.desktop
  install -D -m644 ${srcdir}/vscodium-bin-uri-handler.desktop ${pkgdir}/usr/share/applications/codium-uri-handler.desktop
  install -D -m644 ${srcdir}/resources/app/resources/linux/code.png \
          ${pkgdir}/usr/share/pixmaps/vscodium.png
  install -m755 "${srcdir}/${pkgname}.sh" "${pkgdir}/usr/bin/codium"

  # Symlink shell completions
  install -d -m755 ${pkgdir}/usr/share/zsh/site-functions
  install -d -m755 ${pkgdir}/usr/share/bash-completion/completions
  ln -s /opt/${pkgname}/resources/completions/zsh/_codium ${pkgdir}/usr/share/zsh/site-functions
  ln -s /opt/${pkgname}/resources/completions/bash/codium ${pkgdir}/usr/share/bash-completion/completions
}
