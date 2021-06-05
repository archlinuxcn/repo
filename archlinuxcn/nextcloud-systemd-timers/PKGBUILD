# Maintainer: Dominik Schrempf <dominik.schrempf@gmail.com>
pkgname=nextcloud-systemd-timers
pkgver=0.11.0
pkgrel=2
epoch=
pkgdesc="Systemd services and timers for Nextcloud background jobs (see Nextcloud Arch Wiki entry)."
arch=('any')
url=""
license=('GPL')
groups=()
depends=()
makedepends=()
checkdepends=()
optdepends=('nextcloud-app-previewgenerator: pre-generation of previews')
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=nextcloud-systemd-timers.install
changelog=
source=("nextcloud-app-update-all.service"
        "nextcloud-app-update-all.timer"
        "nextcloud-files-scan-all.service"
        "nextcloud-files-scan-all.timer"
        "nextcloud-preview-generate-all.service"
        "nextcloud-preview-generate-all.timer"
        "nextcloud-preview-pre-generate.service"
        "nextcloud-preview-pre-generate.timer")
sha256sums=('0706490da2a72647c2d98d52001004ab79b1747eeab330e7653f1e06ab5408dd'
            '39039f1a3dc23022fccc991daca86d77e7d41be275566f6892cd6b290fa0da4a'
            '88beeaaad1a05911314fbc6e7db8d316f7ec6d42df107fcd3b1c52cf291f1333'
            '2f191059b619141ba883ae132af56460212c84eb208f087b87b79b0a3b9e4900'
            '4713096a56800abde60380cbf80a45bb60fd83a12dec9ffc93c52283f06fb597'
            'bd4bbd01a9d68e0217c3b48c977dda881fd956b53f981a6e32af0357d2e0b716'
            '7bc2cb4ae0073bcbb42d86f4e2ce92ca81623dc0ea4b8a631baf0ab4338e8937'
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
          nextcloud-files-scan-all.service \
          nextcloud-files-scan-all.timer \
          nextcloud-preview-generate-all.service \
          nextcloud-preview-generate-all.timer \
          nextcloud-preview-pre-generate.service \
          nextcloud-preview-pre-generate.timer
}

# vim:set ts=2 sw=2 et:
