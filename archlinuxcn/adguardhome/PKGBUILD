# Maintainer graysky <graysky AT archlinux DOT us>

pkgname=adguardhome
_pkgname=AdGuardHome
pkgver=0.103.3
pkgrel=3
pkgdesc="Network-wide ads and trackers blocking DNS server"
arch=('x86_64')
url="https://github.com/AdguardTeam/AdGuardHome"
license=('GPL')
source=("$pkgname-$pkgver.tar.gz::https://github.com/AdguardTeam/AdGuardHome/archive/v$pkgver.tar.gz"
  "$_pkgname.service" sysusers.conf tmpfiles.conf
  001-Makefile-support-running-with-multiple-parallel-jobs.patch::https://github.com/AdguardTeam/AdGuardHome/commit/e57cbc36d944b6c4ebe99f397eb55976d786d5f8.patch
)
makedepends=(go npm git)
install=readme.install
sha256sums=('57db560d722d085709d27d7d15f9ae060b938fdd5ae0fb534b858e4bf55dba8f'
            '3eb76cc878f544bfc276929096c1d7d233e2e3d613886ee9a78b306ac3cd763e'
            'e9a50b7004218803ecf44c0be8c7fb28d584e8b7b3a821f26ff3478816ab0afd'
            '7cacae3dad7042f331208a47f7177a27b03a45984659df900ac175d715883aad'
            '758e7967badd0b17f4a8389e01872e9f9d643e753149d129477f6b1c888f5f29')

prepare(){
  cd "$_pkgname-$pkgver"
  patch -Np1 -i ../001-Makefile-support-running-with-multiple-parallel-jobs.patch
}

build(){
  cd "$_pkgname-$pkgver"
  make
}

package() {
  install -Dm755 "$_pkgname-$pkgver/$_pkgname" "$pkgdir/var/lib/adguardhome/$_pkgname"
  install -Dm644 "$_pkgname.service" "$pkgdir/usr/lib/systemd/system/$_pkgname.service"
  install -Dm644 "$srcdir"/sysusers.conf "$pkgdir/usr/lib/sysusers.d/$pkgname.conf"
  install -Dm644 "$srcdir"/tmpfiles.conf "$pkgdir/usr/lib/tmpfiles.d/$pkgname.conf"
}
