# Maintainer: pandada8 <pandada8@gmail.com>
pkgname=v2ray
pkgver=2.47
pkgrel=3
pkgdesc="A platform for building proxies to bypass network restrictions."
arch=('i686' 'x86_64')
url="https://github.com/v2ray/v2ray-core"
license=('MIT')

source=('v2ray.service' 'https://raw.githubusercontent.com/v2ray/v2ray-core/master/LICENSE')

source_i686=(v2ray-linux-32-$pkgver.zip::https://github.com/v2ray/v2ray-core/releases/download/v$pkgver/v2ray-linux-32.zip)
source_x86_64=(v2ray-linux-64-$pkgver.zip::https://github.com/v2ray/v2ray-core/releases/download/v$pkgver/v2ray-linux-64.zip)

md5sums=('46c94d3cff90cf10869e2fe9e804314f'
         '22ecbf92e9821283dc3f8937890c0c5e')
md5sums_i686=('eef1ccfc3d55fad6b9ceced4f8876e84')
md5sums_x86_64=('50097d5d2f3cccf1943677aad8b21333')

arch_map=( ["i686"]="32"  ["x86_64"]="64")

package() {
  dir="$srcdir/v2ray-v$pkgver-linux-${arch_map[$CARCH]}"
  $dir/v2ctl verify -sig $dir/v2ctl.sig $dir/v2ctl
  $dir/v2ctl verify -sig $dir/v2ray.sig $dir/v2ray
  install -Dm644 v2ray.service ${pkgdir}/usr/lib/systemd/system/v2ray@.service
  install -Dm644 LICENSE ${pkgdir}/usr/share/licenses/v2ray/LICENSE
  install -Dm644 $dir/systemd/v2ray.service ${pkgdir}/usr/lib/systemd/system/v2ray.service
  sed -i '/ExecStart/c\ExecStart=/usr/bin/env v2ray.location.asset=/etc/v2ray /usr/bin/v2ray -config /etc/v2ray/config.json' ${pkgdir}/usr/lib/systemd/system/v2ray.service
  install -Dm644 $dir/geoip.dat $dir/geosite.dat $dir/*.json -t ${pkgdir}/etc/v2ray/
  install -Dm755 $dir/v2ray $dir/v2ctl -t ${pkgdir}/usr/bin/
}
