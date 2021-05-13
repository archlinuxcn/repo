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
pkgver=5.0.6.sdk203
_runtimever=5.0.6
_sdkver=5.0.203
pkgrel=1
arch=('x86_64' 'armv7h' 'aarch64')
url='https://www.microsoft.com/net/core'
license=('MIT')
options=('staticlibs')
source_armv7h=('https://download.visualstudio.microsoft.com/download/pr/55547694-fe7e-43f3-bf58-33ef9bb7ee85/5d8b57df472b96e6f38988041751ba2e/dotnet-sdk-5.0.203-linux-arm.tar.gz')
source_aarch64=('https://download.visualstudio.microsoft.com/download/pr/af5f1e5b-d544-47af-b730-038e4258641b/bccb3982f5690134ab66748a5afc36c7/dotnet-sdk-5.0.203-linux-arm64.tar.gz')
source_x86_64=('https://download.visualstudio.microsoft.com/download/pr/ef13f9da-46dc-4de9-a05e-5a4c20574189/be95913ebf1fb6c66833ca40060d3f65/dotnet-sdk-5.0.203-linux-x64.tar.gz')
sha512sums_armv7h=('d90409e32bab33bbc52ebcf8387e1226808672982a8014ef4cbfd42f5e7d8164f88de107e9aaa5c62c0e05cba7ae40cc226bd2fc31ccb79618f1f0bd268e2fc9')
sha512sums_aarch64=('a9d588ff27f62a73a61c1486e26046c5cd9030557d9f929617e779679e670a854e37b85fa3bbb35e768a72cd07d12b90e6ad30ae500f12303e2e9c883d07a8f0')
sha512sums_x86_64=('49d8f0414806a9c938192ed13e7707ac2609ca6c2dc408d616e56e98fc0a954b1aa3f569858f7ba38fb79b2ee36dc1920c7f08d1ba4f93da501542b1c8a1320f')

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
  provides=("dotnet-runtime=${_runtimever}" "dotnet-runtime-5.0")
  conflicts=("dotnet-runtime=${_runtimever}" "dotnet-runtime-5.0")

  install -dm 755 "${pkgdir}"/usr/share/{dotnet/shared,licenses}
  cp -dr --no-preserve='ownership' shared/Microsoft.NETCore.App "${pkgdir}"/usr/share/dotnet/shared/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/dotnet-runtime-bin
}

package_aspnet-runtime-bin() {
  pkgdesc='The ASP.NET Core runtime (binary)'
  depends=('dotnet-runtime-bin')
  provides=("aspnet-runtime=${_runtimever}" "aspnet-runtime-5.0")
  conflicts=("aspnet-runtime=${_runtimever}" "aspnet-runtime-5.0")

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
    'netstandard-targeting-pack-bin')
  optdepends=('aspnet-targeting-pack-bin: Build ASP.NET Core applications')
  provides=("dotnet-sdk-bin" "dotnet-sdk=${pkgver}" "dotnet-sdk-5.0")
  conflicts=("dotnet-sdk-bin" "dotnet-sdk=${pkgver}" "dotnet-sdk-5.0")

  install -dm 755 "${pkgdir}"/usr/share/{dotnet,licenses}
  cp -dr --no-preserve='ownership' sdk templates "${pkgdir}"/usr/share/dotnet/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/dotnet-sdk-bin
}

package_netstandard-targeting-pack-bin() {
  pkgdesc='The .NET Standard targeting pack (binary)'
  provides=('netstandard-targeting-pack-2.1' 'netstandard-targeting-pack')
  conflicts=('netstandard-targeting-pack-2.1' 'netstandard-targeting-pack')

  install -dm 755 "${pkgdir}"/usr/share/{dotnet,dotnet/packs,licenses}
  cp -dr --no-preserve='ownership' packs/NETStandard.Library.Ref "${pkgdir}"/usr/share/dotnet/packs/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/netstandard-targeting-pack
}

package_dotnet-targeting-pack-bin() {
  pkgdesc='The .NET Core targeting pack (binary)'
  depends=(netstandard-targeting-pack-bin)
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