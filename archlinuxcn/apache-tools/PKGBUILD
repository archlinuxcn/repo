pkgname=apache-tools
pkgver=2.4.65
pkgrel=1
pkgdesc="Useful Apache tools - htdigest, htpasswd, ab (Apache Benchmark), htdbm"
arch=("i686" "x86_64" "armv6h" "armv7h" "aarch64")
url="http://httpd.apache.org/"
license=("Apache")
depends=("apr-util" "pcre")
makedepends=("apr-util" "db")
conflicts=(apache)
#source=("https://downloads.apache.org/httpd/httpd-$pkgver.tar.bz2"
source=("https://archive.apache.org/dist/httpd/httpd-$pkgver.tar.bz2"
        "$pkgname-Makefile.patch")
sha256sums=('58b8be97d9940ec17f7656c0c6b9f41b618aac468b894b534148e3296c53b8b3'
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
