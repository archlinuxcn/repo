# Maintainer:  Caleb Maclennan <caleb@alerque.com>
# Contributor: Crotok <crotok@mailbox.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Alessio 'mOLOk' Bolognino <themolok@gmail.com>

_distname=Gnome2-Wnck
pkgname=perl-${_distname,,}
pkgver=0.18
pkgrel=2
pkgdesc='Perl interface to the Window Navigator Construction Kit'
url="https://metacpan.org/pod/${_distname//-/::}"
arch=(x86_64)
license=(GPL PerlArtistic)
depends=(perl gtk2-perl libwnck)
makedepends=(perl-extutils-depends perl-extutils-pkgconfig)
options=('!emptydirs')
source=("https://cpan.metacpan.org/authors/id/X/XA/XAOC/$_distname-$pkgver.tar.gz")
sha256sums=('44becec8b2d7f41f2780a73b092269fdb79cd49265bae0c8ff391037c4564a35')

build() {
	cd "$_distname-$pkgver"
	PERL_MM_USE_DEFAULT=1 PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
	make
}

package() {
	cd "$_distname-$pkgver"
	make install DESTDIR="$pkgdir"
}
