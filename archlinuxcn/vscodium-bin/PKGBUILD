# Maintainer: Carson Rueter <roachh at proton mail dot com>
# Maintainer: Icelk <main at icelk.dev>
# Contributor: Cameron Katri <katri.cameron@gmail.com>
# Contributor: Plague-doctor <plague <at>> privacyrequired <<dot>> com >
# Contributor: me at oguzkaganeren dot com dot tr
# Contributor: Rowisi < nomail <at> private <dot> com >

pkgname=vscodium-bin
_pkgname=VSCodium
pkgver=1.66.2
pkgrel=1
pkgdesc="Binary releases of VS Code without MS branding/telemetry/licensing."
arch=('x86_64' 'aarch64' 'armv7h')
url="https://github.com/VSCodium/vscodium"
license=('MIT')
depends=(
        fontconfig libxtst gtk3 python cairo alsa-lib nss gcc-libs libnotify libxss
        'glibc>=2.28-4'
        )
optdepends=(
        'gvfs: For move to trash functionality'
        'libdbusmenu-glib: For KDE global menu'
)
provides=('codium' 'vscodium')
conflicts=('vscodium' 'vscodium-git')

sha256sums=('a665ef6e2a1711df2552d7ae49fd7f30f7a2d7e0dea71c7c5f4c90764d8c37ce'
            'fd6b46c021e4f0b75d27fcf67481019dbbaa7059ea186437a47a6b6ae8bb574f')
sha256sums_x86_64=('f682b11a39c9e65949a297fdd3d9fef6b472d7084f47eb5813cb7814468fe6c4')
sha256sums_aarch64=('41d449cb64a65f7eeee4bac9190410d77f1a56540633c5b769276c617174518e')
sha256sums_armv7h=('a42a6ad9fb8ccb2470e1230b275cd1cb3b138675403771f5539ab9aa998e19fe')
source=('vscodium-bin.desktop'
        'vscodium-bin-uri-handler.desktop')
source_x86_64=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-x64-${pkgver}.tar.gz")
source_armv7h=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-armhf-${pkgver}.tar.gz")
source_aarch64=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-arm64-${pkgver}.tar.gz")

shopt -s extglob

package() {
  install -d -m755 ${pkgdir}/opt/${pkgname}
  install -d -m755 ${pkgdir}/usr/bin
  install -d -m755 ${pkgdir}/usr/share/{applications,pixmaps}
  cp -r ${srcdir}/!(vscodium-bin.desktop|${pkgname}-${pkgver}.tar.gz) ${pkgdir}/opt/${pkgname}
  ln -s /opt/${pkgname}/bin/codium ${pkgdir}/usr/bin/codium
  ln -s /opt/${pkgname}/bin/codium ${pkgdir}/usr/bin/vscodium
  install -D -m644 ${srcdir}/vscodium-bin.desktop ${pkgdir}/usr/share/applications/codium.desktop
  install -D -m644 ${srcdir}/vscodium-bin-uri-handler.desktop ${pkgdir}/usr/share/applications/codium-uri-handler.desktop
  install -D -m644 ${srcdir}/resources/app/resources/linux/code.png \
          ${pkgdir}/usr/share/pixmaps/vscodium.png
}
