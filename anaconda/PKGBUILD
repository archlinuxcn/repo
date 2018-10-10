# Maintainer : Immae <ismael.bouya@normalesup.org>
# Contributor : Martin Wimpress <code@flexion.org>
# Contributor : Jingbei Li <i@jingbei.li>
pkgname=anaconda
pkgver=5.3.0
pkgrel=1
pkgdesc="Completely free enterprise-ready Python distribution for large-scale data processing, predictive analytics, and scientific computing."
arch=('x86_64')
url="https://store.continuum.io/cshop/anaconda/"
license=("custom")
source=("http://repo.continuum.io/archive/Anaconda3-${pkgver}-Linux-x86_64.sh"
"$pkgname.install")
options=(!strip libtool staticlibs)
sha256sums=('cfbf5fe70dd1b797ec677e63c61f8efc92dad930fd1c94d60390bb07fdc09959'
            '72e3066ba033c8e59684331f2d9ea8ea2dc1855d51a7a4ea2fa5565b7dd6cc60')
install="$pkgname.install"

prepare() {
	cd ${srcdir}
	msg2 "Patching Anaconda3-${pkgver}-Linux-x86_64.sh"
	sed \
		-e '/wc -c "\$THIS_PATH" | grep/s/!//' \
		-e "/export FORCE/s|$|;sed \"/^def update_prefix/a\\\    new_prefix='/opt/$pkgname'\" -i pkgs/.install.py|" \
		-i Anaconda3-${pkgver}-Linux-x86_64.sh
}

package() {
	prefix=${pkgdir}/opt/${pkgname}
	LD_PRELOAD="/usr/lib/libfakeroot/libfakeroot.so"

	msg2 "Installing ${pkgname} to /opt/${pkgname}"
	bash ${srcdir}/Anaconda3-${pkgver}-Linux-${CARCH}.sh -b -p $prefix -f
	[ "$BREAK_EARLY" = 1 ] && exit 1
	cd $prefix

	msg2 "Correcting permissions"
	chmod a+r -R pkgs

	msg2 "Stripping \$pkgdir from default meta"
	find conda-meta -name '*.json' -exec sed -e "s/${pkgdir//\//\\\/}//g" -i {} \;

	msg2 "Installing license"
	install -D -m644 LICENSE.txt "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
