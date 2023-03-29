#Maintainer Sakuraba Amane <tobiichiamane@archlinuxcn.org>
pkgname=plasma5-applets-kde-githubissues-git
pkgver=r46.f7a5f56
pkgrel=2
pkgdesc="A plasma widget that shows a list of recent github issues for a specific repo"
url="https://github.com/Zren/plasma-applet-githubissues"
arch=('x86_64')
license=('GPL')
depends=("plasma-desktop" "plasma-framework")
makedepends=("git")
conflicts=()
replaces=()
backup=()
source=("git+https://github.com/Zren/plasma-applet-githubissues.git")
md5sums=("SKIP")

pkgver() {
	cd "plasma-applet-githubissues" || exit 1
	printf "r%s.%s" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

package() {
	#mkdir -p "$pkgdir/usr/share/plasma/plasmoids"
	cd "$srcdir/plasma-applet-githubissues/package" 
  find ./ -type f -exec install -Dm755 "{}" "$pkgdir/usr/share/plasma/plasmoids/com.github.zren.githubissues/{}" \;
}
