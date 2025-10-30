# Maintainer:
# Contributor: The one with the braid <info@braid.business>

: ${FVM_CACHE_PATH:=$SRCDEST/fvm-cache}
: ${RUSTUP_TOOLCHAIN:=nightly}
export FVM_CACHE_PATH RUSTUP_TOOLCHAIN

_pkgname="fluffychat"
pkgname="$_pkgname"
pkgver=2.2.0
pkgrel=1
pkgdesc="The cutest instant messenger in the [matrix]"
url="https://github.com/krille-chan/fluffychat"
license=('AGPL-3.0-only')
arch=('x86_64' 'aarch64')

depends=(
  'gtk3'
  'libsecret'     # flutter_secure_storage
  'xdg-user-dirs' # path_provider
  'openssl'       # sqlite encryption
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
optdepends=(
  'zenity: for flutter_file_picker'
  'kdialog: for flutter_file_picker'
)

options=('!lto' '!strip' '!debug')

_pkgsrc="$_pkgname-$pkgver"
_pkgext="tar.gz"
source=(
  "$_pkgsrc.$_pkgext"::"$url/archive/refs/tags/v$pkgver.$_pkgext"
  '0000-fix-wayland-gtk-csd.patch'
)
sha256sums=(
  '7efc395a198d006dbf768163e0812e22d8cbf708ed8eb57448c20e308e9b7056'
  '04a373c2c25a9be1617ab1ccb19da48ae379ff392bb59a3938bcdec00ab82230'
)

prepare() (
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    src="${src%.zst}"
    if [[ $src == *.patch ]]; then
      printf '\n\nApplying patch: %s\n' "$src"
      patch -d "$_pkgsrc" -Np1 -F100 -i "${srcdir:?}/$src"
    fi
  done
)

build() {
  # fix incompatible flags on ARM
  if [ "${CARCH::1}" != "x" ]; then
    export CFLAGS CXXFLAGS
    local i _unwanted

    _unwanted=(
      -fstack-protector-strong
      -fstack-clash-protection
    )

    for i in "${_unwanted[@]}"; do
      CFLAGS=$(sed -E -e "s&${i}&&g" -e 's&\s+& &g' <<< "$CFLAGS")
      CXXFLAGS=$(sed -E -e "s&${i}&&g" -e 's&\s+& &g' <<< "$CXXFLAGS")
    done
  fi

  cd "$_pkgsrc"

  : ${_fvm_version=$(grep -Pom1 '(?<=FLUTTER_VERSION=)[0-9\.]+' ".github/workflows/versions.env")}

  fvm install "$_fvm_version"
  fvm use "$_fvm_version" --force

  fvm flutter --disable-analytics
  #fvm flutter pub upgrade --major-versions
  fvm flutter pub get
  fvm flutter build linux --no-pub --release
}

package() {
  pushd "$_pkgsrc"/build/linux/*/release
  cmake -DCMAKE_INSTALL_PREFIX="/usr/lib/$_pkgname" .
  DESTDIR="$pkgdir" cmake -P cmake_install.cmake
  popd

  # rpath
  patchelf --set-rpath '$ORIGIN' "$pkgdir/usr/lib/$_pkgname/lib"/*.so

  # symlink
  install -dm755 "$pkgdir/usr/bin"
  ln -s "/usr/lib/$_pkgname/$_pkgname" "$pkgdir/usr/bin/$_pkgname"

  # license
  install -Dm644 "$_pkgsrc/LICENSE" -t "$pkgdir/usr/share/licenses/$pkgname/"

  # icon
  install -Dm644 "$_pkgsrc/assets/favicon.png" "$pkgdir/usr/share/pixmaps/$_pkgname.png"

  # launcher
  install -Dm644 /dev/stdin "$pkgdir/usr/share/applications/$_pkgname.desktop" << END
[Desktop Entry]
Type=Application
Name=FluffyChat
Comment=$pkgdesc
Exec=$_pkgname
Icon=$_pkgname
SingleMainWindow=true
StartupWMClass=chat.fluffy.fluffychat
Terminal=false
StartupNotify=false
Categories=Network;InstantMessaging;Chat;MatrixClient
X-Purism-FormFactor=Workstation;Mobile;
END
}
