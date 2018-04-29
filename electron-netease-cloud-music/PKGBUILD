# Maintainer: Metal A-wing <1 at 233 dot email>

pkgname=electron-netease-cloud-music
pkgver=0.4.1
pkgrel=1
pkgdesc=" UNOFFICAL clinet for music.163.com. Powered by Electron and Vue"
arch=('x86_64')
url="https://github.com/Rocket1184/electron-netease-cloud-music"
license=('GPL-3.0')
depends=('electron')

source_x86_64=("https://github.com/Rocket1184/electron-netease-cloud-music/releases/download/v${pkgver}/app.asar"
  'electron-netease-cloud-music.desktop'
  'electron-netease-cloud-music.sh'
  'netease-cloud-music.svg'
)

md5sums_x86_64=('1d97eb7cd9fb08ec4d0a9af9b12bac5d'
                '9198bd214026256cab4f0ad60ed5a538'
                '77f597cf81b39d6d6bfee05d4009d026'
                '24cb8955dac6c6c5f0ae2bc1451c56b8')

package() {
    cd "$srcdir"

    install -Dm755 "$srcdir/electron-netease-cloud-music.sh" "$pkgdir/usr/bin/electron-netease-cloud-music"
    install -Dm644 electron-netease-cloud-music.desktop -t "$pkgdir/usr/share/applications/"
    install -Dm644 netease-cloud-music.svg "$pkgdir/usr/share/icons/hicolor/symbolic/apps/netease-cloud-music.svg"

    #cd "$srcdir/$pkgname-linux-x64"
    #install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

    mkdir -p "$pkgdir/usr/lib/$pkgname/"
    #install -Dm644 resources/app.asar $pkgdir/usr/lib/$pkgname/
    install -Dm644 app.asar $pkgdir/usr/lib/$pkgname/


    #mkdir -p "$pkgdir/usr/lib/$pkgname/"
    #cp -r --no-preserve='ownership' -- * "$pkgdir/usr/lib/$pkgname/"
    #mkdir -p "$pkgdir/usr/bin/"
    #ln -s '../lib/electron-netease-cloud-music/electron-netease-cloud-music' "$pkgdir/usr/bin/electron-netease-cloud-music"
}

