# Maintainer: Carson Rueter <roachh at proton mail dot com>
# Maintainer: Icelk <main at icelk.dev>
# Contributor: Cameron Katri <katri.cameron@gmail.com>
# Contributor: Plague-doctor <plague <at>> privacyrequired <<dot>> com >
# Contributor: me at oguzkaganeren dot com dot tr
# Contributor: Rowisi < nomail <at> private <dot> com >

pkgname=vscodium-bin
_pkgname=VSCodium
pkgver=1.62.0
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

sha256sums=('65e6b053e6d8be61763801312ded64a82cf835d77a6eabe1b9d7eb9e87b2e49b'
            'f26703924abca3738f2e1f84e5a1e27e8cc7dae4364bb53dbff03c2de5fe0898')
sha256sums_x86_64=('c9e61bcb4f5404c91ca048ccbf537c001d6feaf8b0359ac5320c3a824df8799f')
sha256sums_aarch64=('70526474b54606f97e6ba3c40543feaac853c99e1a0b1911f43d372a58f26d46')
sha256sums_armv7h=('478a28c0c994fde35a95e11eb520798d05867cb3bfe5d03268f173c4c89f431d')
source=('vscodium-bin.desktop'
        'vscodium-bin-uri-handler.desktop')
source_x86_64=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-x64-${pkgver}.tar.gz")
source_armv7h=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-armhf-${pkgver}.tar.gz")
source_aarch64=("https://github.com/VSCodium/vscodium/releases/download/${pkgver}/${_pkgname}-linux-arm64-${pkgver}.tar.gz")

shopt -s extglob

package() {
  install -d -m755 ${pkgdir}/usr/bin
  install -d -m755 ${pkgdir}/usr/share/{${pkgname},applications,pixmaps}
  cp -r ${srcdir}/!(vscodium-bin.desktop|${pkgname}-${pkgver}.tar.gz) ${pkgdir}/usr/share/${pkgname}
  ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/codium
  ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/vscodium
  install -D -m644 ${srcdir}/vscodium-bin.desktop ${pkgdir}/usr/share/applications/codium.desktop
  install -D -m644 ${srcdir}/vscodium-bin-uri-handler.desktop ${pkgdir}/usr/share/applications/codium-uri-handler.desktop
  install -D -m644 ${srcdir}/resources/app/resources/linux/code.png \
          ${pkgdir}/usr/share/pixmaps/vscodium.png
}
