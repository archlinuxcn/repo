# Maintainer: Luca Weiss <luca (at) z3ntu (dot) xyz>
# Contributor: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Daniel Seymour <dannyseeless@gmail.com>

pkgbase=jellyfin
pkgname=(jellyfin jellyfin-web jellyfin-server)
pkgver=10.6.4
pkgrel=1
pkgdesc='The Free Software Media System'
arch=('i686' 'x86_64' 'armv6h')
url='https://github.com/jellyfin/jellyfin'
license=('GPL2')
makedepends=('dotnet-sdk>=3' 'yarn' 'git')
source=("jellyfin-$pkgver.tar.gz::https://github.com/jellyfin/jellyfin/archive/v$pkgver.tar.gz"
        "jellyfin-web-$pkgver.tar.gz::https://github.com/jellyfin/jellyfin-web/archive/v$pkgver.tar.gz"
        'jellyfin.conf'
        'jellyfin.service'
        'jellyfin.sysusers'
        'jellyfin.tmpfiles')
backup=('etc/conf.d/jellyfin')
sha512sums=('54fd370bedc5e809c8f6e0491c94696ef61430dd7e69691b4cfd70a90863d6921dbf4bccc056b9b21547b5b9411b0235c2fc30d61947c128633c762a38e5ac6e'
            'ae71befc3d959efd10c769e9f542849d6b9461299231e008d88e7fcff5d2369f5b88789eacddabdf98c5f7d54f526e3f2b6a3ac3bb3b73ca6ea29c54d0c83954'
            '2aa97a1a7a8a447171b59be3e93183e09cbbc32c816843cc47c6777b9aec48bd9c1d9d354f166e0b000ad8d2e94e6e4b0559aa52e5c159abbc103ed2c5afa3f0'
            '99d02080b1b92e731250f39ddd13ceca7129d69d0c05e0939620cbc3f499a9574668c63fa889704a4905560888131e980d7ab1fbcc5837b04d33ce26daa9d42b'
            '6fc2638e6ec4b1ee0240e17815c91107b694e5fde72c1bc7956c83067bbeacb632de899b86837e47a0ec04288131b15c20746373b45e0669c8976069a55d627a'
            '45a62b62d97b9a83289d4dfde684163b1bcf340c1921fb958e5a701812c61b392901841940c67e5fa5148783277d5b4dc65ba01d3a22e8f855ea62154ad9be33')

build(){
  # Build jellyfin-web
  cd jellyfin-web-$pkgver

  yarn install

  # Build jellyfin-server
  cd ../jellyfin-$pkgver

  # Disable dotnet telemetry
  export DOTNET_CLI_TELEMETRY_OPTOUT=1

  dotnet build --configuration Release Jellyfin.Server
  # Ideally, this would be run in package() with the --output variable pointing
  # to "$pkgdir"/usr/lib/jellyfin, but this step fails in fakeroot.
  # The makepkg output looks like
  #   Restore completed in 56.84 ms for /aur/jellyfin-git/src/jellyfin/Jellyfin.Server/Jellyfin.Server.csproj.
  #   ==> ERROR: A failure occurred in package().
  # without indicating any sort of failure.
  dotnet publish --configuration Release Jellyfin.Server --output "$PWD"/publish
  # Clean up the runtimes folder (keep linux-*)
  rm -rfv publish/runtimes/{alpine-*,osx*,tizen-*,win*}
}

package_jellyfin() {
  depends=("jellyfin-web=$pkgver" "jellyfin-server=$pkgver")
}

package_jellyfin-server() {
  pkgdesc="Jellyfin server component"
  depends=('dotnet-runtime>=3' 'aspnet-runtime>=3' 'ffmpeg' 'sqlite')

  mkdir -p "$pkgdir"/usr/lib
  cp -dr --no-preserve='ownership' jellyfin-$pkgver/publish "$pkgdir"/usr/lib/jellyfin

  install -Dm 644 jellyfin.service -t "$pkgdir"/usr/lib/systemd/system/
  install -Dm 644 jellyfin.sysusers "$pkgdir"/usr/lib/sysusers.d/jellyfin.conf
  install -Dm 644 jellyfin.tmpfiles "$pkgdir"/usr/lib/tmpfiles.d/jellyfin.conf
  install -Dm 644 jellyfin.conf "$pkgdir"/etc/conf.d/jellyfin
}

package_jellyfin-web() {
  pkgdesc="Jellyfin web client"

  mkdir -p "$pkgdir"/usr/lib/jellyfin
  cp -r jellyfin-web-$pkgver/dist "$pkgdir"/usr/lib/jellyfin/jellyfin-web
}

# vim: ts=2 sw=2 et:
