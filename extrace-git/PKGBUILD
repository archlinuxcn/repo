# Maintainer: aksr <aksr at t-com dot me>
pkgname=extrace-git
pkgver=0.5.r2.g2b7b03c
pkgrel=1
epoch=
pkgdesc="Trace exec() calls system-wide."
arch=('i686' 'x86_64')
url="https://github.com/chneukirchen/extrace"
license=('custom')
groups=()
depends=()
makedepends=('git')
optdepends=()
checkdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
changelog=
install=
source=("$pkgname::git+https://github.com/chneukirchen/extrace")
noextract=()
md5sums=('SKIP')

pkgver() {
  cd "$srcdir/$pkgname"
  git describe --long | sed -E 's/^v//g;s/([^-]*-g)/r\1/;s/-/./g'
}

build() {
  cd "$srcdir/$pkgname"
  make
}

package() {
  cd "$srcdir/$pkgname"
  install -Dm755 extrace $pkgdir/usr/bin/extrace
  install -m755 pwait $pkgdir/usr/bin/pwait
  install -Dm644 extrace.1 $pkgdir/usr/share/man/man1/extrace.1
  install -Dm644 pwait.1 $pkgdir/usr/share/man/man1/pwait.1
  mkdir -p $pkgdir/usr/share/licenses/$pkgname/
  sed '16,49!d' extrace.c > $pkgdir/usr/share/licenses/$pkgname/LICENSE.extrace
  sed '10,46!d' pwait.c > $pkgdir/usr/share/licenses/$pkgname/LICENSE.pwait
}

