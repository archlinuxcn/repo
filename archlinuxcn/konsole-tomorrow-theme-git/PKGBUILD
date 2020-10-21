# Maintainer: DDoSolitary <DDoSolitary@gmail.com>
pkgname=konsole-tomorrow-theme-git
pkgdesc="Tomorrow color theme for Konsole"
pkgver=r1.6f43a05
pkgrel=1
arch=(any)
url=https://github.com/dram/konsole-tomorrow-theme
license=(MIT)
source=($pkgname::git+https://github.com/dram/konsole-tomorrow-theme)
md5sums=(SKIP)
depends=(konsole)
makedepends=(git)
conficts=(konsole-tomorrow-theme)
provides=(konsole-tomorrow-theme)

pkgver() {
	cd $pkgname
	printf r%s.%s $(git rev-list --count HEAD) $(git rev-parse --short HEAD)
}

package() {
	cd $pkgname
	for i in *.colorscheme; do
		install -Dm644 "$i" "$pkgdir/usr/share/konsole/$i"
	done
}
