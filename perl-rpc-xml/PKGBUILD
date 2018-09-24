# Maintainer: Ivan Semkin (ivan at semkin dot ru)
# Contributor: John D Jones III AKA jnbek <jnbek1972 -_AT_- g m a i l -_Dot_- com>
# Generator  : CPANPLUS::Dist::Arch 1.32

pkgname=perl-rpc-xml
_pkgname='RPC-XML-0.80'
pkgver=0.80
pkgrel=3
pkgdesc='A set of classes for core data, message and XML handling'
url='https://metacpan.org/release/RPC-XML'
arch=(any)
license=(PerlArtistic GPL)
options=(!emptydirs)
depends=('perl-xml-parser>=2.31' 'perl-libwww' 'perl>=5.8.8')
optdepends=('perl-xml-libxml: XML::LibXML support'
            'perl-datetime-format-iso8601: DateTime::Format::ISO8601 support'
            'perl-net-server: Net::Server support')
source=("http://search.cpan.org/CPAN/authors/id/R/RJ/RJRAY/RPC-XML-$pkgver.tar.gz")
sha512sums=('a91586ea903b3e633f85ca8d9048181a7c3aedcff6788c7ae5fb4971e8552c421c86f30254517c25caa35f1991146dcceb34301bb49002e4ec75a2ee9c195992')

build() {
  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""                 \
      PERL_AUTOINSTALL=--skipdeps                            \
      PERL_MM_OPT="INSTALLDIRS=vendor DESTDIR='${pkgdir}'"     \
      PERL_MB_OPT="--installdirs vendor --destdir '${pkgdir}'" \
      MODULEBUILDRC=/dev/null

    cd "${srcdir}/${_pkgname}"
    /usr/bin/perl Makefile.PL
    make
  )
}

check() {
  cd "${srcdir}/${_pkgname}"
  rm t/40_server.t || true
  rm t/40_server_xmllibxml.t || true
  ( export PERL_MM_USE_DEFAULT=1 PERL5LIB=""
    make test
  )
}

package() {
  cd "${srcdir}/${_pkgname}"
  make install

  find "${pkgdir}" -name .packlist -o -name perllocal.pod -delete
}
# vim:set ts=2 sw=2 et:
