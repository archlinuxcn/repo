# Maintainer: Julien Virey <julien.virey@gmail.com>

pkgname=privatebin-cli
_binname=privatebin
_bindate=$(date --rfc-3339=date)
pkgver=2.0.2
pkgrel=3
pkgdesc='A powerful CLI for creating and managing PrivateBin pastes with ease'
arch=('x86_64' 'aarch64')
url='https://github.com/gearnode/privatebin'
license=('ISC')
conflicts=("${pkgname}-bin")
makedepends=('go' 'pandoc')
options=(!lto)
install="$pkgname.install"
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('312544308f6727da210f568d387fd629231b6db8c9a58a3a8dfd2596a3d97513')

prepare() {
  cd $_binname-$pkgver
  export GOPATH="${srcdir}"
  go mod download

  # Man
  pandoc --standalone --to man -M footer=$pkgver doc/privatebin.1.md -o privatebin.1
  pandoc --standalone --to man -M footer=$pkgver doc/privatebin-create.1.md -o privatebin-create.1
  pandoc --standalone --to man -M footer=$pkgver doc/privatebin-show.1.md -o privatebin-show.1
  pandoc --standalone --to man -M footer=$pkgver doc/privatebin.conf.5.md -o privatebin.conf.5
}

build() {
  cd "$_binname-$pkgver"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  export GOPATH="${srcdir}"
  export GOFLAGS="-buildmode=pie -trimpath -ldflags=-linkmode=external -mod=readonly -modcacherw"

  go build \
    -ldflags "-X 'main.version=$pkgver'
        -X 'main.commit=$pkgrel'
        -X 'main.date=$_bindate'" \
    -o $_binname cmd/privatebin/main.go cmd/privatebin/cfg.go
}

package() {
  cd $_binname-$pkgver
  install -Dm755 $_binname "$pkgdir"/usr/bin/$_binname
  install -Dm644 LICENSE.txt -t "${pkgdir}"/usr/share/licenses/${pkgname}/LICENSE
  install -Dm644 privatebin.1 -t "${pkgdir}"/usr/share/man/man1/
  install -Dm644 privatebin-create.1 -t "${pkgdir}"/usr/share/man/man1/
  install -Dm644 privatebin-show.1 -t "${pkgdir}"/usr/share/man/man1/
  install -Dm644 privatebin.conf.5 -t "${pkgdir}"/usr/share/man/man5/
}
