# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>
# Contributor: Alexander F Rødseth <xyproto@archlinux.org>
# Contributor: Daniel Micay <danielmicay@gmail.com>
# Contributor: frownlee <florez.brownlee@gmail.com>

pkgname=android-ndk-beta
_pkgname=${pkgname/-beta*/}
pkgver=r23_beta3
pkgrel=1
pkgdesc='Android C/C++ developer kit (beta)'
arch=('x86_64')
url='https://developer.android.com/ndk/'
license=('GPL' 'LGPL' 'custom')
options=('!strip' 'staticlibs')
backup=("etc/profile.d/$pkgname.sh")
install="$pkgname.install"
depends=('glibc')
optdepends=(
  'ncurses5-compat-libs: for using gdb'
  'python2: various helper scripts'
  'python: various helper scripts'
)
source=("$pkgname.sh")
source_x86_64=("$pkgname-$pkgver.zip"::"https://dl.google.com/android/repository/${_pkgname}-${pkgver/_/-}-linux-x86_64.zip")
# SHA1 sums is kept to follow upstream releases https://github.com/android-ndk/ndk/issues/673
sha1sums=('b0a3c3d4e148c1049f9c8b12f2632840630ea4db')
sha1sums_x86_64=('2298465ef13dab0c527b9cf6ef892b1ec6461fb4')
sha256sums=('a39422d48174302e1ee27f07031f20adc78224d12c17a5451129a88b47c901c1')
sha256sums_x86_64=('02950d40b7d6623a5af398a28689c15a789d88b1b190e6381ccece209f109236')

package() {
  install -Ddm755 "$pkgdir/opt"
  mv "$_pkgname-${pkgver/_/-}" "$pkgdir/opt/$pkgname"

  install -Dm644 $pkgname.sh -t "$pkgdir/etc/profile.d/"

  # XXX: not creating a symlink at /opt/android-sdk/ndk-bundle as the latter is already used by android-ndk
}
