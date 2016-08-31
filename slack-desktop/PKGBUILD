# Maintainer: "Amhairghin" Oscar Garcia Amor (https://ogarcia.me)
# Contributor: Simon Gomizelj <simongmzlj(at)gmail(dot)com>
# Contributor: Kyle Manna <kyle(at)kylemanna(dot)com>

pkgname=slack-desktop
pkgver=2.1.2
pkgrel=1
pkgdesc="Slack Desktop (Beta) for Linux"
arch=('i686' 'x86_64')
url="https://slack.com/downloads"
license=('custom')
depends=('alsa-lib' 'expat' 'gconf' 'gtk2' 'gvfs' 'hunspell' 'hunspell-en' 'libgcrypt' 'libgnome-keyring' 'libnotify' 'libxss' 'libxtst' 'xdg-utils')
optdepends=('gnome-keyring')

source_x86_64=("https://downloads.slack-edge.com/linux_releases/${pkgname}-${pkgver}-amd64.deb")
source_i686=("https://downloads.slack-edge.com/linux_releases/${pkgname}-${pkgver}-i386.deb")

sha256sums_x86_64=('46576dbe929d4d60d0311056c0268d22dfaa58edc6774ce8a7e61873414bbf2e')
sha256sums_i686=('cc9660d95f5ce765c18b35191e2475d6bd272affc6d47f176759cc202910ddb4')

package() {
    bsdtar -O -xf "slack-desktop-${pkgver}"*.deb data.tar.xz | bsdtar -C "$pkgdir" -xJf -

    # Permission fix
    find "${pkgdir}" -type d -exec chmod 755 {} +

    # Remove all unnecessary stuff
    rm -rf "${pkgdir}/etc"
    rm -rf "${pkgdir}/usr/share/lintian"
    rm -rf "${pkgdir}/usr/share/doc"

    # Move license
    install -dm755 ${pkgdir}/usr/share/licenses/${pkgname}
    mv ${pkgdir}/usr/lib/slack/LICENSE ${pkgdir}/usr/share/licenses/${pkgname}
    ln -s /usr/share/licenses/${pkgname}/LICENSE ${pkgdir}/usr/lib/slack/LICENSE
}
