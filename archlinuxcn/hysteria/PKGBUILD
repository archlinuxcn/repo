# Maintainer: Haruue Icymoon <i@haruue.moe>

_pkgbase=hysteria
pkgname=$_pkgbase
pkgver=1.3.0
pkgrel=1
pkgdesc='A feature-packed network utility optimized for networks of poor quality'
arch=('x86_64')
url="https://github.com/HyNetwork/hysteria"
license=('GPL3')
depends=('glibc' 'acl' 'shadow')
makedepends=('go' 'git')
install=$_pkgbase.install
source=("$_pkgbase"::"git+$url.git#tag=v$pkgver"
        hysteria@.service
        hysteria-server@.service
        sysusers.conf
	tmpfiles.conf
        )
sha256sums=('SKIP'
            '61ef8c91f417d83411d89295495e0c926ded7ed02302e7a0efa123d564e12f7e'
            '5a0fb1185e7bff6e05ec8ecb8a45b269fd4c7fa562ab107954ab87642a71f8d0'
            '44f1cb2fedfc94dc396ceb215e62237dbc8c74c035c45a3430c1f3748d266dd9'
            '1e93d9f2b312eaf02ac00229106cd796e0cd54a9a468a0a8d3ae843399c1c310')

prepare(){
  mkdir -p "$srcdir/gopath"
  export GOPATH="$srcdir/gopath"
  cd "$srcdir/$_pkgbase"
  mkdir -p build/
}

build() {
  cd "$srcdir/$_pkgbase"
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS} -DLWIP_NOASSERT"
  export CGO_CXXFLAGS="${CXXFLAGS} -DLWIP_NOASSERT"
  export CGO_LDFLAGS="${LDFLAGS}"
  local _goldflags="-w -s -linkmode=external"
  local _goldflags="$_goldflags -X 'main.appVersion=$(git describe --tags --always)'"
  local _goldflags="$_goldflags -X 'main.appCommit=$(git rev-parse HEAD)'"
  local _goldflags="$_goldflags -X 'main.appDate=$(date -u '+%F %T')'"
  go build \
    -buildmode=pie -trimpath -mod=readonly -modcacherw \
    -o "build/$_pkgbase" \
    -ldflags "$_goldflags" \
    -tags=gpl \
    ./cmd
}

#check() {
#  cd "$srcdir/$_pkgbase"
#  go test ./...
#}

package() {
  # install hysteria
  install -Dm755 "$srcdir/$_pkgbase/build/$_pkgbase" "$pkgdir/usr/bin/$_pkgbase"

  # install sysusers
  install -Dm644 "$srcdir/sysusers.conf" "$pkgdir/usr/lib/sysusers.d/hysteria.conf"
  install -Dm644 "$srcdir/tmpfiles.conf" "$pkgdir/usr/lib/tmpfiles.d/hysteria.conf"

  # install systemd service
  install -Dm644 "$srcdir/hysteria@.service" "$pkgdir/usr/lib/systemd/system/hysteria@.service"
  install -Dm644 "$srcdir/hysteria-server@.service" "$pkgdir/usr/lib/systemd/system/hysteria-server@.service"

  # install config directory
  install -dm755 "$pkgdir/etc/hysteria"
}
