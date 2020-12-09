# Maintainer: Attila Greguss <floyd0122[at]gmail[dot]com>

pkgbase=dotnet-core-bin
pkgname=(
  'dotnet-host-bin'
  'aspnet-runtime-bin'
  'dotnet-runtime-bin'
  'dotnet-sdk-bin'
  'netstandard-targeting-pack-bin'
  'dotnet-targeting-pack-bin'
  'aspnet-targeting-pack-bin'
 )
pkgver=5.0.1.sdk101
_runtimever=5.0.1
_sdkver=5.0.101
pkgrel=1
arch=('x86_64' 'armv7h' 'aarch64')
url='https://www.microsoft.com/net/core'
license=('MIT')
options=('staticlibs')
source_armv7h=('https://download.visualstudio.microsoft.com/download/pr/567a64a8-810b-4c3f-85e3-bc9f9e06311b/02664afe4f3992a4d558ed066d906745/dotnet-sdk-5.0.101-linux-arm.tar.gz')
source_aarch64=('https://download.visualstudio.microsoft.com/download/pr/2add7523-39ec-413a-b8a7-24361cc4e599/30489ebd7ebcc723da48a64669860fd0/dotnet-sdk-5.0.101-linux-arm64.tar.gz')
source_x86_64=('https://download.visualstudio.microsoft.com/download/pr/a0487784-534a-4912-a4dd-017382083865/be16057043a8f7b6f08c902dc48dd677/dotnet-sdk-5.0.101-linux-x64.tar.gz')
sha512sums_armv7h=('2b03ae553b59ad39aa22b5abb5b208318b15284889a86abdc3096e382853c28b0438e2922037f9bc974c85991320175ba48d7a6963bb112651d7027692bb5cde')
sha512sums_aarch64=('b26beafd7649fd9081a914909aca6302e8629f24d97ac5d7ac4c7aace007aff93e920510f3fa5a871c71ad42f2e38241115339ccf01d2399b2c9000b53607a86')
sha512sums_x86_64=('398d88099d765b8f5b920a3a2607c2d2d8a946786c1a3e51e73af1e663f0ee770b2b624a630b1bec1ceed43628ea8bc97963ba6c870d42bec064bde1cd1c9edb')

package_dotnet-host-bin() {
  pkgdesc='A generic driver for the .NET Core Command Line Interface (binary)'
  provides=("dotnet-host" "dotnet-host=${_runtimever}")
  conflicts=('dotnet-host')

  install -dm 755 "${pkgdir}"/usr/{bin,lib,share/{dotnet,licenses/dotnet-host}}
  cp -dr --no-preserve='ownership' dotnet host "${pkgdir}"/usr/share/dotnet/
  cp -dr --no-preserve='ownership' LICENSE.txt ThirdPartyNotices.txt "${pkgdir}"/usr/share/licenses/dotnet-host
  ln -sf /usr/share/dotnet/dotnet "${pkgdir}"/usr/bin/dotnet
  ln -sf /usr/share/dotnet/host/fxr/"${_runtimever}"/libhostfxr.so "${pkgdir}"/usr/lib/libhostfxr.so
}

package_dotnet-runtime-bin() {
  pkgdesc='The .NET Core runtime (binary)'
  depends=("dotnet-host>=${_runtimever}"
           'glibc'
           'icu' 
           'krb5'
           'libcurl.so'
           'libunwind'
           'openssl'
           'zlib'
  )
  optdepends=('lttng-ust: CoreCLR tracing')
  provides=("dotnet-runtime-bin" "dotnet-runtime=${_runtimever}" "dotnet-runtime-5.0")
  conflicts=("dotnet-runtime-bin" "dotnet-runtime=${_runtimever}" "dotnet-runtime-5.0")

  install -dm 755 "${pkgdir}"/usr/share/{dotnet/shared,licenses}
  cp -dr --no-preserve='ownership' shared/Microsoft.NETCore.App "${pkgdir}"/usr/share/dotnet/shared/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/dotnet-runtime-bin
}

package_aspnet-runtime-bin() {
  pkgdesc='The ASP.NET Core runtime (binary)'
  depends=('dotnet-runtime-bin')
  provides=("aspnet-runtime-bin" "aspnet-runtime=${_runtimever}" "aspnet-runtime-5.0")
  conflicts=("aspnet-runtime-bin" "aspnet-runtime=${_runtimever}" "aspnet-runtime-5.0")

  install -dm 755 "${pkgdir}"/usr/share/{dotnet/shared,licenses}
  cp -dr --no-preserve='ownership' shared/Microsoft.AspNetCore.App "${pkgdir}"/usr/share/dotnet/shared/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/aspnet-runtime-bin
}

package_dotnet-sdk-bin() {
  pkgdesc='The .NET Core SDK (binary)'
  depends=(
    'dotnet-runtime-bin'
    'glibc'
    'dotnet-targeting-pack-bin'
    'netstandard-targeting-pack-2.1')
  optdepends=('aspnet-targeting-pack-bin: Build ASP.NET Core applications')
  provides=("dotnet-sdk-bin" "dotnet-sdk=${pkgver}" "dotnet-sdk-5.0")
  conflicts=("dotnet-sdk-bin" "dotnet-sdk=${pkgver}" "dotnet-sdk-5.0")

  install -dm 755 "${pkgdir}"/usr/share/{dotnet,licenses}
  cp -dr --no-preserve='ownership' sdk templates "${pkgdir}"/usr/share/dotnet/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/dotnet-sdk-bin
}

package_netstandard-targeting-pack-bin() {
  pkgdesc='The .NET Standard targeting pack (binary)'
  provides=('netstandard-targeting-pack-2.1' 'netstandard-targeting-pack-bin')
  conflicts=('netstandard-targeting-pack-2.1' 'netstandard-targeting-pack-bin')

  install -dm 755 "${pkgdir}"/usr/share/{dotnet,dotnet/packs,licenses}
  cp -dr --no-preserve='ownership' packs/NETStandard.Library.Ref "${pkgdir}"/usr/share/dotnet/packs/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/netstandard-targeting-pack
}

package_dotnet-targeting-pack-bin() {
  pkgdesc='The .NET Core targeting pack (binary)'
  depends=(netstandard-targeting-pack-2.1)
  provides=(dotnet-targeting-pack=${_runtimever} dotnet-targeting-pack-5.0)
  conflicts=(dotnet-targeting-pack=${_runtimever} dotnet-targeting-pack-5.0)

  if [ $CARCH = 'x86_64' ]; then msarch=x64;
  elif [ $CARCH = 'armv7h' ]; then msarch=arm;
  elif [ $CARCH = 'aarch64' ]; then msarch=arm64; fi

  install -dm 755 "${pkgdir}"/usr/share/{dotnet,dotnet/packs,licenses}
  cp -dr --no-preserve='ownership' packs/Microsoft.NETCore.App.{Host.linux-${msarch},Ref} "${pkgdir}"/usr/share/dotnet/packs/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/dotnet-targeting-pack-bin
}

package_aspnet-targeting-pack-bin() {
  pkgdesc='The ASP.NET Core targeting pack (binary)'
  depends=(dotnet-targeting-pack-bin)
  provides=(aspnet-targeting-pack=${_runtimever} aspnet-targeting-pack-5.0)
  conflicts=(aspnet-targeting-pack=${_runtimever} aspnet-targeting-pack-5.0)

  install -dm 755 "${pkgdir}"/usr/share/{dotnet,dotnet/packs,licenses}
  cp -dr --no-preserve='ownership' packs/Microsoft.AspNetCore.App.Ref "${pkgdir}"/usr/share/dotnet/packs/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/aspnet-targeting-pack-bin
}