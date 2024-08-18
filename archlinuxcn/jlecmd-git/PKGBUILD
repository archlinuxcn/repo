# Maintainer: Chih-Hsuan Yen <base64_decode("eXUzYWN0eHQydHR0ZmlteEBjaHllbi5jYwo=")>
# Based on PKGBUILD of extra/marksman
# Contributor: Jelle van der Waa <jelle@archlinux.org>

pkgname=jlecmd-git
pkgver=1.1.0.0.r54.gf76cae2
pkgrel=1
pkgdesc="Automatic and Custom Destinations jump list parser with Windows 10 support"
arch=('x86_64')
url="https://github.com/EricZimmerman/JLECmd"
license=('MIT')
makedepends=('dotnet-sdk-6.0' 'git')
depends=('dotnet-runtime-6.0')
options=('!strip')
source=(git+https://github.com/EricZimmerman/JLECmd)
b2sums=('SKIP')

pkgver() {
  cd JLECmd
  ( set -o pipefail
    git describe --long --tag 2>/dev/null | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
  )
}

prepare() {
  cd JLECmd
  sed -i 's#net462;##' JLECmd/JLECmd.csproj
}

build() {
  cd JLECmd

  # Disable dotnet telemetry
  export DOTNET_CLI_TELEMETRY_OPTOUT=1

  dotnet build --configuration Release JLECmd.sln
  dotnet publish --configuration Release JLECmd.sln --output "$PWD"/publish --framework net6.0 --no-self-contained
}

package() {
  mkdir -p "$pkgdir"/usr/lib
  mkdir -p "$pkgdir"/usr/bin
  cp -dr --no-preserve='ownership' JLECmd/publish "$pkgdir"/usr/lib/jlecmd

  ln -s /usr/lib/jlecmd/JLECmd "$pkgdir"/usr/bin/jlecmd

  install -Dm644 JLECmd/license -t "$pkgdir"/usr/share/licenses/$pkgname
}
