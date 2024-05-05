# Maintainer: Haoyang Liu <tttturtleruss@gmail.com> 

pkgname=hustmirror-cli
pkgver=1.1.3
pkgrel=1
epoch=
pkgdesc="The command line tool (hustmirror-cli) is a small tool that can help you quickly change sources to HUST mirror sources."
arch=('x86_64')
license=('GPL')
url='https://github.com/hust-open-atom-club/hustmirror-cli'
groups=()
depends=('bash')
makedepends=('make' 'python3')
checkdepends=()
optdepends=()
provides=()
conflicts=(hustmirror-cli-git)
replaces=()
backup=()
options=()
install=
changelog=
source=("$pkgname-${pkgver}.tar.gz::${url}/archive/refs/tags/v${pkgver}.tar.gz"
        "$pkgname.patch"
	"$pkgname-makefile.patch")
noextract=()
sha256sums=('SKIP'
            'a08dfc1246edcb721505d717dff36abdaa4aee0f1a74c02d4eece69f563cb5e8'
	    '04c5c54b8dbf4f43d58024aacbfb05e769b5745a6bd090c1d2dbea6ce9f80b5d')
validpgpkeys=()

prepare() {
	cd "$pkgname-${pkgver}"
	patch -p1 -i "$srcdir/$pkgname.patch"
	patch -p1 -i "$srcdir/$pkgname-makefile.patch"
}

build() {
	cd "$pkgname-${pkgver}"
	make
}

package() {
	cd "$pkgname-${pkgver}"
	make DESTDIR="$pkgdir/" install
}
