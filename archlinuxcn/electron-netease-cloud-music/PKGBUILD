# Maintainer: Metal A-wing <1 at 233 dot email>
# Contributor: Rocka <i at Rocka dot me>

pkgname=electron-netease-cloud-music
pkgver=0.9.38
pkgrel=1
pkgdesc="UNOFFICIAL client for music.163.com . Powered by Electron, Vue, and Muse-UI."
arch=('any')
url="https://github.com/Rocket1184/electron-netease-cloud-music"
license=('GPL3')
depends=('electron')
optdepends=('dbus: MPRIS support')
makedepends=('yarn')

source=("$pkgname-$pkgver.tar.gz::https://github.com/Rocket1184/$pkgname/archive/v$pkgver.tar.gz"
        'electron-netease-cloud-music.desktop'
        'electron-netease-cloud-music.sh'
)

md5sums=('fbad8bfd9eab444b5a2ab6b5f73c86ad'
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

    ICON="$srcdir/$pkgname-$pkgver/assets/icons/icon.svg"
    install -Dm644 "$ICON" "$pkgdir/usr/share/icons/hicolor/scalable/apps/${pkgname}.svg"

    install -Dm644 "$srcdir/$pkgname-$pkgver/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
