# Maintainer:
# Contributor: Patrick Northon <northon_patrick3@yahoo.ca>

## links
# https://localsend.org/
# https://github.com/localsend/localsend

## options
: ${_install_path:=usr/lib}

# basic info
_pkgname="localsend"
pkgname="$_pkgname"
pkgver=1.16.1
pkgrel=1
pkgdesc="An open source cross-platform alternative to AirDrop"
url="https://github.com/localsend/localsend"
license=('MIT')
arch=('x86_64')

depends=(
  'libayatana-appindicator'
)
makedepends=(
  'clang'
  'cmake'
  'fvm' # AUR
  'git'
  'lld'
  'llvm'
  'ninja'
  'patchelf'
  'rustup'
)

options=('!lto')

_pkgsrc="$_pkgname-$pkgver"
_pkgext="tar.gz"
source=("$_pkgsrc.$_pkgext"::"$url/archive/refs/tags/v$pkgver.$_pkgext")
sha256sums=('c47a702c58e7d526511a18fb95935ab55daa62c7391f5bd2d573dab00937eeb9')

build() {
  export FVM_CACHE_PATH="$SRCDEST/fvm-cache"

  cd "$_pkgsrc/app"
  fvm install

  fvm flutter --disable-analytics
  #fvm flutter pub upgrade --major-versions
  fvm flutter --no-version-check pub get
  fvm flutter build linux --no-pub --release
}

package() {
  cd "$_pkgsrc/app/build/linux/x64/release/bundle"

  # files
  install -Dm755 "localsend_app" "$pkgdir/$_install_path/$_pkgname/$_pkgname"
  cp --reflink=auto -r lib/ "$pkgdir/$_install_path/$_pkgname/"
  cp --reflink=auto -r data/ "$pkgdir/$_install_path/$_pkgname/"

  # runpath
  patchelf --set-rpath '$ORIGIN/lib' "$pkgdir/$_install_path/$_pkgname/$_pkgname"
  for i in "$pkgdir/$_install_path/$_pkgname/lib"/*.so; do
    [ -z "$(patchelf --print-rpath "$i")" ] && continue
    patchelf --set-rpath '$ORIGIN' "$i"
  done

  # symlink
  install -dm755 "${pkgdir}/usr/bin"
  ln -sfr "$pkgdir/$_install_path/$_pkgname/$_pkgname" "$pkgdir/usr/bin/${_pkgname}"

  # icon
  install -Dm644 "$srcdir/$_pkgsrc/app/build/flutter_assets/assets/img/logo-512.png" "$pkgdir/usr/share/pixmaps/$_pkgname.png"

  # launcher
  install -Dm644 /dev/stdin "$pkgdir/usr/share/applications/$_pkgname.desktop" << END
[Desktop Entry]
Type=Application
Name=LocalSend
Comment=$pkgdesc
Exec=$_pkgname
Icon=$_pkgname
Terminal=false
Categories=Utility;Network;
END

  # license
  install -Dm644 "$srcdir/$_pkgsrc/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname/"

  # permissions
  chmod -R u+rwX,go+rX,go-w "$pkgdir/"
}
