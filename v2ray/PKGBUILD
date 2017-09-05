# Maintainer: pandada8 <pandada8@gmail.com>
pkgname=v2ray
pkgver=2.36.3
pkgrel=1
pkgdesc="A platform for building proxies to bypass network restrictions."
arch=('i686' 'x86_64')
url="https://github.com/v2ray/v2ray-core"
license=('MIT')

source=('v2ray.service' 'https://raw.githubusercontent.com/v2ray/v2ray-core/master/LICENSE')

source_i686=(v2ray-linux-32.zip::https://github.com/v2ray/v2ray-core/releases/download/v$pkgver/v2ray-linux-32.zip)
source_x86_64=(v2ray-linux-64.zip::https://github.com/v2ray/v2ray-core/releases/download/v$pkgver/v2ray-linux-64.zip)

md5sums=('33e14922626081da86f868ccc4d5d7df'
         '22ecbf92e9821283dc3f8937890c0c5e')
md5sums_i686=('baa1db986b6b475a88659aa13b872edd')
md5sums_x86_64=('deccdd21607207555b6400e0f9c4de3e')

arch_map=( ["i686"]="32"  ["x86_64"]="64")

package() {
  dir="$srcdir/v2ray-v$pkgver-linux-${arch_map[$CARCH]}"
  install -Dm644 v2ray.service ${pkgdir}/usr/lib/systemd/system/v2ray@.service
  install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/v2ray/LICENSE
  install -Dm644 $dir/systemd/v2ray.service ${pkgdir}/usr/lib/systemd/system/v2ray.service
  sed -i 's/v2ray\/v2ray/v2ray/g' ${pkgdir}/usr/lib/systemd/system/v2ray.service
  install -Dm755 $dir/v2ray ${pkgdir}/usr/bin/v2ray
  install -Dm644 $dir/vpoint_socks_vmess.json ${pkgdir}/etc/v2ray/vpoint_socks_vmess.json
  install -Dm644 $dir/vpoint_vmess_freedom.json ${pkgdir}/etc/v2ray/vpoint_vmess_freedom.json
}
