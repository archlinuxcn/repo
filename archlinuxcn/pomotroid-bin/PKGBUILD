# Maintainer: Victor Zamanian <victor.zamanian@gmail.com>

_pkgname=pomotroid
pkgname="${_pkgname}-bin"
pkgver=0.13.0
pkgrel=1
pkgdesc="Simple and visually-pleasing Pomodoro timer"
arch=('x86_64')
url="https://github.com/Splode/pomotroid"
license=('MIT')
depends=('zlib' 'hicolor-icon-theme')
options=(!strip)
source_x86_64=(
  "${url}/releases/download/v${pkgver}/${_pkgname}-${pkgver}-linux.tar.gz"
  "https://raw.githubusercontent.com/Splode/pomotroid/master/LICENSE"
  "${_pkgname}.desktop"
  "${_pkgname}.png"
)
md5sums_x86_64=('f8367a78ecb135496c54868863b34c15'
                '98368ac76439a0812a58d0a586b28ed1'
                '4276e15ba2505a034a80a272e9c9f0ed'
                '81ad82d2a70c058cb80a6ee7679c5f66')

package() {
    # Copy everything from tar
    install -dm755 "${pkgdir}/opt"
    cp -a "${srcdir}/${_pkgname}-${pkgver}-linux/" "${pkgdir}/opt/${_pkgname}"
    chmod 755 "${pkgdir}/opt/${_pkgname}"

    # Copy license
    install -Dm644 "${srcdir}/LICENSE" "${pkgdir}/opt/${_pkgname}/LICENSE"

    # Copy desktop file
    install -Dm644 "${srcdir}/${_pkgname}.desktop" \
      "${pkgdir}/usr/share/applications/${_pkgname}.desktop"

    # Icon images
    install -dm755 "${pkgdir}/usr/share/icons/hicolor/256x256/apps"
    install -Dm644 -t "${pkgdir}/usr/share/icons/hicolor/256x256/apps" \
      "${srcdir}/${_pkgname}.png"

    # Symlink executable
    install -dm755 "${pkgdir}/usr/bin"
    ln -s "/opt/${_pkgname}/${_pkgname}" "${pkgdir}/usr/bin/${_pkgname}"

    # Symlink license
    install -dm755 "${pkgdir}/usr/share/licenses/${_pkgname}"
    ln -s "/opt/${_pkgname}/LICENSE" "$pkgdir/usr/share/licenses/${_pkgname}"
}
