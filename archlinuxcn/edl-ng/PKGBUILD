# Maintainer: Cryolitia PukNgae <cryolitia@archlinuxcn.org>

pkgname=edl-ng
pkgver=1.5.0
pkgrel=1
pkgdesc="A modern, user-friendly tool for interacting with Qualcomm devices in Emergency Download (EDL) mode."
arch=('x86_64')
url="https://github.com/strongtz/edl-ng"
license=( 'MIT' )
depends=(glibc libusb)
makedepends=(git dotnet-sdk-9.0)
source=("$pkgname::git+$url#tag=v$pkgver")
sha512sums=('98af40031587c7253895ef1ddd59549647964c92a6a61aa7f2003a24d8e1888a227a472a622f78ffa03d1216a5c18af0b09d433d669f67a0edcc988864839295')
b2sums=('a93d081d2c0a4697fa6c9000dc660ca8d06246f6d764db5373a5779514a5de9d2f27bef8d37a6fbc53593bab89ace6c77c014499e648dc46c4b00e0be1e49387')

prepare() {
  cd "$pkgname"

  sed -i "/Microsoft.CodeAnalysis.CSharp/{s/4.14.0/4.12.0/}" QCEDL.Analyzer/QCEDL.Analyzer.csproj
}

build(){
  cd "$pkgname"

  # disable dotnet telemetry
  export DOTNET_CLI_TELEMETRY_OPTOUT=1
  export DOTNET_SKIP_FIRST_TIME_EXPERIENCE=1
  export DOTNET_NOLOGO=1

  dotnet \
    publish \
    QCEDL.CLI \
    --configuration Release \
    --output builddir \
    --os linux \
    -p:DebugSymbols=false \
    -p:DebugType=none
}

package() {
  cd "$pkgname"

  # install binaries
  install -vd "$pkgdir/usr/"{lib,bin}
  cp -r builddir "$pkgdir/usr/lib/$pkgname"
  ln -sf /usr/lib/edl-ng/edl-ng "$pkgdir/usr/bin/edl-ng"

  install -Dvm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname/"

  # ensure binaries have correct permissions
  chmod 755 "$pkgdir/usr/lib/$pkgname/edl-ng"
}

