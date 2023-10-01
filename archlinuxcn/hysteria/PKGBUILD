# Maintainer: Haruue Icymoon <i@haruue.moe>

_pkgbase=hysteria
pkgname=$_pkgbase
pkgver=2.0.3
pkgrel=1
pkgdesc='A powerful, lightning fast and censorship resistant proxy'
arch=('x86_64')
url="https://hysteria.network/"
license=('MIT')
depends=('glibc' 'acl' 'shadow')
makedepends=('go' 'git')
install=$_pkgbase.install
source=("$_pkgbase-git"::"git+https://github.com/apernet/hysteria.git#tag=app/v$pkgver"
        hysteria@.service
        hysteria-server@.service
        sysusers.conf
        tmpfiles.conf
        )
sha256sums=('SKIP'
            '93b139bcb6ca1500ad7bd43d8a20d0edd4eb36e1b8ca608819dbe6783519deb7'
            '9269693b913e652aca2efadf10e29bd761df83505aef803fdd2223abc72034d9'
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
  local _app_src_cmd_pkg="github.com/apernet/hysteria/app/cmd"
  local _goldflags="-w -s -linkmode=external"
  local _goldflags="$_goldflags -buildid="
  local _goldflags="$_goldflags -X '$_app_src_cmd_pkg.appVersion=$(git describe --tags --always --match 'app/v*' | grep -o "v.*")'"
  local _goldflags="$_goldflags -X '$_app_src_cmd_pkg.appDate=$(date -u '+%Y-%m-%dT%H:%M:%SZ')'"
  local _goldflags="$_goldflags -X '$_app_src_cmd_pkg.appType=release'"
  local _goldflags="$_goldflags -X '$_app_src_cmd_pkg.appCommit=$(git rev-parse HEAD)'"
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
