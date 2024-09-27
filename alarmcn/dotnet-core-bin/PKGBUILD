# Maintainer: Attila Greguss <floyd0122[at]gmail[dot]com>
# Co-Maintainer: Nate Plumm <nate[at]ceresta[dot]com>

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
pkgver=8.0.8.sdk402
_runtimever=8.0.8
_sdkver=8.0.402
_short_ver=8.0
pkgrel=2
arch=('x86_64' 'armv7h' 'aarch64')
url='https://www.microsoft.com/net/core'
license=('MIT')
options=('staticlibs')
source=('dotnet.sh')
source_armv7h=('https://download.visualstudio.microsoft.com/download/pr/3f1915a5-3dce-4e1b-89c8-d1d3e5c748f0/2acbc06979a9c5c40774a0314557baeb/dotnet-sdk-8.0.402-linux-arm.tar.gz')
source_aarch64=('https://download.visualstudio.microsoft.com/download/pr/42db7609-0abd-4645-a474-a3c9a4e27066/31ef83a143f817c7b085d4989904eebd/dotnet-sdk-8.0.402-linux-arm64.tar.gz')
source_x86_64=('https://download.visualstudio.microsoft.com/download/pr/1ebffeb0-f090-4001-9f13-69f112936a70/5dbc249b375cca13ec4d97d48ea93b28/dotnet-sdk-8.0.402-linux-x64.tar.gz')
sha512sums=('dbb0633698b82bcc2c87c714b9f8f41b474133e8da65f4f13713d302905af65e0a1c796766deb60e00de0761e0fa8015cb3858f5ac8691e4e1cbd117ac105447')
sha512sums_armv7h=('ac654aded46a89a825f5e7471332834800b1a11a14bcd92282da155bea89966add3fa9ed8281d6f20bd4a4f5d2c5aefaf454c0c630cda09aa759c2f6a7755d10')
sha512sums_aarch64=('03a98e2fa90902f1251f231e268eb70c59639ef806d0466ce14ec3224d0739526a38982ca84d68e76ebd99f5962d6d490915358aa70e9276842e4f148fbd9596')
sha512sums_x86_64=('a74f5cb0ac34ac3889c7616da7386563103e28a60fc8f767857f9b65c34c34d11301593de6b248d26c72557d63c18b0f7ce15bbcc0114f321c5e14dcec98008c')

package_dotnet-host-bin() {
  pkgdesc='A generic driver for the .NET Core Command Line Interface (binary)'
  provides=("dotnet-host" "dotnet-host=${_runtimever}")
  depends=(
    'gcc-libs'
    'glibc'
  )
  conflicts=('dotnet-host')

  install -dm 755 "${pkgdir}"/usr/{bin,lib,share/{dotnet,licenses/dotnet-host}}
  cp -dr --no-preserve='ownership' dotnet host "${pkgdir}"/usr/share/dotnet/
  cp -dr --no-preserve='ownership' LICENSE.txt ThirdPartyNotices.txt "${pkgdir}"/usr/share/licenses/dotnet-host
  ln -sf /usr/share/dotnet/dotnet "${pkgdir}"/usr/bin/dotnet
  ln -sf /usr/share/dotnet/host/fxr/"${_runtimever}"/libhostfxr.so "${pkgdir}"/usr/lib/libhostfxr.so
  install -Dm 644 "${srcdir}"/dotnet.sh -t "${pkgdir}"/etc/profile.d/
}

package_dotnet-runtime-bin() {
  pkgdesc='The .NET Core runtime (binary)'
  depends=(
  	"dotnet-host>=${_runtimever}"
    'gcc-libs'
    'glibc'
    'icu'
    'libgssapi_krb5.so'
    'libunwind'
    'zlib'
    'openssl'
  )
  optdepends=('lttng-ust: CoreCLR tracing')
  provides=("dotnet-runtime=${_runtimever}" "dotnet-runtime-${_short_ver}")
  conflicts=("dotnet-runtime=${_runtimever}" "dotnet-runtime-${_short_ver}")

  install -dm 755 "${pkgdir}"/usr/share/{dotnet/shared,licenses}
  cp -dr --no-preserve='ownership' shared/Microsoft.NETCore.App "${pkgdir}"/usr/share/dotnet/shared/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/dotnet-runtime-bin
}

package_aspnet-runtime-bin() {
  pkgdesc='The ASP.NET Core runtime (binary)'
  depends=('dotnet-runtime-bin')
  provides=("aspnet-runtime=${_runtimever}" "aspnet-runtime-${_short_ver}")
  conflicts=("aspnet-runtime=${_runtimever}" "aspnet-runtime-${_short_ver}")

  install -dm 755 "${pkgdir}"/usr/share/{dotnet/shared,licenses}
  cp -dr --no-preserve='ownership' shared/Microsoft.AspNetCore.App "${pkgdir}"/usr/share/dotnet/shared/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/aspnet-runtime-bin
}

package_dotnet-sdk-bin() {
  pkgdesc='The .NET Core SDK (binary)'
  depends=(
    'glibc'
    'gcc-libs'
    'dotnet-runtime-bin'
    'dotnet-targeting-pack-bin'
    'netstandard-targeting-pack-bin')
  optdepends=('aspnet-targeting-pack-bin: Build ASP.NET Core applications')
  provides=("dotnet-sdk-bin" "dotnet-sdk=${pkgver}" "dotnet-sdk-${_short_ver}=${pkgver}")
  conflicts=("dotnet-sdk-bin" "dotnet-sdk=${pkgver}" "dotnet-sdk-${_short_ver}")

  install -dm 755 "${pkgdir}"/usr/share/{dotnet,licenses}
  cp -dr --no-preserve='ownership' sdk sdk-manifests templates "${pkgdir}"/usr/share/dotnet/
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
  provides=(dotnet-targeting-pack=${_runtimever} dotnet-targeting-pack-${_short_ver})
  conflicts=(dotnet-targeting-pack=${_runtimever} dotnet-targeting-pack-${_short_ver})

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
  provides=(aspnet-targeting-pack=${_runtimever} aspnet-targeting-pack-${_short_ver})
  conflicts=(aspnet-targeting-pack=${_runtimever} aspnet-targeting-pack-${_short_ver})

  install -dm 755 "${pkgdir}"/usr/share/{dotnet,dotnet/packs,licenses}
  cp -dr --no-preserve='ownership' packs/Microsoft.AspNetCore.App.Ref "${pkgdir}"/usr/share/dotnet/packs/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/aspnet-targeting-pack-bin
}