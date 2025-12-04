pkgname=apache-tools
pkgver=2.4.66
pkgrel=1
pkgdesc="Useful Apache tools - htdigest, htpasswd, ab (Apache Benchmark), htdbm"
arch=("i686" "x86_64" "armv6h" "armv7h" "aarch64")
url="http://httpd.apache.org/"
license=("Apache")
depends=("apr-util" "pcre")
makedepends=("apr-util" "db")
conflicts=(apache)
#source=("https://downloads.apache.org/httpd/httpd-$pkgver.tar.bz2"
source=("https://dlcdn.apache.org/httpd/httpd-$pkgver.tar.bz2"
        "$pkgname-Makefile.patch")
sha256sums=('94d7ff2b42acbb828e870ba29e4cbad48e558a79c623ad3596e4116efcfea25a'
            '2dc48d34773b0c873d10e3542f77a4f7b50d5fb9bd8c52e3bb28b76ff9587f3f')

prepare() {
    cd httpd-$pkgver/
    patch -p1 -i ../$pkgname-Makefile.patch
}

build() {
    cd httpd-$pkgver/
    ./configure --prefix=/usr --sbindir=/usr/bin --with-pcre=/usr
    make -C support
}

package() {
    make -C httpd-$pkgver/support DESTDIR="$pkgdir" install
    make -C httpd-$pkgver DESTDIR="$pkgdir" mandir="/usr/share/man" manualdir="/usr/share/$pkgname/manual" install-man
}
