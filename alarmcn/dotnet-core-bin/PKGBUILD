# Maintainer: Attila Greguss <floyd0122[at]gmail[dot]com>
# Co-Maintainer: Nate Plumm <nate[at]ceresta[dot]com>

pkgbase=dotnet-core-bin
pkgname=(
  'dotnet-host-bin'
  'aspnet-runtime-bin'
  'dotnet-runtime-bin'
  'dotnet-sdk-bin'
  'dotnet-targeting-pack-bin'
  'aspnet-targeting-pack-bin'
 )
pkgver=10.0.14.sdk403
_runtimever=10.0.14
_sdkver=10.0.403
_short_ver=10.0
pkgrel=1
arch=('x86_64' 'armv7h' 'aarch64')
url='https://www.microsoft.com/net/core'
license=('MIT')
options=('staticlibs')
source=(
  'dotnet.sh'
  "https://raw.githubusercontent.com/dotnet/dotnet/v${_runtimever}/src/sdk/scripts/register-completions.bash"
  "https://raw.githubusercontent.com/dotnet/dotnet/v${_runtimever}/src/sdk/scripts/register-completions.zsh"
)
source_armv7h=("https://builds.dotnet.microsoft.com/dotnet/Sdk/${_sdkver}/dotnet-sdk-${_sdkver}-linux-arm.tar.gz")
source_aarch64=("https://builds.dotnet.microsoft.com/dotnet/Sdk/${_sdkver}/dotnet-sdk-${_sdkver}-linux-arm64.tar.gz")
source_x86_64=("https://builds.dotnet.microsoft.com/dotnet/Sdk/${_sdkver}/dotnet-sdk-${_sdkver}-linux-x64.tar.gz")
sha512sums=('768151c7179fb6a126b3de9cae01e363e8894f6fab384b1e2c5066c2adca4578638983b1b62aea10dd18045e6d6e8f8ea13280481134de94f004a118919b2c06'
            '9f977e0bd12abc0dda4d914f369c58fce502b4030cf91d4248b32242d98fe5a2bbd8446502feeb914561f310dfd3c113bb6da19bfd5dfa6233109e62d22fa966'
            '3a7f3572a09ea93b2c4512fd1af76eae8b1d7572974ad710b45d46663e031971ab617598da94e6280300c147cea41071a65a10991faca56a29904466a6769668')
sha512sums_armv7h=('a53b1fc7e0d509a40fd38ee3df93ec00ae951465d02198ccb9a7d4ead611b1e2627ee2353df6fd1f25595a5596bfd36f38ce249f7b217c432a693a5a9f9c8749')
sha512sums_aarch64=('0966aa2b70f4677b8319be9df447a78a0dcd6164836425b55a68fd714f4023feb87b4cac21b9a996b79472ad54487cd0adcd2a9dfd570e2b2a1d26423a2baa9b')
sha512sums_x86_64=('b7b3d8461cf98b07d2552ce9199702fa3ad010ac2671a5f8cd5136f7534e50f6855ba7bbb02b11494563f1d04156276a31cda1103b900e5eecd0d9473dc7b9c5')

package_dotnet-host-bin() {
  pkgdesc='A generic driver for the .NET Core Command Line Interface (binary)'
  provides=("dotnet-host" "dotnet-host=${_runtimever}")
  conflicts=('dotnet-host')
  depends=(
    'libgcc'
    'libstdc++'
    'glibc'
  )
  optdepends=('bash-completion: Bash completion support')

  install -dm 755 "${pkgdir}"/usr/{bin,lib,share/{dotnet,dnx,licenses/dotnet-host}}
  cp -dr --no-preserve='ownership' dotnet host dnx "${pkgdir}"/usr/share/dotnet/
  cp -dr --no-preserve='ownership' LICENSE.txt ThirdPartyNotices.txt "${pkgdir}"/usr/share/licenses/dotnet-host
  ln -sf /usr/share/dotnet/dotnet "${pkgdir}"/usr/bin/dotnet
  ln -sf /usr/share/dotnet/dnx "${pkgdir}"/usr/bin/dnx
  ln -sf /usr/share/dotnet/host/fxr/"${_runtimever}"/libhostfxr.so "${pkgdir}"/usr/lib/libhostfxr.so
  install -Dm 644 "${srcdir}"/dotnet.sh -t "${pkgdir}"/etc/profile.d/
  install -Dm 644 "${srcdir}"/register-completions.bash "${pkgdir}"/usr/share/bash-completion/completions/dotnet
  install -Dm 644 "${srcdir}"/register-completions.zsh "${pkgdir}"/usr/share/zsh/site-functions/_dotnet
}

package_dotnet-runtime-bin() {
  pkgdesc='The .NET Core runtime (binary)'
  depends=(
  	"dotnet-host>=${_runtimever}"
    'libgcc'
    'libstdc++'
    'glibc'
    'icu'
    'krb5'
    'libunwind'
    'zlib'
    'openssl'
  )
  optdepends=('lttng-ust2.12: CoreCLR tracing')
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
    'libgcc'
    'libstdc++'
    'dotnet-runtime-bin'
    'dotnet-targeting-pack-bin'
  )
  optdepends=(
    'aspnet-runtime-bin: Run ASP.NET Core applications'
    'aspnet-targeting-pack-bin: Build ASP.NET Core applications'
  )
  provides=("dotnet-sdk-bin" "dotnet-sdk=${pkgver}" "dotnet-sdk-${_short_ver}=${pkgver}")
  conflicts=("dotnet-sdk-bin" "dotnet-sdk=${pkgver}" "dotnet-sdk-${_short_ver}")

  install -dm 755 "${pkgdir}"/usr/share/{dotnet,licenses}
  cp -dr --no-preserve='ownership' sdk sdk-manifests templates "${pkgdir}"/usr/share/dotnet/
  install -dm 755 "${pkgdir}"/usr/share/dotnet/metadata/workloads/"${_sdkver}"
  touch "${pkgdir}"/usr/share/dotnet/metadata/workloads/"${_sdkver}"/userlocal
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/dotnet-sdk-bin
}

package_dotnet-targeting-pack-bin() {
  pkgdesc='The .NET Core targeting pack (binary)'
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