# Maintainer: ssf <punx69 at gmx dot net>
pkgname=kvantum-kde4-colorscheme-svn
pkgver=r112
pkgrel=1
pkgdesc="Kvantum colorscheme for KDE4"
arch=('any')
url="https://github.com/tsujan/Kvantum"
license=("GPL3")
makedepends=('subversion' 'gawk' 'grep' 'sed' 'findutils')
optdepends=('qt5-style-kvantum-svn: An SVG theme engine for qt5' 'qt4-style-kvantum-svn: An SVG theme engine for qt4' 'kvantum-tools-qt4-svn: Kvantum config tools for Qt4' 'kvantum-tools-qt5-svn: Kvantum config tools for Qt5')
conflicts=('kdestyle-kvantum-kde4' 'kdestyle-kvantum-kde4-git')
provides=("kvantum-kde4-colorscheme=${pkgver}")
_svntrunk=https://github.com/tsujan/Kvantum/trunk/Kvantum/color
_svnmod="$pkgname"

pkgver() {
	svn log $_svntrunk --config-dir "$srcdir" | awk 'NR==2' | awk '{print $1}'
}

build() {
	cd "$srcdir"
	msg "Connecting to SVN server...."
	if [ -d "$_svnmod/.svn" ]; then
		(
		cd "$_svnmod"
		svn status --config-dir "$srcdir" --no-ignore | grep -E '(^\?)|(^\I)|(^\M)' | sed -e 's/^. *//' | sed -e 's/\(.*\)/"\1"/' | xargs rm -drf
		svn up . --config-dir
		)
	else
		svn co "$_svntrunk" --config-dir "$srcdir" "$_svnmod"
	fi
	msg "SVN checkout done or server timeout"
}

package() {
	install -Dm0644 $srcdir/$pkgname/Kvantum.colors $pkgdir/usr/share/apps/color-schemes/Kvantum.colors
}
