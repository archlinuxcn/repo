# Maintainer:
# Contributor: Damien Guihal <dguihal@gmail.com>
# Contributor: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>

: ${CARGO_HOME:=$SRCDEST/cargo-home}
: ${_nodeversion:=18}

_pkgname="vdhcoapp"
pkgname="$_pkgname"
pkgver=2.0.20
pkgrel=2
pkgdesc="Companion application for Video DownloadHelper browser add-on"
url="https://github.com/aclap-dev/vdhcoapp"
license=('GPL-2.0-or-later')
arch=('x86_64')

_source_vdhcoapp() {
  makedepends=(
    'esbuild'
    'jq'
    'nvm' # AUR
    'yq'
  )

  options=('emptydirs' '!strip' '!debug')
  install="$_pkgname.install"

  _pkgsrc="$_pkgname-$pkgver"
  _pkgext="tar.gz"
  source=("$_pkgsrc.$_pkgext"::"$url/archive/v$pkgver.$_pkgext")
  sha256sums=('f39a17e0375b0b58cd7326fafe51de7e8b1f32a11b24583baa41f9e0b8c0ef68')
}

_source_filepicker() {
  depends+=(
    'gtk3'
  )
  makedepends+=(
    'cargo'
    'git'
  )

  _filepicker_url="https://github.com/paulrouget/static-filepicker"
  _filepicker_pkgsrc="vdhcoapp-filepicker"
  source+=("$_filepicker_pkgsrc"::"git+$_filepicker_url.git")
  sha256sums+=('SKIP')
}

_prepare_vdhcoapp() (
  cd "$_pkgsrc"
  mv -f app/* .

  # create config.json
  tomlq . ./config.toml \
    | jq '.target.os = "linux"' \
    | jq '.target.arch = "amd64"' \
    | jq ".meta.version = \"${pkgver}\"" \
      > src/config.json

  # fix path to config.json
  sed -E -i src/main.js src/native-autoinstall.js \
    -e 's&^(const config = require\('\'')(config.json'\''\);)$&\1./\2&'
)

_prepare_filepicker() (
  _cargo_env

  cd "$_filepicker_pkgsrc"
  cargo fetch --locked --target "$(rustc -vV | sed -n 's/host: //p')"
)

_build_vdhcoapp() (
  _nvm_env

  cd "$_pkgsrc"

  npm install --no-package-lock --no-audit --no-fund --prefer-offline
  npm install pkg --no-package-lock --no-audit --no-fund --prefer-offline

  local _esbuild_options=(
    src/main.js
    --target=esnext
    "--banner:js=const _importMetaUrl=require('url').pathToFileURL(__filename)"
    "--define:import.meta.url=_importMetaUrl"
    --format=cjs
    --bundle
    --platform=node
    --tree-shaking=true
    --alias:electron=electron2
    --outfile=bundled.js
  )

  esbuild "${_esbuild_options[@]}"

  local _pkg_options=(
    bundled.js
    --target "node$_nodeversion-linux-x64"
    --output vdhcoapp
  )

  ./node_modules/.bin/pkg "${_pkg_options[@]}"
)

_build_filepicker() (
  _cargo_env

  cd "$_filepicker_pkgsrc"
  cargo build --frozen --release --all-features
)

_package_vdhcoapp() (
  cd "$_pkgsrc"
  install -Dm755 vdhcoapp -t "$pkgdir/usr/bin/"

  install -dm755 "$pkgdir/usr/lib/mozilla/native-messaging-hosts/"
  install -dm755 "$pkgdir/etc/opt/chrome/native-messaging-hosts/"
  install -dm755 "$pkgdir/etc/chromium/native-messaging-hosts/"
  install -dm755 "$pkgdir/etc/opt/edge/native-messaging-hosts/"
)

_package_filepicker() (
  _cargo_env
  install -Dm755 "$_filepicker_pkgsrc/$CARGO_TARGET_DIR/release/filepicker" -t "$pkgdir/usr/bin/"
)

_cargo_env() {
  export CARGO_HOME
  export RUSTUP_TOOLCHAIN=stable
  export CARGO_TARGET_DIR=target
}

_nvm_env() {
  export HOME="$SRCDEST/node-home"
  export NVM_DIR="$SRCDEST/node-nvm"

  # set up nvm
  source /usr/share/nvm/init-nvm.sh || [[ $? != 1 ]]
  nvm install $_nodeversion
  nvm use $_nodeversion
}

_source_vdhcoapp
_source_filepicker

prepare() {
  _prepare_vdhcoapp
  _prepare_filepicker
}

build() {
  _build_vdhcoapp
  _build_filepicker
}

package() {
  depends+=('ffmpeg')

  _package_vdhcoapp
  _package_filepicker
}
