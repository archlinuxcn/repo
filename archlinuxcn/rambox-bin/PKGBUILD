# Maintainer: Janek Thomaschewski <janek@thomaschewski.dev>

pkgname=rambox-bin
_pkgname=Rambox
pkgver=0.7.9
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

sha256sums_i686=('d8a820b32152dfb8404522cdaeec44da40f0879b3945a7db7bbf6ca35b9a21b0')
sha256sums_x86_64=('04b9aaae7ced1e1ba71800bea861a45e57fed73a53923d263e7cb173a04c779f')

package() {
    # extract package data
    tar xf data.tar.xz -C "${pkgdir}"

    # install symbolic link in /usr/bin
    install -d -m755 "${pkgdir}/usr/bin"
    ln -s /opt/${_pkgname}/rambox "${pkgdir}/usr/bin"

    # fix crash on some systems due to https://github.com/ramboxapp/community-edition/issues/2481
    chmod 4755 "${pkgdir}/opt/${_pkgname}/chrome-sandbox"
}
