# Maintainer: Torge Matthies <openglfreak at googlemail dot com>

pkgbase=deepfilternet-git
pkgname=(libdf-git libdeep_filter_ladspa-git deepfilternet-demos-git)
pkgver=v0.5.6.r89.gd375b2d
pkgrel=2
pkgdesc='A Low Complexity Speech Enhancement Framework for Full-Band Audio (48kHz) using Deep Filtering (Git version)'
url='https://github.com/Rikorose/DeepFilterNet'
arch=('x86_64')
license=('MIT' 'Apache')
depends=('gcc-libs' 'alsa-lib')
makedepends=('cargo' 'git')
_repo=DeepFilterNet
source=('git+https://github.com/Rikorose/DeepFilterNet.git')
sha512sums=('SKIP')

if check_option "lto" "y"; then
  export CARGO_PROFILE_RELEASE_LTO=true CARGO_PROFILE_RELEASE_CODEGEN_UNITS=1
fi
if check_option "debug" "y"; then
  export CARGO_PROFILE_RELEASE_DEBUG=2
fi

pkgver() {
  cd "$_repo"
  git describe --long --tags --abbrev=7 | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd "$_repo"
  export RUSTUP_TOOLCHAIN=nightly
  # --locked cannot be used, as the lockfile isn't up to date
  cargo fetch --target "$(rustc -vV | sed -n 's/host: //p')"
}

build() {
  cd "$_repo"
  export RUSTUP_TOOLCHAIN=nightly
  export CARGO_TARGET_DIR=target
  cargo build --profile=release-lto --frozen \
    -p deep-filter-ladspa -p deep_filter -p df-demo \
    --features df-demo/ui \
    --bin df-demo \
    --lib
}

# tests don't compile

package_libdf-git() {
  pkgdesc+=" - core library"
  depends=('gcc-libs')
  conflicts+=('libdf')
  provides+=('libdf')
  cd "$_repo"
  install -Dm0755 -t "$pkgdir/usr/lib/" "target/release-lto/libdf.so"
  install -Dm0644 -t "$pkgdir/usr/share/licenses/${pkgname}/" "LICENSE" "LICENSE-MIT"
}

package_libdeep_filter_ladspa-git() {
  pkgdesc+=" - ladspa plugin"
  depends=('gcc-libs')
  conflicts+=('libdeep_filter_ladspa')
  provides+=('libdeep_filter_ladspa')
  cd "$_repo"
  install -Dm0755 -t "$pkgdir/usr/lib/ladspa/" "target/release-lto/libdeep_filter_ladspa.so"
  install -Dm0644 -t "$pkgdir/usr/share/licenses/${pkgname}/" "LICENSE" "LICENSE-MIT"
}

package_deepfilternet-demos-git() {
  pkgdesc+=" - demo application"
  depends=('gcc-libs' 'alsa-lib')
  conflicts+=('deepfilternet-demos')
  provides+=('deepfilternet-demos')
  cd "$_repo"
  install -Dm0755 -t "$pkgdir/usr/bin/" "target/release-lto/df-demo"
  install -Dm0644 -t "$pkgdir/usr/share/licenses/${pkgname}/" "LICENSE" "LICENSE-MIT"
}
