# Maintainer: Vlad M. <vlad@archlinux.net>
# COntributor: beatgammit

pkgname=servo-git
_pkgname=servo
pkgver=35547.a03708eeb9
pkgrel=1
pkgdesc="Parallel Browser Project: web browser written in Rust"
arch=('i686' 'x86_64')
url="https://github.com/servo/servo"
license=('MPL')
depends=('freetype2' 'mesa' 'libxrandr' 'libxi' 'libgl' 'glu' 'fontconfig' 'ttf-font' 'bzip2' 'libxcursor' 'libxmu' 'xcb-util' 'python-dbus' 'gst-plugins-bad')
install="$pkgname.install"
makedepends=('git' 'curl' 'python2' 'python2-virtualenv' 'gperf' 'depot-tools-git' 'cmake' 'rustup' 'clang' 'autoconf2.13')
provides=("$_pkgname")
conflicts=("$_pkgname")
_branch=servo
source=(
'git+https://github.com/servo/servo.git'
)
md5sums=('SKIP')

pkgver() {
  cd "$_branch"
  echo $(git rev-list --count HEAD).$(git rev-parse --short HEAD)
}

build() {
  cd "$_branch"
  
  # fixes build error
  # possibly _FORTIFY_SOURCE? https://bugs.archlinux.org/task/34759
  #unset CPPFLAGS

  ./mach build --dev
}

package() {
  servopath=$_branch/target/debug
  install -Dm755 "$servopath/servo" "$pkgdir/opt/servo/servo"

  mkdir -p "$pkgdir/usr/lib"

  find "$servopath/deps" -name "*-*.so" -exec basename {} \; | sort | uniq | while read _f; do
	  _file=$(find "$servopath/deps" -name "$_f" -print | head -n 1)
	  if [ -z "$_file" ]; then
		  echo "Skipping: $_f"
		  continue
	  fi
	  install -Dm644 "$_file" "$pkgdir/usr/lib"
  done

  mkdir -p "$pkgdir/opt/servo/resources"
  cp -r $_branch/resources/* "$pkgdir/opt/servo/resources"

  mkdir -p "$pkgdir/etc/profile.d" 
  echo 'export PATH=$PATH:/opt/servo' > "$pkgdir/etc/profile.d/${_pkgname}.sh"
  echo 'setenv PATH ${PATH}:/opt/servo' > "$pkgdir/etc/profile.d/${_pkgname}.csh"
  chmod 755 "$pkgdir/etc/profile.d/${_pkgname}".{csh,sh}
}
