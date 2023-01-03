# Maintainer: Alexey Stukalov <astukalov@gmail.com>
# Contributor: Muflone http://www.muflone.com/contacts/english/

pkgname=smartgit
pkgver=22.1.2
pkgrel=1
pkgdesc='Git client with Hg and SVN support.'
arch=('any')
url="http://www.syntevo.com/smartgit"
license=('custom')
depends=('desktop-file-utils' 'git' 'gtk3' 'which')
optdepends=('mercurial: hg repositories support')
replaces=('smartgithg')

# package version as it appears in the name of tar.gz archive file
_pkgver=${pkgver//\./_}
# folder within tar.gz archive
_pkgfolder=${pkgname}
source=("https://www.syntevo.com/downloads/${pkgname}/${pkgname}-linux-${_pkgver}.tar.gz"
        "${pkgname}.desktop")
sha1sums=('87aab68c12fad7d54f327033ddf4ec65f830c203'
          'bafa47c0b43ad89aaa3b34a078771b3cd12bd1f3')

package() {
    # Install licenses
    install -d -m 755 "${pkgdir}/usr/share/licenses/${pkgname}"
    mv "${_pkgfolder}/licenses"/* "${pkgdir}/usr/share/licenses/${pkgname}"
    mv "${_pkgfolder}/license.html" "${pkgdir}/usr/share/licenses/${pkgname}"
    rmdir "${_pkgfolder}/licenses"
    # Install application files
    install -d -m 755 "${pkgdir}/opt"
    mv "${_pkgfolder}" "${pkgdir}/opt/${pkgname}"
    # Install desktop file
    install -D -m 644 "${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
    # Install icon files
    install -d -m 755 "${pkgdir}/usr/share/icons/hicolor"
    cd "${pkgdir}/usr/share/icons/hicolor"
    for _size in 32 48 64 128 256
    do
        install -d "${_size}x${_size}/apps"
        ln -s "/opt/${pkgname}/bin/smartgit-${_size}.png" "${_size}x${_size}/apps/${pkgname}.png"
    done
    # Add symlink to /usr/bin
    chmod 755 "${pkgdir}/opt/${pkgname}/bin/smartgit.sh"
    install -d -m 755 "${pkgdir}/usr/bin"
    ln -s "/opt/${pkgname}/bin/smartgit.sh" "${pkgdir}/usr/bin/${pkgname}"
}
