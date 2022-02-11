# Maintainer: Carson Rueter <roachh at proton mail dot com>
# Maintainer: Icelk <main at icelk.dev>
# Contributor: Cameron Katri <katri.cameron@gmail.com>
# Contributor: Plague-doctor <plague <at>> privacyrequired <<dot>> com >
# Contributor: me at oguzkaganeren dot com dot tr
# Contributor: Rowisi < nomail <at> private <dot> com >

pkgname=vscodium-bin
_pkgname=VSCodium
pkgver=1.64.2
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
sha256sums_x86_64=('682ea0170d5e533dd2bd93f8e2deaad826339a1e46bea6e4be362d7b32b9ae51')
sha256sums_aarch64=('06e25b4bdb1f48885b3c3780328b0700fb83a0807d6c0e9c022b87f27ff7aea8')
sha256sums_armv7h=('5594b22a6f624d5b99f710d4b05f135e0b54a7eb13179f3fe42614b514887e15')
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
