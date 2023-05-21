# Maintainer: Pylogmon <pylogmon@outlook.com>

pkgname=pot-translation
reponame=pot-desktop
pkgver=0.3.6
pkgrel=1
pkgdesc="一个跨平台的划词翻译软件"
arch=('x86_64')
url="https://github.com/pot-app/pot-desktop"
license=('GPL3')
provides=("$pkgname")
conflicts=("$pkgname-bin" "$pkgname-git")
depends=('libappindicator-gtk3' 'webkit2gtk' 'gtk3' 'libayatana-appindicator' 'xdotool')
makedepends=('nodejs' 'pnpm' 'rust')

source=("${reponame}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")

sha512sums=('09bae1eb5edae464a1156ab1574a595b9e879fe0cceb115512b8fa450f2974a752c2c18fce222a8ce77b644fa4c8c751aa6394d97a25c46276ad26b0e6911e13')

build(){
    cd $srcdir/${reponame}-${pkgver}
    sed -i "s/\"version\".*/\"version\": \"$pkgver\"/g" src-tauri/tauri.conf.json 
    pnpm i
    pnpm tauri build -b deb
}
package() {
    cd $srcdir/${reponame}-${pkgver}
    tar xpf src-tauri/target/release/bundle/deb/pot_${pkgver}_amd64/data.tar.gz -C ${pkgdir}
}
