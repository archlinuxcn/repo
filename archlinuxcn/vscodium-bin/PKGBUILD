# Maintainer: Plague-doctor <plague <at>> privacyrequired <<dot>> com >
# Contributor: me at oguzkaganeren dot com dot tr
# Contributor: Rowisi < nomail <at> private <dot> com >

pkgname=vscodium-bin
pkgver=1.43.0
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
provides=('code')
conflicts=('code')
source=(vscodium-bin.desktop)
sha256sums=('5504e93bd55f2bc068c29e4fa962c1eddc6e08edb39c3255319dd5ad998a1b86')

source_x86_64=("${pkgname}-${pkgver}-${pkgrel}-x86_64.tar.gz::${url}/releases/download/${pkgver}/VSCodium-linux-x64-${pkgver}.tar.gz")
source_aarch64=("${pkgname}-${pkgver}-${pkgrel}-aarch64.tar.gz::${url}/releases/download/${pkgver}/VSCodium-linux-arm64-${pkgver}.tar.gz")
source_armv7h=("${pkgname}-${pkgver}-${pkgrel}-armv7h.tar.gz::${url}/releases/download/${pkgver}/VSCodium-linux-arm-${pkgver}.tar.gz")

sha256sums_x86_64=('6ae5c32f0968d93570a7acf3262cb44fb2dd5dba6c6e6133bb1433daa3c23a8d')
sha256sums_aarch64=('e041328109cd2dc99427437031380618ac322639b9171ef61eab6c65128752e6')
sha256sums_armv7h=('8c7d4cb7c75285d028ec1edcaeee2a25b1a945064308abd0dbed6a9bf91888a6')

noextract=("${pkgname}-${pkgver}-${pkgrel}-${CARCH}.tar.gz")

prepare() {
    mkdir -p ${srcdir}/${pkgname}
    tar -xf ${srcdir}/${pkgname}-${pkgver}-${pkgrel}-${CARCH}.tar.gz -C ${srcdir}/${pkgname}
}

package() {
    install -d -m755 ${pkgdir}/usr/bin
    install -d -m755 ${pkgdir}/usr/share/{${pkgname},applications,pixmaps}
    cp -r ${srcdir}/${pkgname} ${pkgdir}/usr/share
    ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/code
    ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/codium
    ln -s /usr/share/${pkgname}/bin/codium ${pkgdir}/usr/bin/vscodium
    install -D -m644 vscodium-bin.desktop ${pkgdir}/usr/share/applications/${pkgname}.desktop
    install -D -m644 ${srcdir}/${pkgname}/resources/app/resources/linux/code.png \
            ${pkgdir}/usr/share/pixmaps/vscodium.png
}
