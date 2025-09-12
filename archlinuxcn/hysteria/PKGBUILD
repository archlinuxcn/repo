# Maintainer: Haruue Icymoon <i@haruue.moe>

_pkgbase=hysteria
pkgname=$_pkgbase
pkgver=2.6.3
pkgrel=1
pkgdesc='A powerful, lightning fast and censorship resistant proxy'
arch=('x86_64')
url="https://hysteria.network/"
license=('MIT')
depends=('glibc')
makedepends=('go' 'git' 'sed' 'grep')
optdepends=('v2ray-rules-dat: geoip/geosite data originating from V2Ray'
            'meta-rules-dat: geoip/geosite data originating from MetaCubeX')
source=("$_pkgbase-git"::"git+https://github.com/apernet/hysteria.git#tag=app/v$pkgver"
        hysteria@.service
        hysteria-server@.service
        sysusers.conf
        tmpfiles.conf
        )
sha256sums=('SKIP'
            '7f67a976138c60741ebc0dc7ba4e8ad6d284cf45f130a435a5c65aa836446d05'
            '2142db7d6bfb7df5180357f5b4b25401cf3a788624c567e58fa3ecec00a58c75'
            '44f1cb2fedfc94dc396ceb215e62237dbc8c74c035c45a3430c1f3748d266dd9'
            '1e93d9f2b312eaf02ac00229106cd796e0cd54a9a468a0a8d3ae843399c1c310')

prepare(){
  mkdir -p "$srcdir/gopath"
  export GOPATH="$srcdir/gopath"
  cd "$srcdir/$_pkgbase-git"
  mkdir -p build/
}

_get_toolchain_version() {
  go version | sed 's/^\s*//;s/\s*$//;s/^go version //'
}

_get_lib_version() {
  cat core/go.mod | sed -n 's/^\s*//;s/\s*$//;/github\.com\/apernet\/quic-go/{s/^[^ ]* //p}'
}

build() {
  cd "$srcdir/$_pkgbase-git"
  #export GOAMD64=v3
  export CGO_CPPFLAGS="${CPPFLAGS}"
  export CGO_CFLAGS="${CFLAGS}"
  export CGO_CXXFLAGS="${CXXFLAGS}"
  export CGO_LDFLAGS="${LDFLAGS}"
  local _app_src_cmd_pkg="github.com/apernet/hysteria/app/v2/cmd"
  local _goldflags="-w -s -linkmode=external"
  local _goldflags="$_goldflags -buildid="
  local _goldflags="$_goldflags -X '$_app_src_cmd_pkg.appVersion=$(git describe --tags --always --match 'app/v*' | grep -o "v.*")'"
  local _goldflags="$_goldflags -X '$_app_src_cmd_pkg.appDate=$(date -u '+%Y-%m-%dT%H:%M:%SZ')'"
  local _goldflags="$_goldflags -X '$_app_src_cmd_pkg.appType=release'"
  local _goldflags="$_goldflags -X '$_app_src_cmd_pkg.appToolchain=$(_get_toolchain_version)'"
  local _goldflags="$_goldflags -X '$_app_src_cmd_pkg.appCommit=$(git rev-parse HEAD)'"
  local _goldflags="$_goldflags -X '$_app_src_cmd_pkg.libVersion=$(_get_lib_version)'"
  local _goldflags="$_goldflags -X '$_app_src_cmd_pkg.appPlatform=$(go env GOOS)'"
  local _goldflags="$_goldflags -X '$_app_src_cmd_pkg.appArch=$(go env GOARCH)'"
  go build \
    -buildmode=pie -trimpath -mod=readonly -modcacherw \
    -o "build/$_pkgbase" \
    -ldflags "$_goldflags" \
    ./app
}

#check() {
#  cd "$srcdir/$_pkgbase-git"
#  go test ./...
#}

package() {
  # install hysteria
  install -Dm755 "$srcdir/$_pkgbase-git/build/$_pkgbase" "$pkgdir/usr/bin/$_pkgbase"

  # install sysusers
  install -Dm644 "$srcdir/sysusers.conf" "$pkgdir/usr/lib/sysusers.d/$_pkgbase.conf"
  install -Dm644 "$srcdir/tmpfiles.conf" "$pkgdir/usr/lib/tmpfiles.d/$_pkgbase.conf"

  # install systemd service
  install -Dm644 "$srcdir/hysteria@.service" "$pkgdir/usr/lib/systemd/system/hysteria@.service"
  install -Dm644 "$srcdir/hysteria-server@.service" "$pkgdir/usr/lib/systemd/system/hysteria-server@.service"

  # install license (required for MIT)
  install -Dm644 "$srcdir/$_pkgbase-git/LICENSE.md" "$pkgdir/usr/share/licenses/hysteria/LICENSE.md"

  # install config directory
  install -dm755 "$pkgdir/etc/hysteria"
}
