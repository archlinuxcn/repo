# Maintainer:
# Contributor: The one with the braid <info@braid.business>

## links
# https://fluffychat.im/
# https://github.com/krille-chan/fluffychat

: ${_fvm_version=}

: ${FVM_CACHE_PATH:=$SRCDEST/fvm-cache}
: ${RUSTUP_TOOLCHAIN:=nightly}
export FVM_CACHE_PATH RUSTUP_TOOLCHAIN

_pkgname="fluffychat"
pkgname="$_pkgname"
pkgver=2.1.0
pkgrel=1
pkgdesc="The cutest instant messenger in the [matrix]"
url="https://github.com/krille-chan/fluffychat"
license=('AGPL-3.0-only')
arch=('x86_64' 'aarch64')

depends=(
  'gtk3'
  'libsecret'     # flutter_secure_storage
  'xdg-user-dirs' # path_provider
  'libolm'        # for e2ee
  'openssl'       # sqlite encryption
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
  '1afa88205a8ed1424330dbaeae5d087848c038b61ba739b0c43eb7d5bec4cd78'
  '0699d9eca413975cf8c99fcc906092cb4f546c9be139b6fcb3995e607eac1763'
)

prepare() {
  cd "$_pkgsrc"
  local src
  for src in "${source[@]}"; do
    src="${src%%::*}"
    src="${src##*/}"
    src="${src%.zst}"
    if [[ $src == *.patch ]]; then
      printf '\n\nApplying patch: %s\n' "$src"
      patch -Np1 -F100 -i "${srcdir:?}/$src"
    fi
  done
}

build() {
  # fix incompatible C(XX)FLAGS on Arch Linux on ARM
  if [ "${CARCH::1}" != "x" ]; then
    local i _cflags _cxxflags _unwanted
    _cflags=(${CFLAGS})
    _cxxflags=(${CXXFLAGS})

    _unwanted=(
      -fstack-protector-strong
      -fstack-clash-protection
    )

    for i in ${_unwanted[@]}; do
      _cflags=(${_cflags[@]//$i/})
      _cxxflags=(${_cxxflags[@]//$i/})
    done

    CFLAGS="${_cflags[@]}"
    CXXFLAGS="${_cxxflags[@]}"
  fi

  : ${_fvm_version:=$(grep -Pom1 '(?<=FLUTTER_VERSION=)[0-9\.]+' "$_pkgsrc/.github/workflows/versions.env")}

  cd "$_pkgsrc"
  fvm install $_fvm_version
  fvm global $_fvm_version

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

  # reset rpath
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
