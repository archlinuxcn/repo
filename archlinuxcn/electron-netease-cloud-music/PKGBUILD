# Maintainer: Metal A-wing <1 at 233 dot email>
# Contributor: Rocka <i at Rocka dot me>

pkgname=electron-netease-cloud-music
pkgver=0.8.17
pkgrel=1
pkgdesc="UNOFFICIAL client for music.163.com . Powered by Electron, Vue, and Muse-UI."
arch=('any')
url="https://github.com/Rocket1184/electron-netease-cloud-music"
license=('GPL3')
depends=('electron')
optdepends=('dbus: MPRIS support')
makedepends=('imagemagick' 'yarn')

source=("$pkgname-$pkgver.tar.gz::https://github.com/Rocket1184/$pkgname/archive/v$pkgver.tar.gz"
        'electron-netease-cloud-music.desktop'
        'electron-netease-cloud-music.sh'
)

md5sums=('b93cecbfcd8a7444c8530b5e39fc4f31'
         '7f35c2dbfc5cd0fd63cd0be16cf35f3c'
         '155178854f344b3d56283beb739c8730')

build() {
    cd "$srcdir/$pkgname-$pkgver"
    YARN_CACHE_FOLDER="$srcdir/yarn_cache" yarn install --ignore-scripts
    yarn dist
}

package() {
    mkdir -p "$pkgdir/usr/lib"
    cp -r "$srcdir/$pkgname-$pkgver/dist" "$pkgdir/usr/lib/$pkgname"

    install -Dm755 "$srcdir/electron-netease-cloud-music.sh" "$pkgdir/usr/bin/electron-netease-cloud-music"
    install -Dm644 "$srcdir/electron-netease-cloud-music.desktop" -t "$pkgdir/usr/share/applications/"

    ICON="$srcdir/$pkgname-$pkgver/assets/icons/icon.png"
    install -Dm644 "$ICON" "$pkgdir/usr/share/icons/hicolor/512x512/apps/${pkgname}.png"
    for size in 16 24 32 48 64 72 128 256; do
        target="$pkgdir/usr/share/icons/hicolor/${size}x${size}/apps/"
        mkdir -p $target
        convert "$ICON" -resize ${size}x${size} "$target/$pkgname.png"
    done

    install -Dm644 "$srcdir/$pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

