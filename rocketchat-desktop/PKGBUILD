# Maintainer: Matthias Lisin <ml@visu.li>
# Contributor: sum01 <sum01@protonmail.com>
pkgname=rocketchat-desktop
pkgver=2.13.3
_srcname="Rocket.Chat.Electron-$pkgver"
pkgrel=1
pkgdesc='Rocket.Chat Native Cross-Platform Desktop Application via Electron.'
arch=('i686' 'x86_64')
url="https://github.com/RocketChat/Rocket.Chat.Electron"
license=('MIT')
depends=('nss' 'libxss' 'gconf' 'gtk3' 'glibc')
makedepends=('sed' 'yarn>=0.21.3' 'nodejs>=7.0.0' 'node-gyp' 'python2')
conflicts=('rocketchat-client-bin')
source=("$pkgname-$pkgver.tar.gz::https://github.com/RocketChat/Rocket.Chat.Electron/archive/$pkgver.tar.gz"
        fix-linux-target.patch
        fix-gulp-release.patch
        rocketchat-desktop.desktop)
sha512sums=('1d63816c8667b27ab90f336dc67ad352b26c0dd3a419e82a3a169e5d3a38fcc58ac91bd3b3e1ecbb5611c49493fd86972a8bd59c9a858ba2bd1e36b751edbbaf'
            '8a2753f6cffa7779cc9c008c872d24c8c6c20307886ec62f124a26249c1e96d0dcf1fd2529c6a335b2f1eea533cf24c9a2ca486794452b0190e14b5d47c8c0b5'
            '043a9b4ed2eddbb93404eab70cc2238bde5930d97c1bf88c1e49eddf61e960db19b996e5ffd9fd65062041fc0726d8ca5f9a4d5436e753260fda482a9544bbf3'
            'd87664b9bdf30eac3011393d094962e0d568a94b5eaf4c8e5f17529442dcba905cea7341527066102a97a07a981acd6ce045b8737eb78a7d81a2a2d05023fe26')
if [[ $CARCH == "i686" ]]; then
    _releasename="release:linux-ia32"
    _distname="linux-ia32-unpacked"
else
    _releasename="release:linux-x64"
    _distname="linux-unpacked"
fi

prepare() {
    patch -p1 -d "$_srcname" < fix-linux-target.patch
    patch -p1 -d "$_srcname" < fix-gulp-release.patch
}

build() {
    cd "$srcdir/$_srcname"
    yarn install --non-interactive --pure-lockfile --cache-folder "$srcdir/yarn-cache"
    yarn build --env=production "$_releasename"
}

package() {
    install -d "$pkgdir"/{usr/bin,opt}
    install -Dm644 "$srcdir/$_srcname/build/icons/512x512.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/$pkgname.png"
    install -Dm644 "$srcdir/$pkgname.desktop" "$pkgdir/usr/share/applications/$pkgname.desktop"
    install -Dm644 "$srcdir/$_srcname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
    cp -r "$srcdir/$_srcname/dist/$_distname" "$pkgdir/opt/$pkgname"
    ln -sf "/opt/$pkgname/$pkgname" "$pkgdir/usr/bin/$pkgname"
}
