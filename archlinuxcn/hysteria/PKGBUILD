# Maintainer: Haruue Icymoon <i@haruue.moe>

_pkgbase=hysteria
pkgname=$_pkgbase
pkgver=1.3.4
pkgrel=1
pkgdesc='A feature-packed network utility optimized for networks of poor quality'
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
        )
sha256sums=('SKIP'
            'e5816c4c66ae564ab927e1460b4f1f89d7bbd5b957634723ef24a82eaf814d06'
            'f79262911516c65a0574c12df5415c62b264e15c2d437635b6b10ef9689e0b94'
            '44f1cb2fedfc94dc396ceb215e62237dbc8c74c035c45a3430c1f3748d266dd9'
            '1e93d9f2b312eaf02ac00229106cd796e0cd54a9a468a0a8d3ae843399c1c310')

prepare(){
  mkdir -p "$srcdir/gopath"
  export GOPATH="$srcdir/gopath"
  cd "$srcdir/$_pkgbase-git"
  mkdir -p build/
}

build() {
  cd "$srcdir/$_pkgbase-git"
  #export GOAMD64=v3
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  local _goldflags="-w -s -linkmode=external"
  local _goldflags="$_goldflags -X 'main.appVersion=$(git describe --tags --always --match 'v*')'"
  local _goldflags="$_goldflags -X 'main.appCommit=$(git rev-parse HEAD)'"
  local _goldflags="$_goldflags -X 'main.appDate=$(date -u '+%F %T')'"
  go build \
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
