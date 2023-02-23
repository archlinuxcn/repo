# Maintainer: S Stewart <tda@null.net>
# Maintainer: Cranky Supertoon <crankysupertoon@gmail.com>
# Special thanks to RyanTheAllmighty for making hyper-appimage
pkgname="gdlauncher-bin"
_pkgname="gdlauncher"
pkgver="1.1.30"
pkgrel=1
arch=('x86_64')
pkgdesc="GDLauncher is simple, yet powerful Minecraft custom launcher with a strong focus on the user experience"
url="https://gdevs.io"
license=('GPL3')
makedepends=('tar' 'xz')
depends=('libnotify' 'libxss' 'libxtst' 'libindicator-gtk3' 'libappindicator-gtk3')
provides=('gdlauncher')
conflicts=('gdlauncher' 'gdlauncher-beta' 'gdlauncher-beta-bin' 'gdlauncher-appimage' 'gdlauncher-git' 'gdlauncher-classic')
source_x86_64=("GDLauncher-${pkgver}.deb::https://github.com/gorilla-devs/GDLauncher/releases/download/v${pkgver}/GDLauncher-linux-setup.deb")
md5sums_x86_64=('1253e2cdb07104000094f16df1d55cdb')

package() {
    # Extract data folder from .deb archive
    tar xf "${srcdir}/data.tar.xz" --directory=$pkgdir

    # fix file permissions - all files as 644 - directories as 755
    find "${pkgdir}/"{opt,usr} -type d -exec chmod 755 {} \;
    find "${pkgdir}/"{opt,usr} -type f -exec chmod 644 {} \;

    # make sure the main and 7za binary have the right permissions
    chmod a+x "${pkgdir}/opt/GDLauncher/"{${_pkgname},7za}

    # link the binary
    install -d -m755 "${pkgdir}/usr/bin/"
    ln -sr "${pkgdir}/opt/GDLauncher/${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"
}
