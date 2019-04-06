#
# Maintainer: Clemens Buchacher <drizzd@aon.at>
#
# You can use the newpkg script from
# https://github.com/drizzd/octave-forge-archlinux to automatically generate
# new octave-forge PKGBUILDs or update existing ones. Patches welcome.
#

_pack=control
pkgname=octave-$_pack
pkgver=3.2.0
pkgrel=1
pkgdesc="Computer-Aided Control System Design (CACSD) Tools for GNU Octave, based on the proven SLICOT Library"
arch=(any)
url="https://octave.sourceforge.io/$_pack/"
license=('GPL3')
groups=('octave-forge')
depends=('octave>=4.0.0')
makedepends=('gcc-fortran')
optdepends=()
backup=()
options=('!makeflags')
install=$pkgname.install
_archive=$_pack-$pkgver.tar.gz
source=("https://downloads.sourceforge.net/octave/$_archive")
noextract=("$_archive")
sha256sums=('faf1d510d16ab46e4fa91a1288f4a7839ee05469c33e4698b7a007a0bb965e3e')

_octave_run() {
	octave --no-history --no-init-file --no-window-system -q -f --eval "$*"
}

_install_dir() {
	src=$1
	dst=$2
	mkdir -p "$(dirname "$dst")"
	cp -rT "$src" "$dst"
}

build() {
	_prefix="$srcdir"/install_prefix
	_archprefix="$srcdir"/install_archprefix
	mkdir -p "$_prefix" "$_archprefix"
	cd "$srcdir"
	_octave_run "$(cat <<-EOF
		pkg local_list octave_packages;
		pkg prefix $_prefix $_archprefix;
		pkg install -verbose -nodeps $_archive;
		EOF
		)"
}

package() {
	prefix=$pkgdir/usr/share/octave/packages
	archprefix=$pkgdir/usr/lib/octave/packages
	_install_dir "$srcdir"/install_prefix "$prefix"
	_install_dir "$srcdir"/install_archprefix "$archprefix"
}
