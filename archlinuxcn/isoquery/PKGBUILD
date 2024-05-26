# Maintainer: Nicolas Iooss <nicolas.iooss_aur at m4x.org>

pkgname=isoquery
pkgver=3.2.7
pkgrel=1
pkgdesc="Search and display ISO codes for countries, languages, currencies, and scripts."
arch=('i686' 'x86_64')
url="https://codeberg.org/toddy/isoquery"
license=('GPL3')
depends=('iso-codes' 'json-glib')
makedepends=('gettext' 'perl-syntax-keyword-try' 'po4a' 'python-docutils')
source=("$pkgname-$pkgver.tar.gz::https://codeberg.org/toddy/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('331d820bdf62a72e02464f94cdecf55049545549d617a2332bf84e9f550d6381')

prepare() {
    cd "$pkgname"

    # Some integration tests expect "de" or "fr" lang to be installed.
    # Remove them.
    # List obtained with: grep ' -l fr' -rl tests/expected
    rm tests/expected/iso_15924/all_localized_test_commandline.txt
    rm tests/expected/iso_3166-1/all_localized_test_commandline.txt
    rm tests/expected/iso_3166-2/all_localized_test_commandline.txt
    rm tests/expected/iso_3166-3/all_localized_test_commandline.txt
    rm tests/expected/iso_4217/all_localized_test_commandline.txt
    rm tests/expected/iso_639-2/all_localized_test_commandline.txt
    rm tests/expected/iso_639-3/all_localized_test_commandline.txt
    rm tests/expected/iso_639-5/all_localized_test_commandline.txt
    # List obtained with: grep ' --locale de' -rl tests/expected
    rm tests/expected/iso_3166-1/invalid_codes_localized_test_commandline.txt
    rm tests/expected/iso_3166-1/multiple_codes_localized_test_commandline.txt
}

build() {
    cd "$pkgname"

    ./configure --prefix=/usr
    make
}

check() {
    cd "$pkgname"

    make check
}

package() {
    cd "$pkgname"

    make DESTDIR="$pkgdir" install
}
