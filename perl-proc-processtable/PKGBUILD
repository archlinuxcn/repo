pkgname=perl-proc-processtable
pkgver=0.50
pkgrel=2
pkgdesc="Provides a consistent interface to process table information."
arch=('any')
url="http://search.cpan.org/dist/Proc-ProcessTable/"
license=('PerlArtistic')
depends=('perl')
provides=('perl-proc-killall=1.0.0' 'perl-proc-killfam=1.0.0' 'perl-proc-processtable-process=0.20.0')
options=(!emptydirs)
source=("http://search.cpan.org/CPAN/authors/id/J/JW/JWB/Proc-ProcessTable-$pkgver.tar.gz")
md5sums=('3b21edabad48989c44d784f2059f3837')

build() {
  cd $srcdir/Proc-ProcessTable-$pkgver

  PERL_MM_USE_DEFAULT=1 perl Makefile.PL INSTALLDIRS=vendor
  make
}

package() {
  cd $srcdir/Proc-ProcessTable-$pkgver

  make install DESTDIR="${pkgdir}"
  find ${pkgdir} -name perllocal.pod -delete
  find ${pkgdir} -name .packlist -delete
}
