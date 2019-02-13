# Maintainer: BlackEagle < ike DOT devolder AT gmail DOT com >

pkgname=vivaldi-ffmpeg-codecs
pkgver=71.0.3578.98
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
sha512sums=('dbeb90e16c6c05422c1f43e8fe747d60dab49c1fffdd0f33824ca24429f3871bda649eb1e6402470d3d9bb701e47d55d2fff4f46530e3f43e72f516d1837aad6')

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

  #python2 tools/clang/scripts/update.py --without-android

  #export PATH="${srcdir}/chromium-${pkgver}/third_party/llvm-build/Release+Asserts/bin:$srcdir/path:$PATH"

  #export CC="clang"
  #export CXX="clang++"

  local args="ffmpeg_branding=\"ChromeOS\" proprietary_codecs=true enable_hevc_demuxing=true enable_ac3_eac3_audio_demuxing=true use_gnome_keyring=false use_sysroot=false use_gold=false use_allocator=\"none\" linux_use_bundled_binutils=false fatal_linker_warnings=false treat_warnings_as_errors=false enable_nacl=false enable_nacl_nonsfi=false is_clang=false clang_use_chrome_plugins=false is_component_build=true is_debug=false symbol_level=0 use_custom_libcxx=false use_lld=false use_jumbo_build=false"

  #(
    #cd third_party/ffmpeg
    #chromium/scripts/build_ffmpeg.py linux x64 --branding ChromeOS
    #chromium/scripts/copy_config.sh
    #chromium/scripts/generate_gn.py
  #)

  gn gen out/Release -v --args="$args" --script-executable=/usr/bin/python2

  ninja -C out/Release -v media/ffmpeg
}

package() {
  cd "$srcdir/chromium-$pkgver"

	install -Dm644 out/Release/libffmpeg.so \
    "$pkgdir/opt/vivaldi/libffmpeg.so"
}

# vim:set ts=2 sw=2 et:
