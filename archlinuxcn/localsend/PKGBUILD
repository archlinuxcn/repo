# Maintainer:
# Contributor: Patrick Northon <northon_patrick3@yahoo.ca>

: ${_use_sodeps:=false}

: ${_install_path:=usr/lib}

_pkgname="localsend"
pkgname="$_pkgname"
pkgver=1.18.1
pkgrel=1
pkgdesc="An open source cross-platform alternative to AirDrop"
url="https://github.com/localsend/localsend"
license=('Apache-2.0')
arch=('x86_64' 'aarch64')

depends=(
  'at-spi2-core'
  'cairo'
  'fontconfig'
  'gdk-pixbuf2'
  'glib2'
  'gtk3'
  'hicolor-icon-theme'
  'libayatana-appindicator'
  'libepoxy'
  'pango'
)
makedepends=(
  'clang'
  'cmake'
  'fvm'
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
sha256sums=('555a73c39e2cfc01ee8cf0033ae11610725829d8289aa9c4794446241d9de2b0')

prepare() {
  sed -E 's&^(channel) = .*$&\1 = "stable"&' -i "$_pkgsrc/packages/localsend_isolates/rust-toolchain.toml"
}

build() (
  local _units=$(($(nproc) > 16 ? $(nproc) : 16))
  export CARGO_PROFILE_RELEASE_LTO=false
  export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=$_units

  export FVM_CACHE_PATH="$SRCDEST/fvm-cache"

  export CXXFLAGS+=' -Wno-error=deprecated-declarations'

  cd "$_pkgsrc/app"
  fvm install

  fvm flutter --disable-analytics
  #fvm flutter pub upgrade --major-versions
  fvm flutter --no-version-check pub get
  fvm flutter build linux --no-pub --release
)

package() {
  if [[ "${_use_sodeps::1}" == "t" ]]; then
    eval "depends=(
      libatk-1.0.so
      libcairo.so
      libepoxy.so
      libfontconfig.so
      libgdk-3.so
      libgdk_pixbuf-2.0.so
      libgio-2.0.so
      libglib-2.0.so
      libgobject-2.0.so
      libgtk-3.so
      libpango-1.0.so
      libpangocairo-1.0.so
    )"
  fi

  local _arch="x64"
  if [[ "${CARCH::1}" == "a" ]]; then
    _arch="arm64"
  fi

  cd "$_pkgsrc/app/build/linux/$_arch/release/bundle"

  # files
  install -Dm755 "localsend_app" "$pkgdir/$_install_path/$_pkgname/$_pkgname"
  cp -r lib/ "$pkgdir/$_install_path/$_pkgname/"
  cp -r data/ "$pkgdir/$_install_path/$_pkgname/"

  # runpath
  patchelf --set-rpath '$ORIGIN/lib' "$pkgdir/$_install_path/$_pkgname/$_pkgname"
  for i in "$pkgdir/$_install_path/$_pkgname/lib"/*.so; do
    [ -z "$(patchelf --print-rpath "$i")" ] && continue
    patchelf --set-rpath '$ORIGIN' "$i"
  done

  # symlink
  mkdir -pm755 "${pkgdir}/usr/bin"
  ln -sfr "$pkgdir/$_install_path/$_pkgname/$_pkgname" "$pkgdir/usr/bin/${_pkgname}"

  # icon
  install -Dm644 "$srcdir/$_pkgsrc/app/build/flutter_assets/assets/img/logo-512.png" "$pkgdir/usr/share/icons/hicolor/512x512/apps/$_pkgname.png"

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
