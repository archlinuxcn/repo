# Maintainer: BlackIkeEagle <ike DOT devolder AT gmail DOT com>
# Contributor: TZ86

pkgname=vivaldi
pkgver=1.14.1077.55
pkgrel=1
pkgdesc='An advanced browser made with the power user in mind.'
url="https://vivaldi.com"
options=(!strip !zipman)
license=('custom')
arch=('x86_64')
depends=('gtk3' 'libcups' 'nss' 'gconf' 'alsa-lib' 'libxss' 'ttf-font' 'desktop-file-utils' 'shared-mime-info' 'hicolor-icon-theme')
makedepends=('w3m')
optdepends=(
    'vivaldi-ffmpeg-codecs: playback of proprietary video/audio'
    'pepper-flash: flash support'
    'google-chrome: Widevine DRM Plugin'
    'vivaldi-widevine: Widevine DRM Plugin'
    'libnotify: native notifications'
)
source_x86_64=("https://downloads.vivaldi.com/stable/vivaldi-stable-${pkgver}-1.x86_64.rpm")
sha512sums_x86_64=('b56722ada4fce23cc5907b41d91b63ae99c68c71f91784e040282a6969f9723797ead6b2a5bb3ed7d908b7949bbeedb0d25c3ff33de088ddd8a79e18f5f7c2d4')

package() {
    cp -a {opt,usr} "$pkgdir"

    # suid sandbox
    chmod 4755 "$pkgdir/opt/vivaldi/vivaldi-sandbox"

    # make /usr/bin/vivaldi-stable available
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

    # quick fix for the actions
    if ! grep 'Desktop Action' "$pkgdir/usr/share/applications/vivaldi-stable.desktop" > /dev/null 2>&1; then
        cat <<'EOF' >> "$pkgdir/usr/share/applications/vivaldi-stable.desktop"

[Desktop Action new-window]
Name=New Window
Exec=/usr/bin/vivaldi-stable --new-window
TargetEnvironment=Unity

[Desktop Action new-private-window]
Name=New Private Window
Exec=/usr/bin/vivaldi-stable --incognito
TargetEnvironment=Unity
EOF
    fi
}

