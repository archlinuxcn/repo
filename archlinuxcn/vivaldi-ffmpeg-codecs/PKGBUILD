# Maintainer: BlackEagle < ike DOT devolder AT gmail DOT com >

pkgname=vivaldi-ffmpeg-codecs
pkgver=73.0.3683.88
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
source=(
  "https://commondatastorage.googleapis.com/chromium-browser-official/chromium-$pkgver.tar.xz"
  'chromium-73-gcc-0.patch'
  'chromium-73-gcc-2.patch'
  'chromium-73-gcc-3.patch'
)
sha512sums=('db4d20ef618171e1672e77ac04159ccde7bc425f19faf0a61de883380a1f75baa2bdfe9241f4467022d25635d9ed7444543b9e90a32c4efe9c81b9f3858d189a'
            'de7101ba00d8c1f00cd3f557574653cb9df80e59efe869c4fb127736b0f0793b20157169af74c8e38057c460e29a7e90e05274c749dbb6a30aa0aa7886b74b36'
            'a242e7669d9c4b86f39dfe0516bced6b234336f4671514b1eca647b3d82228602dda96c69370326eacb3f68b5a47d58a2d6e4f5d97ea67583caf0c2b4430f0d4'
            '93173033df16138b94dda215b088dd63937f738536d6cbcc4133258502e1f5bdda45bcbbd95250bc7f781839544c3d45e2dfa8aa4477a0617cfaa723e9140085')

prepare() {
  cd "$srcdir/chromium-$pkgver"

  # Use Python 2
  find -name '*.py' | xargs sed -e 's|env python|&2|g' -e 's|bin/python|&2|g' -i

  # force some 'older' binaries in the path
  [[ -d "$srcdir/path" ]] && rm -rf "$srcdir/path"
  mkdir "$srcdir/path"
  ln -s /usr/bin/python2 "$srcdir/path/python"

  patch -p1 -i "$srcdir/chromium-73-gcc-0.patch"
  patch -p1 -i "$srcdir/chromium-73-gcc-2.patch"
  patch -p1 -i "$srcdir/chromium-73-gcc-3.patch"
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
