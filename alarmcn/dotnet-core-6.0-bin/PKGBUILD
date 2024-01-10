# Maintainer: Attila Greguss <floyd0122[at]gmail[dot]com>
# armv7h and aarch64 Comaintainers needed

pkgbase=dotnet-core-6.0-bin
pkgname=(
  'aspnet-runtime-6.0-bin'
  'dotnet-runtime-6.0-bin'
  'dotnet-sdk-6.0-bin'
  'dotnet-targeting-pack-6.0-bin'
  'aspnet-targeting-pack-6.0-bin'
 )
pkgver=6.0.24.sdk416
_runtimever=6.0.24
_sdkver=6.0.416
pkgrel=1
arch=('x86_64' 'armv7h' 'aarch64')
url='https://www.microsoft.com/net/core'
license=('MIT')
options=('staticlibs')
source_armv7h=('https://download.visualstudio.microsoft.com/download/pr/2c8da3b8-66b9-4906-ba3c-cb536f5c46eb/b5c8900abce86499ce826798eb2fbef7/dotnet-sdk-6.0.416-linux-arm.tar.gz')
source_aarch64=('https://download.visualstudio.microsoft.com/download/pr/a56a7895-ec29-44fe-9fbf-3ea6a1bedd3d/47393de218098a0d63e9629b008abf07/dotnet-sdk-6.0.416-linux-arm64.tar.gz')
source_x86_64=('https://download.visualstudio.microsoft.com/download/pr/675f1077-ab10-40cf-ac18-d146a14ea18a/522055f875b0a2474dacfa25729d3231/dotnet-sdk-6.0.416-linux-x64.tar.gz')
sha512sums_armv7h=('b9adf8bd6e7f882ba2ab154cc149a7f3ba01becc34aa6815b7ac62454f37f282f1502c499de33bf3d450014fda8aa65fd3708406143e2048f821bd9d0d74e444')
sha512sums_aarch64=('b121ba30bd8bab2f8744f32442d93807b60dac90f8b6caa395d87151b2ffc335f93a95843f08a412d0b90c82d587301b73ea96f5a520658be729c65a061a8a80')
sha512sums_x86_64=('5a3c60c73b68e9527406a93c9cc18941d082ac988d0b4bfea277da3465c71777dded1b3389f0dde807eda6a8186fcf68d617d2473a52203cb75127ab3dafc64d')

package_dotnet-runtime-6.0-bin() {
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
  provides=("dotnet-runtime=${_runtimever}" "dotnet-runtime-6.0")
  conflicts=("dotnet-runtime=${_runtimever}" "dotnet-runtime-6.0")

  install -dm 755 "${pkgdir}"/usr/share/{dotnet/shared,licenses}
  cp -dr --no-preserve='ownership' shared/Microsoft.NETCore.App "${pkgdir}"/usr/share/dotnet/shared/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/dotnet-runtime-6.0-bin
}

package_aspnet-runtime-6.0-bin() {
  pkgdesc='The ASP.NET Core runtime (binary)'
  depends=('dotnet-runtime-6.0-bin')
  provides=("aspnet-runtime=${_runtimever}" "aspnet-runtime-6.0")
  conflicts=("aspnet-runtime=${_runtimever}" "aspnet-runtime-6.0")

  install -dm 755 "${pkgdir}"/usr/share/{dotnet/shared,licenses}
  cp -dr --no-preserve='ownership' shared/Microsoft.AspNetCore.App "${pkgdir}"/usr/share/dotnet/shared/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/aspnet-runtime-6.0-bin
}

package_dotnet-sdk-6.0-bin() {
  pkgdesc='The .NET Core SDK (binary)'
  depends=(
    'glibc'
    'gcc-libs'
    'dotnet-runtime-6.0-bin'
    'dotnet-targeting-pack-6.0-bin'
    'netstandard-targeting-pack')
  optdepends=('aspnet-targeting-pack-bin: Build ASP.NET Core applications')
  provides=("dotnet-sdk=${pkgver}" "dotnet-sdk-6.0")
  conflicts=("dotnet-sdk=${pkgver}" "dotnet-sdk-6.0")

  install -dm 755 "${pkgdir}"/usr/share/{dotnet,licenses}
  cp -dr --no-preserve='ownership' sdk sdk-manifests templates "${pkgdir}"/usr/share/dotnet/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/dotnet-sdk-6.0-bin
}

package_dotnet-targeting-pack-6.0-bin() {
  pkgdesc='The .NET Core targeting pack (binary)'
  depends=(
    'netstandard-targeting-pack'
  )
  provides=(dotnet-targeting-pack=${_runtimever} dotnet-targeting-pack-6.0)
  conflicts=(dotnet-targeting-pack=${_runtimever} dotnet-targeting-pack-6.0)

  if [ $CARCH = 'x86_64' ]; then msarch=x64;
  elif [ $CARCH = 'armv7h' ]; then msarch=arm;
  elif [ $CARCH = 'aarch64' ]; then msarch=arm64; fi

  install -dm 755 "${pkgdir}"/usr/share/{dotnet,dotnet/packs,licenses}
  cp -dr --no-preserve='ownership' packs/Microsoft.NETCore.App.{Host.linux-${msarch},Ref} "${pkgdir}"/usr/share/dotnet/packs/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/dotnet-targeting-pack-6.0-bin
}

package_aspnet-targeting-pack-6.0-bin() {
  pkgdesc='The ASP.NET Core targeting pack (binary)'
  depends=(
    'dotnet-targeting-pack-6.0-bin'
  )
  provides=(aspnet-targeting-pack=${_runtimever} aspnet-targeting-pack-6.0)
  conflicts=(aspnet-targeting-pack=${_runtimever} aspnet-targeting-pack-6.0)

  install -dm 755 "${pkgdir}"/usr/share/{dotnet,dotnet/packs,licenses}
  cp -dr --no-preserve='ownership' packs/Microsoft.AspNetCore.App.Ref "${pkgdir}"/usr/share/dotnet/packs/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/aspnet-targeting-pack-6.0-bin
}
