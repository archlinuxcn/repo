# Maintainer: Carson Rueter <roachh at proton mail dot com>
# Maintainer: Icelk <main at icelk.dev>
# Contributor: Cameron Katri <katri.cameron@gmail.com>
# Contributor: Plague-doctor <plague <at>> privacyrequired <<dot>> com >
# Contributor: me at oguzkaganeren dot com dot tr
# Contributor: Rowisi < nomail <at> private <dot> com >

pkgname=vscodium-bin
_pkgname=VSCodium
pkgver=1.76.1.23069
pkgrel=2
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
            '87f687c1dfa66f390c63ac2717ba754e5b9babefb09e417312e089440eb15ab4')
sha256sums_x86_64=('d3240c42150333bf912048509f5c404434a72dadc4295d86041cb9636cb87c60')
sha256sums_aarch64=('0776b12520e5e52015f5952851c2280a532069adfb72ab6dfccd7c63cb75ff0d')
source=('vscodium-bin.desktop'
        'vscodium-bin-uri-handler.desktop'
        'vscodium-bin.install'
        'vscodium-bin.sh')
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
