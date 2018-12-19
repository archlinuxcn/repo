# Maintainer:  Caleb Maclennan <caleb@alerque.com>
# Contributor: Crotok <crotok@mailbox.org>
# Contributor: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: Alessio 'mOLOk' Bolognino <themolok@gmail.com>

pkgname=perl-gnome2-wnck
_cpname=Gnome2-Wnck
pkgver=0.16
pkgrel=17
pkgdesc="Perl interface to the Window Navigator Construction Kit"
arch=('x86_64')
license=("GPL" "PerlArtistic")
url="https://metacpan.org/pod/${_cpname//-/::}"
depends=('perl' 'gtk2-perl' 'libwnck')
makedepends=('perl-extutils-depends' 'perl-extutils-pkgconfig')
options=('!emptydirs')
source=("https://cpan.metacpan.org/authors/id/T/TS/TSCH/$_cpname-$pkgver.tar.gz")
sha256sums=('604a8ece88ac29f132d59b0caac27657ec31371c1606a4698a2160e88ac586e5')

build() {
    cd "$_cpname-$pkgver"
    PERL_MM_USE_DEFAULT=1 PERL_USE_UNSAFE_INC=1 perl Makefile.PL INSTALLDIRS=vendor
    make
}

package() {
    cd "$_cpname-$pkgver"
    make install DESTDIR="$pkgdir"
}
