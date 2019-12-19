# vim:set ft=sh:
# Maintainer: BlackEagle < ike DOT devolder AT gmail DOT com >

pkgname=vivaldi-ffmpeg-codecs
pkgver=79.0.3945.93
_vivaldi_major_version=2.10
pkgrel=1
pkgdesc="additional support for proprietary codecs for vivaldi"
arch=('x86_64')
url="https://ffmpeg.org/"
license=('LGPL2.1')
depends=('glibc')
makedepends=(
  'gtk3' 'libexif' 'libxss' 'ninja' 'nss' 'pciutils' 'python2'
  'xdg-utils' 'gn'
)
options=('!strip')
source=(
  "https://commondatastorage.googleapis.com/chromium-browser-official/chromium-$pkgver.tar.xz"
)
sha512sums=('b94f9890ae82e43d1b0d2abd99e3cde80a4481731ecd64ee23cd5d2d100cf667c4747f2d30e163a102363f130b097c612032189166515793f4e556792f2ce8c6')

prepare() {
  cd "$srcdir/chromium-$pkgver"

  # Use Python 2
  find -name '*.py' | xargs sed -e 's|env python|&2|g' -e 's|bin/python|&2|g' -i

  # force some 'older' binaries in the path
  [[ -d "$srcdir/path" ]] && rm -rf "$srcdir/path"
  mkdir "$srcdir/path"
  ln -s /usr/bin/python2 "$srcdir/path/python"

}

build() {
  cd "$srcdir/chromium-$pkgver"

  python2 tools/clang/scripts/update.py

  export PATH="${srcdir}/chromium-${pkgver}/third_party/llvm-build/Release+Asserts/bin:$srcdir/path:$PATH"

  export CC="clang"
  export CXX="clang++"

  local args="ffmpeg_branding=\"ChromeOS\" proprietary_codecs=true enable_platform_hevc=true enable_platform_ac3_eac3_audio=true enable_platform_mpeg_h_audio=true enable_platform_dolby_vision=true enable_mse_mpeg2ts_stream_parser=true use_gnome_keyring=false use_sysroot=false use_gold=false linux_use_bundled_binutils=false treat_warnings_as_errors=false enable_nacl=false enable_nacl_nonsfi=false clang_use_chrome_plugins=true is_component_build=true is_debug=false symbol_level=0 use_custom_libcxx=true"

  gn gen out/Release -v --args="$args" --script-executable=/usr/bin/python2

  ninja -C out/Release -v media/ffmpeg
}

package() {
  cd "$srcdir/chromium-$pkgver"

	install -Dm644 out/Release/libffmpeg.so \
    "$pkgdir/opt/vivaldi/libffmpeg.so.$_vivaldi_major_version"
}

# vim:set ts=2 sw=2 et:
