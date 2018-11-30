# Contributor: Dalton Miller
# Contributor: Kilian Lackhove kilian@lackhove.de
# Contributor: Justin Patera serialhex@gmail.com
# Contributor: ava1ar <mail(at)ava1ar(dot)me>
# Maintainer: widowild

pkgname=rslsync
pkgver=2.6.2
pkgrel=1
pkgdesc="Resilio Sync (ex:BitTorrent Sync) - automatically sync files via secure, distributed technology"
license=("custom:resilio")
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://www.getsync.com"
install=rslsync.install
backup=('etc/rslsync.conf')
conflicts=()
source=(rslsync.service rslsync_user.service rslsync.tmpfiles)
source_arm=("rslsync_arm-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.resilio.com/stable/linux-arm/resilio-sync_arm.tar.gz")
source_armv6h=("rslsync_arm-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.resilio.com/stable/linux-arm/resilio-sync_arm.tar.gz")
source_armv7h=("rslsync_armhf-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.resilio.com/stable/linux-armhf/resilio-sync_armhf.tar.gz")
source_aarch64=("rslsync_arm64-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.resilio.com/stable/linux-arm64/resilio-sync_arm64.tar.gz")
source_i686=("rslsync_i386-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.resilio.com/stable/linux-i386/resilio-sync_i386.tar.gz")
source_x86_64=("rslsync_x64-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.resilio.com/stable/linux-x64/resilio-sync_x64.tar.gz")
sha256sums=('4483cbe3fff81281666d8fbe8c9b8d7d27c38ba7a3d3752a865f1ab8c1f212db'
            'ba4b0ee3303027122e67345d4bf852f911a56f213f98c9eaa198c69d903fd8a1'
            '150408a99eea8082b1df115c2c836f4e8e68a85eba7cd56b5885ebd4e07dceda')
sha256sums_i686=('b06cc3facd01de583a1d432394c7e43a1353200a605068ed636be336571278bf')
sha256sums_x86_64=('82f940a130a0e82c3b020dd9cb1381ae0c0f2b52dee1b7eff81f90b3c997086f')
sha256sums_arm=('29ef3db304a47ead441e9a998adf497e3f9f964cbe60a755356001c3f08f1816')
sha256sums_armv6h=('29ef3db304a47ead441e9a998adf497e3f9f964cbe60a755356001c3f08f1816')
sha256sums_armv7h=('ccd2f3e6e0c7f25e4409194cc666bc3055f5c48f7e04ced87b2763c49d34f886')
sha256sums_aarch64=('da4549077bfab205f3a5514c65c9ffb83d35540703c48b5748c87a10712d4dfe')


package() {
  # install main binary
  install -Dm755 "${srcdir}"/rslsync "${pkgdir}"/usr/bin/rslsync
  
  # generate and install system-wide config
  mkdir -p "${pkgdir}"/etc
  ./rslsync --dump-sample-config \
  | sed 's:/home/user/\.sync:/var/lib/rslsync:' \
  | sed 's:\/\/ "pid_file":  "pid_file":' \
  | sed 's:\/\/ "storage_path":  "storage_path":' \
  | sed 's/\/var\/run\/resilio/\/run\/resilio/g' \
  > "${pkgdir}"/etc/rslsync.conf
  chmod 644 "${pkgdir}"/etc/rslsync.conf

  # install systemd config files
  install -Dm644 "${srcdir}"/rslsync.service "${pkgdir}"/usr/lib/systemd/system/rslsync.service
  install -Dm644 "${srcdir}"/rslsync.tmpfiles "${pkgdir}"/usr/lib/tmpfiles.d/rslsync.conf
  install -Dm644 "${srcdir}"/rslsync_user.service "${pkgdir}"/usr/lib/systemd/user/rslsync.service

  # install license
  install -Dm644 "${srcdir}"/LICENSE.TXT "${pkgdir}"/usr/share/licenses/${pkgname}/license.txt
}
