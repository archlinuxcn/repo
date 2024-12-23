# Maintainer: Thomas Weißschuh <thomas t-8ch de>

pkgname=needrestart
url=https://github.com/liske/needrestart
pkgdesc='Restart daemons after library updates.'
pkgver=3.8
pkgrel=1
source=(
	"needrestart-${pkgver}.tar.gz::https://github.com/liske/needrestart/archive/v${pkgver}.tar.gz"
	'needrestart.hook'
)
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

sha256sums=('42664e0b1b98fef1e5e849118b9985ac951516c4d5eb24a7da15d058da647c90'
            'e5c6696a281f5445a3b7e2b7d1055f9189a2c39d4940721aa0c2718780f15f63')
