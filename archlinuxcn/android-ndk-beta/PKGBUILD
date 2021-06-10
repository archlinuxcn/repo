# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Contributor: Alexander F Rødseth <xyproto@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: frownlee <florez.brownlee@gmail.com>

pkgname=android-ndk-beta
_pkgname=${pkgname/-beta*/}
pkgver=r23_beta5
pkgrel=2
pkgdesc='Android C/C++ developer kit (beta)'
arch=('x86_64')
url='https://developer.android.com/ndk/'
license=('GPL' 'LGPL' 'custom')
options=('!strip' 'staticlibs')
backup=("etc/profile.d/$pkgname.sh")
install="$pkgname.install"
depends=('glibc' 'bash')
optdepends=(
  'ncurses5-compat-libs: for using gdb'
  'python2: various helper scripts'
  'python: various helper scripts'
)
source=("$pkgname-$pkgver.zip"::"https://dl.google.com/android/repository/${_pkgname}-${pkgver/_/-}-linux.zip"
        "$pkgname.sh")
# SHA1 sums is kept to follow upstream releases https://github.com/android-ndk/ndk/issues/673
sha1sums=('453ba0ca124e43337318f8a40d26cab114e7092c'
          'b0a3c3d4e148c1049f9c8b12f2632840630ea4db')
sha256sums=('93858626ac0ec0bdbd2e4723056cece0237ab2b358d83e2ae1f42c5bcfc72889'
            'a39422d48174302e1ee27f07031f20adc78224d12c17a5451129a88b47c901c1')

package() {
  install -Ddm755 "$pkgdir/opt"
  mv "$_pkgname-${pkgver/_/-}" "$pkgdir/opt/$pkgname"

  install -Dm644 $pkgname.sh -t "$pkgdir/etc/profile.d/"

  # XXX: not creating a symlink at /opt/android-sdk/ndk-bundle as the latter is already used by android-ndk
}
