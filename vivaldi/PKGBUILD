# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Contributor: TZ86

pkgname=vivaldi
pkgver=1.7.735.46
pkgrel=1
pkgdesc='An advanced browser made with the power user in mind.'
url="https://vivaldi.com"
options=(!strip !zipman)
license=('custom')
arch=('i686' 'x86_64')
depends=('gtk2' 'nss' 'libxtst' 'gconf' 'libxss' 'freetype2' 'ttf-font' 'desktop-file-utils' 'shared-mime-info' 'alsa-lib' 'hicolor-icon-theme')
makedepends=('w3m')
optdepends=(
    'vivaldi-ffmpeg-codecs: playback of proprietary video/audio'
    'google-chrome: Widevine DRM Plugin'
    'vivaldi-widevine: Widevine DRM Plugin'
)
source_i686=("https://downloads.vivaldi.com/stable/vivaldi-stable-${pkgver}-1.i386.rpm")
source_x86_64=("https://downloads.vivaldi.com/stable/vivaldi-stable-${pkgver}-1.x86_64.rpm")
sha256sums_i686=('03ed5e2617075be7be1268b3480ddbd947ca329182da46a9b5686fc98fc58639')
sha256sums_x86_64=('29c73025059a3464654a232f2f275db54631bfbf8bb2c84a59e5094ab5615fda')

package() {
    cp -a {opt,usr} "$pkgdir"

    # suid sandbox
    chmod 4755 "$pkgdir/opt/vivaldi/vivaldi-sandbox"

    binf="$pkgdir/usr/bin/vivaldi-stable"
    if [[ ! -e "$binf" ]] && [[ ! -f "$binf" ]] && [[ ! -L "$binf" ]]; then
        install -dm755 "$pkgdir/usr/bin"
        ln -s /opt/vivaldi/vivaldi "$binf"
    fi

    # install icons
    for res in 16 22 24 32 48 64 128 256; do
        install -Dm644 "$pkgdir/opt/vivaldi/product_logo_${res}.png" \
            "$pkgdir/usr/share/icons/hicolor/${res}x${res}/apps/vivaldi.png"
    done

    # license
    install -dm755 "$pkgdir/usr/share/licenses/$pkgname"
    strings "$pkgdir/opt/vivaldi/locales/en-US.pak" \
        | tr '\n' ' ' \
        | sed -rne 's/.*(<html lang.*>.*html>).*/\1/p' \
        | w3m -I 'utf-8' -T 'text/html' \
        > "$pkgdir/usr/share/licenses/$pkgname/eula.txt"
}

