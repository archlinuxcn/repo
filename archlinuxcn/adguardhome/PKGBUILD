# Maintainer graysky <graysky AT archlinux DOT us>

pkgname=adguardhome
_pkgname=AdGuardHome
pkgver=0.105.1
pkgrel=1
epoch=1
pkgdesc="Network-wide ads and trackers blocking DNS server"
arch=('x86_64')
url="https://github.com/AdguardTeam/AdGuardHome"
license=('GPL')
source=("$pkgname-$pkgver.tar.gz::https://github.com/AdguardTeam/AdGuardHome/archive/v$pkgver.tar.gz"
  "$_pkgname.service" sysusers.conf tmpfiles.conf
)
makedepends=(go nodejs npm yarn git)
install=readme.install
b2sums=('8c43c595df1864f011b27db00bd46a1a945f15981d193a43cc708b0441940e2a1fc4de83a7def9283c4bd9164551b15cbf4eb82a2fec5f7747a226cb704d2c26'
        '4a337bcaf7a1c0530b51a0c436a4cd4f9ff37564f92a6ae29e5587a839c2c92aab5e669c58d52929d9517df6053ef459f23259e3bd57367cd800974db6777010'
        'ae0b990800fbf1468c261def013a1d06cc6185dd2bb85cf1a6f7a6834f3ba29c390f052b8871f2a49b2a83f297a565772c4de73649b24bdc94efd87946ef88a2'
        '430f32020a6077951fc98f8375fffed3b304645f398de4f5ce38ef2233439e23a1e3919fa9e7c93472eb2da75629c7d7ccaae9fe2c48dfe42315020c524a4053')

build(){
  cd "$_pkgname-$pkgver"
  make -j1
}

package() {
  install -Dm755 "$_pkgname-$pkgver/$_pkgname" "$pkgdir/var/lib/adguardhome/$_pkgname"
  install -Dm644 "$_pkgname.service" "$pkgdir/usr/lib/systemd/system/$_pkgname.service"
  install -Dm644 "$srcdir"/sysusers.conf "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"
  install -Dm644 "$srcdir"/tmpfiles.conf "$pkgdir/usr/lib/tmpfiles.d/$pkgname.conf"
}
