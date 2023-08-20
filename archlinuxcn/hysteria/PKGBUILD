# Maintainer: Haruue Icymoon <i@haruue.moe>

_pkgbase=hysteria
pkgname=$_pkgbase
pkgver=1.3.5
pkgrel=2
pkgdesc='A feature-packed network utility optimized for networks of poor quality'
_gover=1.20.7
arch=('x86_64')
url="https://hysteria.network/"
license=('GPL3')
depends=('glibc' 'acl' 'shadow')
makedepends=('go' 'git')
install=$_pkgbase.install
source=("$_pkgbase-git"::"git+https://github.com/apernet/hysteria.git#tag=v$pkgver"
        hysteria@.service
        hysteria-server@.service
        sysusers.conf
        tmpfiles.conf
        "golang-go-${_gover}.src.tar.gz"::"https://go.dev/dl/go${_gover}.src.tar.gz"
        )
sha256sums=('SKIP'
            'e5816c4c66ae564ab927e1460b4f1f89d7bbd5b957634723ef24a82eaf814d06'
            'f79262911516c65a0574c12df5415c62b264e15c2d437635b6b10ef9689e0b94'
            '44f1cb2fedfc94dc396ceb215e62237dbc8c74c035c45a3430c1f3748d266dd9'
            '1e93d9f2b312eaf02ac00229106cd796e0cd54a9a468a0a8d3ae843399c1c310'
            '2c5ee9c9ec1e733b0dbbc2bdfed3f62306e51d8172bf38f4f4e542b27520f597')

prepare(){
  mkdir -p "$srcdir/gopath"
  export GOPATH="$srcdir/gopath"
  cd "$srcdir/$_pkgbase-git"
  mkdir -p build/
}

build() {
  # Building go1.20 as hysteria v1 will never support go1.21
  # ref: https://github.com/apernet/hysteria/issues/647#issuecomment-1676421184
  cd "$srcdir/go/src"
  ./make.bash

  # Building hysteria with go1.20
  cd "$srcdir/$_pkgbase-git"
  #export GOAMD64=v3
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  local _goldflags="-w -s -linkmode=external"
  local _goldflags="$_goldflags -buildid="
  local _goldflags="$_goldflags -X 'main.appVersion=$(git describe --tags --always --match 'v*')'"
  local _goldflags="$_goldflags -X 'main.appCommit=$(git rev-parse HEAD)'"
  local _goldflags="$_goldflags -X 'main.appDate=$(date -u '+%F %T')'"
  "$srcdir/go/bin/go" build \
    -buildmode=pie -trimpath -mod=readonly -modcacherw \
    -o "build/$_pkgbase" \
    -ldflags "$_goldflags" \
    -tags=gpl \
    ./app/cmd
}

#check() {
#  cd "$srcdir/$_pkgbase-git"
#  go test ./...
#}

package() {
  # install hysteria
  install -Dm755 "$srcdir/$_pkgbase-git/build/$_pkgbase" "$pkgdir/usr/bin/$_pkgbase"

  # install sysusers
  install -Dm644 "$srcdir/sysusers.conf" "$pkgdir/usr/lib/sysusers.d/hysteria.conf"
  install -Dm644 "$srcdir/tmpfiles.conf" "$pkgdir/usr/lib/tmpfiles.d/hysteria.conf"

  # install systemd service
  install -Dm644 "$srcdir/hysteria@.service" "$pkgdir/usr/lib/systemd/system/hysteria@.service"
  install -Dm644 "$srcdir/hysteria-server@.service" "$pkgdir/usr/lib/systemd/system/hysteria-server@.service"

  # install config directory
  install -dm755 "$pkgdir/etc/hysteria"
}
