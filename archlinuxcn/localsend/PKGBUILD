# Maintainer:
# Contributor: Patrick Northon <northon_patrick3@yahoo.ca>

: ${CARGO_HOME:=$SRCDEST/cargo-home}
: ${CARGO_TARGET_DIR:=target}
: ${RUSTUP_TOOLCHAIN:=stable}
export CARGO_HOME CARGO_TARGET_DIR RUSTUP_TOOLCHAIN

: ${FVM_CACHE_PATH:=$SRCDEST/fvm-cache}
export FVM_CACHE_PATH

: ${_use_sodeps:=false}

: ${_install_path:=usr/lib}

_pkgname="localsend"
pkgname="$_pkgname"
pkgver=1.18.2
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
  'cargo'
  'clang'
  'cmake'
  'fvm'
  'git'
  'lld'
  'llvm'
  'ninja'
  'patchelf'
)

options=('!lto')

_pkgsrc="$_pkgname-$pkgver"
_pkgext="tar.gz"
source=("$_pkgsrc.$_pkgext"::"$url/archive/refs/tags/v$pkgver.$_pkgext")
sha256sums=('4425dfcf2e016d6540ea44941deb4ba6568201cc47d7f08753606e6e4b2769cd')

_rust_setup() {
  if [ -n "$_arch" ]; then
    return
  fi

  # bypass Cargokit rustup requirement to use system toolchain
  if ! pacman -Qs rustup &> /dev/null; then
    install -Dm755 /dev/stdin fakebin/rustup << END
#!/usr/bin/env true
END
  fi

  if [ -e "$srcdir/fakebin" ]; then
    export PATH="$srcdir/fakebin:$PATH"
  fi

  _arch="x64"
  if [[ "${CARCH::1}" == "a" ]]; then
    _arch="arm64"
  fi

  local _units=$(($(nproc) > 16 ? $(nproc) : 16))
  export CARGO_PROFILE_RELEASE_LTO=false
  export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=$_units
}

prepare() {
  _rust_setup

  cd "$_pkgsrc"
  cargo fetch --locked --target host-tuple
}

build() {
  _rust_setup

  export CXXFLAGS+=' -Wno-error=deprecated-declarations'

  cd "$_pkgsrc"
  cargo build --frozen --release --all-features

  # copy isolate for flutter to find
  local _isolates="app/build/linux/$_arch/release/plugins/rust_lib_localsend_app"
  mkdir -p "$_isolates"
  cp "$srcdir/$_pkgsrc/$CARGO_TARGET_DIR/release/librust_lib_localsend_app.so" "$_isolates/"

  cd "app"
  fvm install

  fvm flutter --disable-analytics
  #fvm flutter pub upgrade --major-versions
  fvm flutter --no-version-check pub get
  fvm flutter build linux --no-pub --release
}

package() {
  _rust_setup

  if [[ "${_use_sodeps::1}" == "t" ]]; then
    eval "depends+=(
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

  # cli, server
  install -Dm755 "$_pkgsrc/$CARGO_TARGET_DIR/release"/{localsend-cli,server} -t "$pkgdir/$_install_path/$_pkgname/"

  # app, lib, data
  cd "$_pkgsrc/app/build/linux/$_arch/release/bundle"
  install -Dm755 "localsend_app" -t "$pkgdir/$_install_path/$_pkgname"
  cp -r lib/ "$pkgdir/$_install_path/$_pkgname/"
  cp -r data/ "$pkgdir/$_install_path/$_pkgname/"

  # runpath
  for i in "$pkgdir/$_install_path/$_pkgname"{,/lib}/*; do
    if [ -f "$i" ] && readelf -h "$i" &> /dev/null; then
      if [[ "$i" =~ /lib/[^/]+$ ]]; then
        printf 'Setting rpath to $ORIGIN for %s ...\n' "${i##*/}"
        patchelf --set-rpath '$ORIGIN' "$i"
      else
        printf 'Setting rpath to $ORIGIN/lib for %s ...\n' "${i##*/}"
        patchelf --set-rpath '$ORIGIN/lib' "$i"
      fi
    fi
  done

  # symlink
  mkdir -pm755 "${pkgdir}/usr/bin"
  ln -sfr "$pkgdir/$_install_path/$_pkgname/${_pkgname}_app" "$pkgdir/usr/bin/${_pkgname}"
  ln -sfr "$pkgdir/$_install_path/$_pkgname/${_pkgname}-cli" "$pkgdir/usr/bin/${_pkgname}-cli"

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
