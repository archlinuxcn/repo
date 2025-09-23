# Maintainer: dbgbgtf <dudududumaxver@outlook.com>
# Maintainer: RocketDev <ma2014119@outlook.com>
pkgname=ceccomp
pkgver=3.1
pkgrel=1
pkgdesc="A C-based seccomp analysis tool"
arch=(x86_64)
url="https://github.com/dbgbgtf1/Ceccomp"
license=('GPL-3.0-or-later')
depends=(
    libseccomp
    glibc
)
makedepends=(
    asciidoctor # for doc generation
    python # for configure
    git
    util-linux # for flock to display a progress
    gettext # for i18n/l10n
)

source=("$pkgname"::git+https://github.com/dbgbgtf1/Ceccomp.git#tag=v${pkgver}?signed)
b2sums=('e4f6106a0a141f8e617abf3d1502dad1eac2764c7ee9b8aa714c5ea5a1cf62c5a9a283195e5a693628e9c5f8dad23137aa21770fe278b6008a99674c03292f28')

validpgpkeys=(
    '0816A179BB09248F30468BD6542A0969B5CEDCDB' # dbgbgtf1 <dudududumaxver@outlook.com>
    'A7ACCC386C15E3C554D34B3EAB08F98092A456BB' # RocketDev <ma2014119@outlook.com>
)

prepare() {
    cd "$srcdir/$pkgname"
    ./configure --prefix="$pkgdir/usr"
    make clean
}

build() {
    cd "$srcdir/$pkgname"
    # force program to load locale in system
    make LOCALE_DIR=/usr/share/locale
}

package() {
    cd "$srcdir/$pkgname"
    make install
}
