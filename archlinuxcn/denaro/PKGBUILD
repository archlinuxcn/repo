# Maintainer: Mattia Borda <mattiagiovanni.borda@icloud.com>

pkgname=denaro
pkgver=2024.2.0
pkgrel=1
pkgdesc="A personal finance manager"
arch=(aarch64 armv7h x86_64 i686)
url=https://github.com/NickvisionApps/$pkgname
license=(GPL3)
depends=('dotnet-runtime>=8' libadwaita)
makedepends=(blueprint-compiler 'dotnet-sdk>=8' git)
source=("git+$url#tag=$pkgver" "git+${url%denaro}cakescripts#commit=1b48cc0957fcd65c3b0f25285e84033fb5b7f542")
b2sums=('SKIP'
        'SKIP')

prepare() {
	rm -rf $pkgname/CakeScripts
	mv cakescripts $pkgname/CakeScripts
	cd $pkgname
	dotnet tool restore
}

build() {
	cd $pkgname
	dotnet cake --target=Publish --prefix=/usr --ui=gnome
}

package() {
	cd $pkgname
	dotnet cake --target=Install --destdir="$pkgdir"
}
