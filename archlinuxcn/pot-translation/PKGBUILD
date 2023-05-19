# Maintainer: Pylogmon <pylogmon@outlook.com>

pkgname=pot-translation
prjname=pot
pkgver=0.3.4
pkgrel=0
pkgdesc="一个跨平台的划词翻译软件"
arch=('x86_64')
url="https://github.com/pot-app/pot-desktop"
license=('GPL3')
provides=("$pkgname")
conflicts=("$pkgname-bin" "$pkgname-git")
depends=('libappindicator-gtk3' 'webkit2gtk' 'gtk3' 'libayatana-appindicator')
makedepends=('nodejs' 'pnpm' 'rust')

source=("${prjname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")

sha512sums=('3076c717d15e8cec6368fa73d9cd5eecd843c8891e6ed015aa7330a2b9795474e835a68fb0f260e69aa3e064cda946ef66e7f25faee5b3f9f21e7d7198a69054')

build(){
    cd $srcdir/${prjname}-${pkgver}
    sed -i "s/\"version\".*/\"version\": \"$pkgver\"/g" src-tauri/tauri.conf.json 
    pnpm i
    pnpm tauri build -b deb
}
package() {
    cd $srcdir/${prjname}-${pkgver}
    tar xpf src-tauri/target/release/bundle/deb/${prjname}_${pkgver}_amd64/data.tar.gz -C ${pkgdir}
}
