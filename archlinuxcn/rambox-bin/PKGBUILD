# Maintainer: Janek Thomaschewski <janek@thomaschewski.dev>

pkgname=rambox-bin
_pkgname=Rambox
pkgver=0.7.8
pkgrel=1
pkgdesc='Free and Open Source messaging and emailing app that combines common web applications into one.'
arch=('i686' 'x86_64')
depends=('desktop-file-utils' 'gtk3' 'libappindicator-gtk3' 'libnotify' 'libxtst' 'libxss' 'libxkbcommon' 'libsecret' 'nss' 'libutil-linux')
provides=('rambox')
conflicts=('rambox')
url='http://rambox.pro/'
license=('GPL3')

source_i686=("https://github.com/ramboxapp/community-edition/releases/download/$pkgver/${_pkgname}-$pkgver-linux-i386.deb")
source_x86_64=("https://github.com/ramboxapp/community-edition/releases/download/$pkgver/${_pkgname}-$pkgver-linux-amd64.deb")

sha256sums_i686=('0c27893080b0ca6b0360bf744dc78cba85e3c1b8a05d7e7e654cc12d2c5be6c9')
sha256sums_x86_64=('520b5a3a95b315c30477d5f0e1c8c10ad0829f7861fe3aa211f97da1d2f38fa3')

package() {
    # extract package data
    tar xf data.tar.xz -C "${pkgdir}"

    # install symbolic link in /usr/bin
    install -d -m755 "${pkgdir}/usr/bin"
    ln -s /opt/${_pkgname}/rambox "${pkgdir}/usr/bin"

    # fix crash on some systems due to https://github.com/ramboxapp/community-edition/issues/2481
    chmod 4755 "${pkgdir}/opt/${_pkgname}/chrome-sandbox"
}
