# Contributor: Dalton Miller
# Contributor: Kilian Lackhove kilian@lackhove.de
# Contributor: Justin Patera serialhex@gmail.com
# Contributor: ava1ar <mail(at)ava1ar(dot)me>
# Maintainer: widowild

pkgname=rslsync
pkgver=2.7.0
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
sha256sums_i686=('8fce5f59ad0b083a413e5a16cc6e0200c966d12a39e0721964923ce1221d7e7b')
sha256sums_x86_64=('ce1415403e089350bf6966af08d5822defd3e6d4a1cb902abc28d6f7fc247c9f')
sha256sums_arm=('bf1242a271c9ad23b0a34f247860981c8de8686ebd1300c1073513a4bfdf5188')
sha256sums_armv6h=('bf1242a271c9ad23b0a34f247860981c8de8686ebd1300c1073513a4bfdf5188')
sha256sums_armv7h=('d4123febd2e463b64fbe4ac42151f2c4cab1a7d549ade8fe994a38b593c8c23b')
sha256sums_aarch64=('c4780cbbcd77a5d9cb023050e29a82216c0cebc37564349bff7edc0eccdba533')


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
