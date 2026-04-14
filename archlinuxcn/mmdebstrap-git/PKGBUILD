# Maintainer: Jax Young <jaxvanyang@gmail.com>
# Contributer: Sean Anderson <seanga2@gmail.com>
pkgname=mmdebstrap-git
_name="${pkgname%-git}"
pkgver=1.5.7.r3.77ec9be
pkgrel=1
pkgdesc="create a Debian chroot"
arch=('any')
url="https://gitlab.mister-muffin.de/josch/mmdebstrap"
license=('MIT')
depends=('apt' 'python' 'perl')
makedepends=('git')
optdepends=(
	'debian-archive-keyring: Debian PKI support'
	'ubuntu-keyring: Ubuntu PKI support'
	'qemu-user-static: foreign-architecture support'
	'qemu-user-static-binfmt: foreign-architecture support'
	'arch-test: foreign-architecture support')
provides=("$_name")
conflicts=("$_name")
source=("$_name::git+$url.git")
sha256sums=('SKIP')

pkgver() {
	cd "$_name"
	printf "%s" "$(git describe --long | sed 's/\([^-]*-\)g/r\1/;s/-/./g')"
}

prepare() {
	cd "$_name"
	sed -i 's,/usr/libexec,/usr/lib,g' gpgvnoexpkeysig mmdebstrap
}

package() {
	cd "$_name"

	source <(perl -V:vendorarch)
	mkdir -p "$pkgdir$vendorarch"
	h2ph -d "$pkgdir$vendorarch" -a syscall.h sys/ioctl.h || true

	mkdir -p "$pkgdir/usr/bin"
	cp -a mmdebstrap "$pkgdir/usr/bin/mmdebstrap"
	cp -a tarfilter "$pkgdir/usr/bin/mmtarfilter"
	mkdir -p "$pkgdir/usr/lib/apt/solvers"
	cp -a proxysolver "$pkgdir/usr/lib/apt/solvers/mmdebstrap-dump-solution"
	mkdir -p "$pkgdir/usr/share/mmdebstrap"
	cp -a hooks "$pkgdir/usr/share/mmdebstrap"
	mkdir -p "$pkgdir/usr/lib/mmdebstrap"
	cp -a gpgvnoexpkeysig "$pkgdir/usr/lib/mmdebstrap"
	cp -a ldconfig.fakechroot "$pkgdir/usr/lib/mmdebstrap"

	mkdir -p "$pkgdir/usr/share/man/man1"
	pod2man mmdebstrap > "$pkgdir/usr/share/man/man1/mmdebstrap.1"
}
