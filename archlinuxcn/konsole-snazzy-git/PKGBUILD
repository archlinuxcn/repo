# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
pkgname=konsole-snazzy-git
pkgdesc="Elegant Konsole theme with bright colors"
pkgver=r3.113050d
pkgrel=1
arch=(any)
url=https://github.com/miedzinski/konsole-snazzy
license=(MIT)
source=($pkgname::git+https://github.com/miedzinski/konsole-snazzy)
md5sums=(SKIP)
depends=(konsole)
makedepends=(git)
conficts=(konsole-snazzy)
provides=(konsole-snazzy)

pkgver() {
	cd $pkgname
	printf r%s.%s $(git rev-list --count HEAD) $(git rev-parse --short HEAD)
}

package() {
	install -Dm644 $pkgname/snazzy.colorscheme "$pkgdir/usr/share/konsole/snazzy.colorscheme"
}
