# Maintainer: Metal A-wing <1 at 233 dot email>
# Contributor: Rocka <i at Rocka dot me>

pkgname=electron-netease-cloud-music
pkgver=0.6.0
pkgrel=1
pkgdesc="UNOFFICAL clinet for music.163.com. Powered by Electron and Vue"
arch=('x86_64')
url="https://github.com/Rocket1184/electron-netease-cloud-music"
license=('GPL-3.0')
depends=('electron')
makedepends=('asar' 'imagemagick')

source_x86_64=("https://github.com/Rocket1184/electron-netease-cloud-music/releases/download/v${pkgver}/${pkgname}_v${pkgver}.asar"
  'electron-netease-cloud-music.desktop'
  'electron-netease-cloud-music.sh'
  'electron-netease-cloud-music.png'
)
md5sums_x86_64=('161ad36472c7aca0d36f76635b37235c'
                '7f35c2dbfc5cd0fd63cd0be16cf35f3c'
                '7ecfe9b9b1c98b43cd9d4c1762a9b96d'
                '3d4d42071b1a86d8e3bf04e0839c3dc4')
package() {
    cd "$srcdir"

    install -Dm755 "$srcdir/electron-netease-cloud-music.sh" "$pkgdir/usr/bin/electron-netease-cloud-music"
    install -Dm644 "$srcdir/electron-netease-cloud-music.desktop" -t "$pkgdir/usr/share/applications/"
#    install -Dm644 "$srcdir/netease-cloud-music.svg" -t "$pkgdir/usr/share/icons/hicolor/symbolic/apps/"
    install -Dm644 ${pkgname}.png "$pkgdir/usr/share/icons/hicolor/512x512/apps/${pkgname}.png"

    for size in 16 24 32 48 64 72 128 256; do
        target="$pkgdir/usr/share/icons/hicolor/${size}x${size}/apps/"
        mkdir -p $target
        convert ${pkgname}.png -resize ${size}x${size} "$target/$pkgname.png"
    done

    asar e "$srcdir/${pkgname}_v${pkgver}.asar" app
    install -Dm644 "$srcdir/app/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

    install -Dm644 "$srcdir/${pkgname}_v${pkgver}.asar" -T "$pkgdir/usr/lib/$pkgname/$pkgname.asar"
}

