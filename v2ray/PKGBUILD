# Maintainer: pandada8 <pandada8@gmail.com>
pkgname=v2ray
pkgver=2.43
pkgrel=1
pkgdesc="A platform for building proxies to bypass network restrictions."
arch=('i686' 'x86_64')
url="https://github.com/v2ray/v2ray-core"
license=('MIT')

source=('v2ray.service' 'https://raw.githubusercontent.com/v2ray/v2ray-core/master/LICENSE')

source_i686=(v2ray-linux-32-$pkgver.zip::https://github.com/v2ray/v2ray-core/releases/download/v$pkgver/v2ray-linux-32.zip)
source_x86_64=(v2ray-linux-64-$pkgver.zip::https://github.com/v2ray/v2ray-core/releases/download/v$pkgver/v2ray-linux-64.zip)

md5sums=('453d35e39d62436aadcc3e64e91ece94'
         '22ecbf92e9821283dc3f8937890c0c5e')
md5sums_i686=('e68af7d8f249fa080bd4064b4e7b71d4')
md5sums_x86_64=('10a125538178b8cfe5b8675d810bc099')

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
