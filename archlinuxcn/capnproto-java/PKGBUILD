pkgname=capnproto-java
pkgver=0.1.16
pkgrel=1
pkgdesc="Cap'n Proto for Java"
arch=('i686' 'x86_64')
url="https://github.com/capnproto/capnproto-java"
license=('MIT')
depends=('capnproto')
source=("https://github.com/capnproto/capnproto-java/archive/v${pkgver}.tar.gz")
sha256sums=('904525c4433fb1779bbc4face11887b016f949f1b019755b1886c5f367f4c091')

build() {
    cd "$pkgname-$pkgver"
    make
}

package() {
    cd "$pkgname-$pkgver"
    
    install -D capnpc-java "$pkgdir"/usr/bin/capnpc-java
    install -Dm644 compiler/src/main/schema/capnp/java.capnp "$pkgdir"/usr/include/capnp/java.capnp
    install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

