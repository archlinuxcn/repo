# Maintainer: Adrien Smith <adrien at bouldersmiths dot com>
pkgname=overmind
pkgver=2.2.2
pkgrel=1
pkgdesc="Process manager for Procfile-based applications and tmux"
arch=("x86_64")
url="https://github.com/DarthSim/$pkgname"
license=("MIT")
depends=('tmux')
makedepends=("go")
conflicts=("$pkgname-bin" "$pkgname-git")
source=("$pkgname-$pkgver.tar.gz::$url/archive/v$pkgver.tar.gz")
sha512sums=('1ca98ee6a058e4d396e96c3b0442387567816e6c3b7cad1122e5f3ca915067ae2b03d9629e156c91e4164fa71f42930002da1d9e0e7f4eaee9d866bcabe94f6f')
b2sums=('0caafb16472bb0c3ea369347156cda929bb8e16ba19b758c61ed0c87ad946b93528f506c675b73da80becc7935a35930f8778e14eea0076c5aa1969b7721fd87')

build() {
  cd "$pkgname-$pkgver"
  go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -ldflags "-linkmode external -extldflags \"${LDFLAGS}\"" \
    -o $pkgname .
}

package() {
  cd "$pkgname-$pkgver"
  install -Dm755 $pkgname "$pkgdir/usr/bin/$pkgname"
  install -Dm644 LICENSE "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
