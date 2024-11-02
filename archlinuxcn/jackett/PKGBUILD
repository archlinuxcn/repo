# Maintainer: txtsd <aur.archlinux@ihavea.quest>
# Contributor: Joaquín Rufo Gutierrez <joaquinito2051@gmail.com>
# Contributor: Donald Webster <fryfrog@gmail.com>

pkgname=jackett
pkgver=0.22.873
pkgrel=1
pkgdesc='Use many torrent trackers with software that supports torznab/potato feeds.'
arch=('x86_64' 'aarch64' 'armv7h')
license=('GPL-2.0-or-later')
url='https://github.com/Jackett/Jackett'
depends=('aspnet-runtime-8.0' 'glibc' 'gcc-libs')
optdepends=(
  'flaresolverr: A proxy server to bypass Cloudflare protection'
)
makedepends=('dotnet-sdk-8.0')
options=('!strip' 'staticlibs' '!debug')

source=(
  "${pkgname}-${pkgver}.tar.gz::https://github.com/Jackett/Jackett/archive/v${pkgver}.tar.gz"
  'jackett.service'
  'jackett.sysusers'
  'jackett.tmpfiles'
)

sha256sums=('22bdc41e785425571978fcb10e3ff91da1d55a9edf1c8cf8b138cf762449975c'
            '41fbd667538c84662757f923b440d8b250ee3819cd333bd5dd561094d4ef5c3c'
            'f865c06ffd21a12d37bf05953d9b483819c0f4e43d243a56db33986113fc40e4'
            '64022e15565a609f449090f02d53ee90ef95cffec52ae14f99e4e2132b6cffe1')

build() {
  cd ${pkgname^}-${pkgver}

  case ${CARCH} in
    x86_64)  _CARCH='x64';;
    aarch64) _CARCH='arm64';;
    armv7h)  _CARCH='arm';;
  esac

  export DOTNET_CLI_TELEMETRY_OPTOUT=1
  dotnet publish src/Jackett.Server -f net8.0 --no-self-contained -r linux-${_CARCH} -c Release -o build/ /p:AssemblyVersion=${pkgver} /p:FileVersion=${pkgver} /p:InformationalVersion=${pkgver} /p:Version=${pkgver}
  # This is required because dotnet build servers do not terminate even after the parent process does
  dotnet build-server shutdown
}

package() {
  cd ${pkgname^}-${pkgver}
  install -d -m 755 "${pkgdir}/usr/lib/jackett/"
  cp -dpr --no-preserve=ownership build/* "${pkgdir}/usr/lib/jackett/"

  install -D -m 644 "${srcdir}/jackett.service" "${pkgdir}/usr/lib/systemd/system/jackett.service"
  install -D -m 644 "${srcdir}/jackett.sysusers" "${pkgdir}/usr/lib/sysusers.d/jackett.conf"
  install -D -m 644 "${srcdir}/jackett.tmpfiles" "${pkgdir}/usr/lib/tmpfiles.d/jackett.conf"
}
