# Maintainer: Florian Pritz <flo@xinu.at>
# Grabbed from Parabola by figue <https://aur.archlinux.org/account/figue> :: https://www.parabola.nu/packages/pcr/x86_64/perl-file-rename/

pkgname=perl-file-rename
pkgver=1.13
pkgrel=1
pkgdesc="Renames multiple files using Perl regular expressions."
arch=(any)
url="https://metacpan.org/release/File-Rename"
license=(PerlArtistic)
depends=(perl)
options=(!emptydirs)
source=(https://cpan.metacpan.org/authors/id/R/RM/RMBARKER/File-Rename-$pkgver.tar.gz)
sha256sums=('0b308d6ac5b8ae0dad6135c7b68620582221b2b3144a5b390ddd2ea64312e64d')

build() {
    cd "$srcdir/File-Rename-$pkgver"

    perl Makefile.PL PREFIX=/usr INSTALLDIRS=vendor
    make
}

package() {
    cd "$srcdir/File-Rename-$pkgver"

    make DESTDIR="$pkgdir/" install
    install -d "$pkgdir/usr/bin/"
    ln -s vendor_perl/rename "$pkgdir/usr/bin/perl-rename"
    ln -s /usr/share/man/man1/rename.1p.gz "$pkgdir/usr/share/man/man1/perl-rename.1p.gz"
}
