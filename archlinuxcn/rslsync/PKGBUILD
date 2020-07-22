# Contributor: Dalton Miller
# Contributor: Kilian Lackhove kilian@lackhove.de
# Contributor: Justin Patera serialhex@gmail.com
# Contributor: ava1ar <mail(at)ava1ar(dot)me>
# Maintainer: widowild

pkgname=rslsync
pkgver=2.7.2
pkgrel=1
pkgdesc="Resilio Sync (ex:BitTorrent Sync) - automatically sync files via secure, distributed technology"
license=("custom:resilio")
arch=('i686' 'x86_64' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://www.getsync.com"
install=rslsync.install
backup=('etc/rslsync.conf')
conflicts=()
source=('rslsync.service'
        'rslsync_user.service'
        'rslsync.tmpfiles'
        'rslsync.sysusers')
source_arm=("rslsync_arm-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.resilio.com/stable/linux-arm/resilio-sync_arm.tar.gz")
source_armv6h=("rslsync_arm-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.resilio.com/stable/linux-arm/resilio-sync_arm.tar.gz")
source_armv7h=("rslsync_armhf-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.resilio.com/stable/linux-armhf/resilio-sync_armhf.tar.gz")
source_aarch64=("rslsync_arm64-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.resilio.com/stable/linux-arm64/resilio-sync_arm64.tar.gz")
source_i686=("rslsync_i386-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.resilio.com/stable/linux-i386/resilio-sync_i386.tar.gz")
source_x86_64=("rslsync_x64-${pkgver}-${pkgrel}.tar.gz::https://download-cdn.resilio.com/stable/linux-x64/resilio-sync_x64.tar.gz")
sha256sums=('4483cbe3fff81281666d8fbe8c9b8d7d27c38ba7a3d3752a865f1ab8c1f212db'
            'ba4b0ee3303027122e67345d4bf852f911a56f213f98c9eaa198c69d903fd8a1'
            '58ba5cef05bcfde72c5841eaeffaa4d31c39e26902b5fefb2e17eb9b629416cf'
            '3c69179987c2e0f54b2f3478ab421c65515f5b5b9bad2b6e055ec04aea0f5c6d')
sha256sums_i686=('dc6c1f11c17cea46bd6254c2fd19ad5ff5edd1fce26e0fa7d47e0768503e9aaf')
sha256sums_x86_64=('0e9e92eb0deeb9314e9676275e91fdce6d6296b352637e7dc59eecb03f2d593d')
sha256sums_arm=('632a51c5c051ec2b24225e9f7f415d3c73349fd29ec9ab10d8bf1a04015adade')
sha256sums_armv6h=('632a51c5c051ec2b24225e9f7f415d3c73349fd29ec9ab10d8bf1a04015adade')
sha256sums_armv7h=('ae3fdbfa0249f9dc621d91c939fa7f5df023486f1e814bedee27ff06bffd11d6')
sha256sums_aarch64=('c2a9630ec671096be5d1744592bd74dea27d6b70d83e143b568a2de458991c49')


package() {
  # install main binary
  install -D -m 755 "${srcdir}"/rslsync "${pkgdir}"/usr/bin/rslsync
  
  # generate and install system-wide config
  mkdir -p "${pkgdir}"/etc
  ./rslsync --dump-sample-config \
  | sed 's:/home/user/\.sync:/var/lib/rslsync:' \
  | sed 's:\/\/ "pid_file":  "pid_file":' \
  | sed 's:\/\/ "storage_path":  "storage_path":' \
  | sed 's/\/var\/run\/resilio/\/run\/resilio/g' \
  > "${pkgdir}"/etc/rslsync.conf

  # install systemd config files
  install -D -m 644 "${srcdir}"/rslsync.service "${pkgdir}"/usr/lib/systemd/system/rslsync.service
  install -D -m 644 "${srcdir}"/rslsync.tmpfiles "${pkgdir}"/usr/lib/tmpfiles.d/rslsync.conf
  install -D -m 644 "${srcdir}"/rslsync_user.service "${pkgdir}"/usr/lib/systemd/user/rslsync.service
  install -D -m 644 "${srcdir}/rslsync.sysusers" "${pkgdir}/usr/lib/sysusers.d/rslsync.conf"

  # install license
  install -D -m 644 "${srcdir}"/LICENSE.TXT "${pkgdir}"/usr/share/licenses/${pkgname}/license.txt
}
