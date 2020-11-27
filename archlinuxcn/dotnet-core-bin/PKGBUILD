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
pkgver=5.0.0.sdk100
_runtimever=5.0.0
_sdkver=5.0.100
pkgrel=1
arch=('x86_64' 'armv7h' 'aarch64')
url='https://www.microsoft.com/net/core'
license=('MIT')
options=('staticlibs')
source_armv7h=('https://download.visualstudio.microsoft.com/download/pr/e8912d3b-483b-4d6f-bd3a-3066b3194313/20f2261fe4e16e55df4bbe03c65a7648/dotnet-sdk-5.0.100-linux-arm.tar.gz')
source_aarch64=('https://download.visualstudio.microsoft.com/download/pr/27840e8b-d61c-472d-8e11-c16784d40091/ae9780ccda4499405cf6f0924f6f036a/dotnet-sdk-5.0.100-linux-arm64.tar.gz')
source_x86_64=('https://download.visualstudio.microsoft.com/download/pr/820db713-c9a5-466e-b72a-16f2f5ed00e2/628aa2a75f6aa270e77f4a83b3742fb8/dotnet-sdk-5.0.100-linux-x64.tar.gz')
sha512sums_armv7h=('c61a0910e34a5d7bffee46835242c24a153bf346e0ef1b048a47d12e60408aa722cec0a08fa1461ab615a4f0d09ef470c479d393f93929837f18699c745c1314')
sha512sums_aarch64=('5fceac0a9468097d66af25516da597eb4836b294ed1647ba272ade5c8faea2ed977a95d9ce720c44d71607fa3a0cf9de55afe0e66c0c89ab1cc6736945978204')
sha512sums_x86_64=('bec37bfb327c45cc01fd843ef93b22b556f753b04724bba501622df124e7e144c303a4d7e931b5dbadbd4f7b39e5adb8f601cb6293e317ad46d8fe7d52aa9a09')

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