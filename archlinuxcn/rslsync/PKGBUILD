# Contributor: Dalton Miller
# Contributor: Kilian Lackhove kilian@lackhove.de
# Contributor: Justin Patera serialhex@gmail.com
# Contributor: ava1ar <mail(at)ava1ar(dot)me>
# Maintainer: widowild

pkgname=rslsync
pkgver=2.6.4
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
sha256sums_i686=('ac79dc3efe886f3cc41f67b1914b4983ffc0fdab6f7fe72428f3d7efd257eb98')
sha256sums_x86_64=('4891d7fa33bfe00a6ff907ef3e0fa601647105fa318a53a53f1795a7a49e3eb0')
sha256sums_arm=('aebff4a7a59df2082f08384ca0dcfc0c5c3c55187baf58021c0bd7520480f8c2')
sha256sums_armv6h=('aebff4a7a59df2082f08384ca0dcfc0c5c3c55187baf58021c0bd7520480f8c2')
sha256sums_armv7h=('8219a54a5a80d5bf4a9162503ef221c80b0783aa102f9f45fd93355b5ce66408')
sha256sums_aarch64=('29ba8d0b55d4cd2e1960f13f208fb732dbcc01eeccbd4b8ae0298cfbd8607290')


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
