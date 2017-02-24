# Contributor: Dalton Miller
# Contributor: Kilian Lackhove kilian@lackhove.de
# Contributor: Justin Patera serialhex@gmail.com
# Contributor: ava1ar <mail(at)ava1ar(dot)me>
# Maintainer: Flow

pkgname=rslsync
pkgver=2.4.4
pkgrel=1
pkgdesc="Resilio Sync (ex:BitTorrent Sync) - automatically sync files via secure, distributed technology"
license=("custom:resilio")
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h')
url="https://www.getsync.com"
install=rslsync.install
backup=('etc/rslsync.conf')
conflicts=()
source=(rslsync.service rslsync_user.service rslsync.conf)
source_arm=("rslsync_arm-${pkgver}.tar.gz::https://download-cdn.resilio.com/stable/linux-arm/resilio-sync_arm.tar.gz")
source_armv6h=("rslsync_arm-${pkgver}.tar.gz::https://download-cdn.resilio.com/stable/linux-arm/resilio-sync_arm.tar.gz")
source_armv7h=("rslsync_armhf-${pkgver}.tar.gz::https://download-cdn.resilio.com/stable/linux-armhf/resilio-sync_armhf.tar.gz")
source_i686=("rslsync_i386-${pkgver}.tar.gz::https://download-cdn.resilio.com/stable/linux-i386/resilio-sync_i386.tar.gz")
source_x86_64=("rslsync_x64-${pkgver}.tar.gz::https://download-cdn.resilio.com/stable/linux-x64/resilio-sync_x64.tar.gz")
sha256sums=('4483cbe3fff81281666d8fbe8c9b8d7d27c38ba7a3d3752a865f1ab8c1f212db'
            'ba4b0ee3303027122e67345d4bf852f911a56f213f98c9eaa198c69d903fd8a1'
            'acc08bf5a321a0ae1ee58aee64af524508359db6305d2164d43bb84a2a3fc7c4')
sha256sums_i686=('77a2b6e6c07526ad29426dcae4e5b84babd50d5d24aa3b0d93a3b3d2b5ce91d9')
sha256sums_x86_64=('00fb4354b713cda91a55a9e84fe4a9be5241f42b5b7b6a6df52f72ea89f1c447')
sha256sums_arm=('3a36576962f93bcefc05842f2cc7303af8a826ecb596abed4a953a7be5595532')
sha256sums_armv6h=('3a36576962f93bcefc05842f2cc7303af8a826ecb596abed4a953a7be5595532')
sha256sums_armv7h=('b71fbf1f5873ddc0cc1e926356eee27b8a83d3c045a3161eaf034728076a2287')

package() {
  # install main binary
  install -Dm755 "${srcdir}"/rslsync "${pkgdir}"/usr/bin/rslsync
  
  # generate and install system-wide config
  mkdir -p "${pkgdir}"/etc
  ./rslsync --dump-sample-config \
  | sed 's:/home/user/\.sync:/var/lib/rslsync:' \
  | sed 's:\/\/ "pid_file":  "pid_file":' \
  | sed 's:\/\/ "storage_path":  "storage_path":' \
  | sed 's/\/var\/run\/btsync\/btsync.pid/\/var\/run\/btsync\/btsync.pid/g' \
  > "${pkgdir}"/etc/rslsync.conf

  # install systemd config files
  install -Dm644 "${srcdir}"/rslsync.service "${pkgdir}"/usr/lib/systemd/system/rslsync.service
  install -Dm644 "${srcdir}"/rslsync.conf "${pkgdir}"/usr/lib/tmpfiles.d/rslsync.conf
  install -Dm644 "${srcdir}"/rslsync_user.service "${pkgdir}"/usr/lib/systemd/user/rslsync.service

  # install license
  install -Dm644 "${srcdir}"/LICENSE.TXT "${pkgdir}"/usr/share/licenses/${pkgname}/license.txt
}
