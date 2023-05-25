# Maintainer: Pylogmon <pylogmon@outlook.com>

pkgname=pot-translation
reponame=pot-desktop
pkgver=0.4.1
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

sha512sums=('ab638eae9dd1f8b3f49215395be8ada6b88b9a0880bca20c1f603840c15d9edc1a405da5701f2b410be5cf1ed2b65a85d6079b06149c557c7d3a7a7542f49ce7')

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
