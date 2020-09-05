# Maintainer: Stefan Tatschner <stefan@rumpelsepp.org>

pkgname=gron
pkgver=0.6.0
pkgrel=1
pkgdesc='Makes JSON greppable'
arch=('x86_64')
url="https://github.com/tomnomnom/gron"
license=('MIT')
makedepends=('go')
source=("https://github.com/tomnomnom/gron/archive/v$pkgver.tar.gz"
        "1616a25e4b7f3364c4c291e467ecf75755a3a2bf.patch"
        "57a0165fce6b1295fc389807dfa37a6c6c28ed41.patch")
sha256sums=('fe75b1b4922b591723f48cb9cd2c31cb60bb3ab9f8d0398df75a08b781d8591c'
            'efe2ce756b192473615613fd17a3d83a71eba73c1e3a1355f8abaec6784aa34a'
            'c8c8c66b9eb437c3e59d0d5fbc0a933c98216a3a66f895778d3b639ebcadcd5c')

# NOTE:
# The author seems to be temporarly inactive due to burnout recovery.
# I decided to include two patches which are in master and are worth it.
#  1) add fish command line completions
#  2) add go modules for easier builds
# I will remove them once a new release is available.

prepare() {
  cd $pkgname-$pkgver
  # fish completions
  patch --forward --strip=1 --input="${srcdir}/1616a25e4b7f3364c4c291e467ecf75755a3a2bf.patch"
  # go modules
  patch --forward --strip=1 --input="${srcdir}/57a0165fce6b1295fc389807dfa37a6c6c28ed41.patch"
}

check() {
  cd $pkgname-$pkgver
  go test .
}

build() {
  cd $pkgname-$pkgver
  go build \
    -gcflags "all=-trimpath=$PWD" \
    -asmflags "all=-trimpath=$PWD" \
    -ldflags "-extldflags $LDFLAGS" \
    -o $pkgname .
}

package() {
  cd $pkgname-$pkgver
  install -Dm755 $pkgname "$pkgdir"/usr/bin/$pkgname
  install -Dm644 completions/gron.fish "$pkgdir"/usr/share/fish/vendor_completions.d/gron.fish
}
