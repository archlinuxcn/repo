# Contributor: kreed <kreed@kreed.org>
# Contributor: rayman2200
# Maintainer: Eric Anderson <ejona86@gmail.com>

pkgname=mcrcon
pkgver=0.7.2
pkgrel=1
pkgdesc="Console based remote console (rcon) client for Minecraft servers"
arch=('i686' 'x86_64')
url="https://github.com/Tiiffi/mcrcon"
license=('ZLIB')
depends=('glibc')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Tiiffi/${pkgname}/archive/v${pkgver}.tar.gz")
sha256sums=('1743b25a2d031b774e805f4011cb7d92010cb866e3b892f5dfc5b42080973270')

build() {
	cd "$pkgname-$pkgver"
	make LINKER="$LDFLAGS"
}

package() {
	cd "$pkgname-$pkgver"
	make PREFIX="$pkgdir/usr/" install
	install -m 644 -D LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
