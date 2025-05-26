# Maintainer: Thomas Weißschuh <aur t-8ch de>

pkgname=needrestart
url=https://github.com/liske/needrestart
pkgdesc='Restart daemons after library updates.'
pkgver=3.11
pkgrel=1
source=("needrestart-${pkgver}.tar.gz::https://github.com/liske/needrestart/archive/v${pkgver}.tar.gz"
	'needrestart.hook'
)
sha256sums=('7a480c38b3b5bf492b3c386ff6bf2baa5905556dd4a7187e157368f35ca13b8b'
            'e5c6696a281f5445a3b7e2b7d1055f9189a2c39d4940721aa0c2718780f15f63')
arch=(any)
license=('GPL-2.0-or-later')
options=(!emptydirs)
depends=(perl-module-find
         perl-term-readkey
         perl-proc-processtable
         perl-sort-naturally
         perl-module-scandeps
         perl-libintl-perl
)
optdepends=(
	'iucode-tool: for outdated microcode detection'
)

build() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	unset PERL5LIB PERL_MM_OPT PERL_LOCAL_LIB_ROOT
	export PERL_MM_USE_DEFAULT=1 PERL_AUTOINSTALL=--skipdeps
	make
}

prepare() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	sed -i -e 's|/usr/sbin|/usr/bin|' Makefile
}

package() {
	cd "${srcdir}/${pkgname}-${pkgver}"
	unset PERL5LIB PERL_MM_OPT PERL_LOCAL_LIB_ROOT
	export PERL_MM_USE_DEFAULT=1 PERL_AUTOINSTALL=--skipdeps
	make DESTDIR="${pkgdir}" install

	install -Dm444 "${srcdir}/needrestart.hook" \
		"${pkgdir}/usr/share/libalpm/hooks/needrestart.hook"
}
