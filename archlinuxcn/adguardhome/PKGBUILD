# Maintainer graysky <graysky AT archlinux DOT us>

pkgname=adguardhome
_pkgname=AdGuardHome
pkgver=0.106.1
pkgrel=3
epoch=1
pkgdesc="Network-wide ads and trackers blocking DNS server"
arch=(x86_64 aarch64 armv7h armv6h)
url="https://github.com/AdguardTeam/AdGuardHome"
license=('GPL')
source=("$pkgname-$pkgver.tar.gz::https://github.com/AdguardTeam/AdGuardHome/archive/v$pkgver.tar.gz"
  "$_pkgname.service" sysusers.conf tmpfiles.conf
)
makedepends=(go nodejs npm yarn git)
install=readme.install
b2sums=('4c5d5169464aecaad00ba93feef5e092fa24b8d3624b171351ff26526b6733947ee299ff8fbc20a1204b0a03a77a33f468e990a9dad9d5cb3b5712cb47b855d5'
        '6221c78867c502db943e74104ade432ba11ea779bb431eb642ee0d8c5f84e73d01dfac2aea4babd1dcce181d68f92f7fb7976f16db43f7effd718a46a83ed403'
        'ae0b990800fbf1468c261def013a1d06cc6185dd2bb85cf1a6f7a6834f3ba29c390f052b8871f2a49b2a83f297a565772c4de73649b24bdc94efd87946ef88a2'
        '430f32020a6077951fc98f8375fffed3b304645f398de4f5ce38ef2233439e23a1e3919fa9e7c93472eb2da75629c7d7ccaae9fe2c48dfe42315020c524a4053')

build(){
  cd "$_pkgname-$pkgver"
  # https://github.com/AdguardTeam/AdGuardHome/issues/2668

  make -j1 CHANNEL=release VERBOSE=1
}

package() {
  install -Dm755 "$_pkgname-$pkgver/$_pkgname" "$pkgdir/var/lib/adguardhome/$_pkgname"
  install -Dm644 "$_pkgname.service" "$pkgdir/usr/lib/systemd/system/$_pkgname.service"
  install -Dm644 "$srcdir"/sysusers.conf "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"
  install -Dm644 "$srcdir"/tmpfiles.conf "$pkgdir/usr/lib/tmpfiles.d/$pkgname.conf"
}
