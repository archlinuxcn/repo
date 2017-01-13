# Maintainer: yk <yk at archlinuxcn dot org>

_pkgname=desktop-app
pkgname=leanote
pkgver=2.2.1
pkgrel=1
pkgdesc="Knowledge, Blog, Sharing, Cooperation... all in this package"
arch=("i686" "x86_64")
url="http://github.com/$pkgname/$_pkgname"
license=("GPL3")
depends=("electron")
makedepends=("electron" "gulp")
provides=("$pkgname")
conflicts=("$pkgname")
#install=$pkgname.install

source=("https://github.com/$pkgname/$_pkgname/archive/V$pkgver.tar.gz"
"leanote.desktop"
"leanote.png"
"leanote"
)
sha256sums=('e68163cb5c2edfcdd47ada1be9779a4c6066ec5819e96c1090b18dd4f5f7af2c'
'8dab30fe0835432e44b5a3a1d46aebde8716a2a47ba4031cbe2a01560987aa83'
'6ff24cc032dfb03fb820d5b4c3a451273e19f339ce5a727a8e39bc6115923de3'
'38cc9670a73086deeb5f3f1b5932b2b489ba7db4c17d913c8357ee57cd6a547d'
)

build() {
	cd "$srcdir/$_pkgname-$pkgver/dev"
    #npm install
    #gulp dev
}

package() {
    install -d "$pkgdir"/opt
    cp -R $srcdir/$_pkgname-$pkgver "$pkgdir"/opt/leanote
    install -D -m655 "./${pkgname}" "${pkgdir}/usr/bin/${pkgname}"
    install -D -m644 "./${pkgname}.desktop" "${pkgdir}/usr/share/applications/${pkgname}.desktop"
    install -D -m644 "./${pkgname}.png" "${pkgdir}/usr/share/pixmaps/${pkgname}.png"
}
