# Maintainer: Dominik Schrempf <dominik.schrempf@gmail.com>
pkgname=nextcloud-systemd-timers
pkgver=0.6.3
pkgrel=1
epoch=
pkgdesc="Systemd services and timers for Nextcloud background jobs (see Nextcloud Arch Wiki entry)."
arch=('any')
url=""
license=('GPL')
groups=()
depends=()
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=nextcloud-systemd-timers.install
changelog=
source=("nextcloud-app-update-all.service"
        "nextcloud-app-update-all.timer"
        "nextcloud-cron.service"
        "nextcloud-cron.timer"
        "nextcloud-files-scan-all.service"
        "nextcloud-files-scan-all.timer"
        "nextcloud-preview-generate-all.service"
        "nextcloud-preview-generate-all.timer"
        "nextcloud-preview-pre-generate.service"
        "nextcloud-preview-pre-generate.timer")
sha256sums=('ee6f44559dc7d378aa4e15800cc32fd4c21834c8eb3c22337e9cc93d99d7d96a'
            '39039f1a3dc23022fccc991daca86d77e7d41be275566f6892cd6b290fa0da4a'
            '7fe27aa2ef2a034cf19a02571cefd1f6b40dd64fa48abda3ed0c82e2181f12c1'
            'a7db3a28abfee48393bd70dc71e9abf813130169229f2a35b072cc11dbd09863'
            'd81ebf8ad4a25293c0b7a80a4aa784848cfdc894eb9b799dd535bbb085713afd'
            '2f191059b619141ba883ae132af56460212c84eb208f087b87b79b0a3b9e4900'
            '18913873bf889f8b4d8bc2109d313fed02e523c86519ca96285640bf965732d5'
            'bd4bbd01a9d68e0217c3b48c977dda881fd956b53f981a6e32af0357d2e0b716'
            'bfaa2602d78f097c95e76d150423f83779384a737d41502bd8067b8f663b436f'
            '56e3cab181040101be05d4b7723825f7b0c082c34403e42c6f0934c6474a6a43')
noextract=()

# prepare() {
#   cd "$srcdir/$pkgname-$pkgver"
#   patch -p1 -i "$srcdir/$pkgname-$pkgver.patch"
# }

# build() {
#   cd "$srcdir/$pkgname-$pkgver"
#   ./configure --prefix=/usr
#   make
# }

# check() {
#   cd "$srcdir/$pkgname-$pkgver"
#   make -k check
# }

package() {
  # cd "$srcdir/$pkgname-$pkgver"
  # make DESTDIR="$pkgdir/" install
  install -D -t $pkgdir/usr/lib/systemd/system -m 644 \
          nextcloud-app-update-all.service \
          nextcloud-app-update-all.timer \
          nextcloud-cron.service \
          nextcloud-cron.timer \
          nextcloud-files-scan-all.service \
          nextcloud-files-scan-all.timer \
          nextcloud-preview-generate-all.service \
          nextcloud-preview-generate-all.timer \
          nextcloud-preview-pre-generate.service \
          nextcloud-preview-pre-generate.timer
}

# vim:set ts=2 sw=2 et:
