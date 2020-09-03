#Maintainer: Janek Thomaschewski <janek@jbbr.net>

pkgname=rambox-bin
_pkgname=rambox
pkgver=0.7.6
pkgrel=1
pkgdesc='Free and Open Source messaging and emailing app that combines common web applications into one.'
arch=('i686' 'x86_64')
depends=('desktop-file-utils' 'bash' 'gtk3' 'libnotify' 'libxtst' 'libxss' 'libxkbcommon' 'libsecret' 'nss' 'libutil-linux')
provides=('rambox')
conflicts=('rambox')
url='http://rambox.pro/'
license=('GPL3')
source=("${_pkgname}.sh" "${_pkgname}.desktop" "${_pkgname}.png")
source_i686=("https://github.com/ramboxapp/community-edition/releases/download/$pkgver/Rambox-$pkgver-linux-ia32.tar.gz")
source_x86_64=("https://github.com/ramboxapp/community-edition/releases/download/$pkgver/Rambox-$pkgver-linux-x64.tar.gz")

sha256sums=('ee2573d62b580e8ee584335534976396761b5da53a009bccb881b9cf6cb2041d'
            '61ad70a929c402e24c79b8868208310f9b3c4d7801db2b791af38293231ee524'
            '0bf4d0c849ad6151f77b346fea0424fab910f434378f9890b16fd15a32a10064')
sha256sums_i686=('65045340f7a378aff8388d95c1d3d91dbc7d0701290c7efc5eca4bd6d2557bb5')
sha256sums_x86_64=('05bf245491ee81d36f055c9950c96c9dedd883dda585f48e1cfd83cb26f3e0d9')

# path after extraction
_path="Rambox-${pkgver}-linux"
# append architecture
[[ "$CARCH" = "i686" ]] && _path="${_path}-ia32"
[[ "$CARCH" = "x86_64" ]] && _path="${_path}-x64"

package() {
    install -d ${pkgdir}/{opt/rambox,usr/{bin,share/pixmaps}}
    cp -R ${srcdir}/${_path}/* ${pkgdir}/opt/${_pkgname}/

    # fix crash on some systems due to https://github.com/ramboxapp/community-edition/issues/2481
    chmod 4755 "${pkgdir}/opt/${_pkgname}/chrome-sandbox"

    install -Dm755 $srcdir/${_pkgname}.sh ${pkgdir}/usr/bin/${_pkgname}
    install -Dm644 $srcdir/${_pkgname}.png ${pkgdir}/usr/share/pixmaps/${_pkgname}.png
    desktop-file-install ${srcdir}/${_pkgname}.desktop --dir ${pkgdir}/usr/share/applications/
}
