# Maintainer: Thomas Weißschuh <thomas t-8ch de>

pkgname=needrestart
url=https://github.com/liske/needrestart
pkgdesc='Restart daemons after library updates.'
pkgver=3.5
pkgrel=2
source=("needrestart-${pkgver}.tar.gz::https://github.com/liske/needrestart/archive/v${pkgver}.tar.gz")
arch=(any)
license=('GPL')
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
	find "$pkgdir" -type d -empty -delete
}

sha256sums=('e9453efde9a0ebaefa5cb3af241382203d14abcc7091bee1249b60039348597e')
