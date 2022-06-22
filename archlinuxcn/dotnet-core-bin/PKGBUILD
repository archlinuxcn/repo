# Maintainer: Attila Greguss <floyd0122[at]gmail[dot]com>

pkgname=dotnet-sdk-bin
pkgver=3.1.100
pkgrel=1
pkgdesc='The .NET Core SDK (binary version)'
arch=('x86_64' 'armv7h' 'aarch64')
url='https://dotnet.microsoft.com/download/dotnet-core'
license=('MIT')
depends=('dotnet-runtime>=3.1.0')
optdepends=('aspnet-runtime>=3.1.0: ASP.NET build support')
options=('staticlibs')
provides=("dotnet-sdk=${pkgver%+*}")
source_armv7h=('https://download.visualstudio.microsoft.com/download/pr/67766a96-eb8c-4cd2-bca4-ea63d2cc115c/7bf13840aa2ed88793b7315d5e0d74e6/dotnet-sdk-3.1.100-linux-arm.tar.gz')
source_aarch64=('https://download.visualstudio.microsoft.com/download/pr/5a4c8f96-1c73-401c-a6de-8e100403188a/0ce6ab39747e2508366d498f9c0a0669/dotnet-sdk-3.1.100-linux-arm64.tar.gz')
source_x86_64=('https://download.visualstudio.microsoft.com/download/pr/d731f991-8e68-4c7c-8ea0-fad5605b077a/49497b5420eecbd905158d86d738af64/dotnet-sdk-3.1.100-linux-x64.tar.gz')
sha512sums_armv7h=('9f4848b4bca649cc6131032de4b0115549a3dafb6bf90250930794aa69f7939bba82cedda67578348a83b50b7057e452846a400589bb4e9d4a2d1b33ce57c71c')
sha512sums_aarch64=('93634c555698ca5c3392332a93551b1548fa103328401c5c25e8955f085124b887b73736b70a139fc8eb8d622e47fcfc0aa25210b73a8f851906b32eaa8a9887')
sha512sums_x86_64=('5217ae1441089a71103694be8dd5bb3437680f00e263ad28317665d819a92338a27466e7d7a2b1f6b74367dd314128db345fa8fff6e90d0c966dea7a9a43bd21')

package() {
  install -dm 755 "${pkgdir}"/{opt/dotnet,usr/share/licenses}
  cp -dr --no-preserve='ownership' packs sdk templates "${pkgdir}"/opt/dotnet/
  ln -s dotnet-host-bin "${pkgdir}"/usr/share/licenses/dotnet-sdk-bin
}
