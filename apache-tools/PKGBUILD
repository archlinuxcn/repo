# Maintainer: Limao Luo <luolimao+AUR@gmail.com>
# Contributor: Marco A Rojas <marquicus@gmail.com>
# Contributor: Pavel Larev <pavel@larev.ws>

pkgname=apache-tools
pkgver=2.4.12
pkgrel=1
pkgdesc="Useful Apache tools - htdigest, htpasswd, ab, htdbm"
arch=(i686 x86_64)
url=http://httpd.apache.org/
license=(Apache)
depends=(apr-util pcre)
conflicts=(apache)
source=(http://www.apache.org/dist/httpd/httpd-$pkgver.tar.bz2
        $pkgname-Makefile.patch)
sha256sums=('ad6d39edfe4621d8cc9a2791f6f8d6876943a9da41ac8533d77407a2e630eae4'
            '2dc48d34773b0c873d10e3542f77a4f7b50d5fb9bd8c52e3bb28b76ff9587f3f')
sha512sums=('f69db14b421f0e1e4861fe4d8b652688d50ca9eb41c622242d11ae55687eb6c2142a8505a8c3fb6f2bd53167be535bc0a77ca1af97e0720930fc7f20f4c1f8e8'
            '6e068e7820e852c788a521ad28c367af4c1c22fded51ede7ae3f840a8a04737cfbe4503c2f3f899c89461d984007e84f80376b5a8a27c7eec8ec0fd78155c22b')

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
}
