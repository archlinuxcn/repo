# Maintainer: BlackEagle < ike DOT devolder AT gmail DOT com >

pkgname=vivaldi-ffmpeg-codecs
pkgver=62.0.3202.97
pkgrel=1
pkgdesc="additional support for proprietary codecs for vivaldi"
arch=('x86_64')
url="https://ffmpeg.org/"
license=('LGPL2.1')
depends=('glibc')
makedepends=(
  'gtk3' 'libexif' 'libxss' 'ninja' 'nss' 'pciutils' 'python2'
  'xdg-utils'
)
options=('!strip')
source=(
  "https://commondatastorage.googleapis.com/chromium-browser-official/chromium-$pkgver.tar.xz"
  'chromium-last-commit-position-r1.patch'
  'https://raw.githubusercontent.com/gentoo/gentoo/master/www-client/chromium/files/chromium-FORTIFY_SOURCE-r2.patch'
  'https://raw.githubusercontent.com/gentoo/gentoo/master/www-client/chromium/files/chromium-gn-bootstrap-r17.patch'
  'chromium-gcc5-r2.patch'
)
sha512sums=('2f8c7e9a17f25670bd3ceb557149185329d372873b75584f57486f26326d8c0fb7849807b46ace0be563a4aebf4a2be4ceeae4fe30cf5da7dcb1068ab1b7ebd1'
            '8f63366ca998e3ee06a79c6df5b4454707bd9865913ecde2f79fcb49fdd86d291f678b9f21807e4eb61d15497cdbe4a4bdc06637882e708f34f6804453bdfd41'
            '2d78092a700788c74b86db636af303fdb63a28ce5b7b0431dd81f6b7ce501e5d0234a6327a1b49bc23e1c1d00ba98fd5334dd07d9a20bb0d81d1a4ca4487a26c'
            '28812a8bd6d591831a3bbd749f1d7c6dd434eb0237970d4e8ea8cfd48fa8efb4d98906eca3d175218fe62c50bcb0b6472b2d7dfdde73d5641cd3fde1d9dc5f3b'
            '55723ffe9c34b5336450e75db8354c1ce5d6429b7296cbf575941eef5f3de3cdc40836e8f9b6905b4153913b10136a12d4c6d37f6a9f447677aa40588bfac182')

prepare() {
  cd "$srcdir/chromium-$pkgver"

  # Use Python 2
  find . -name '*.py' -exec sed -r 's|/usr/bin/python$|&2|g' -i {} +
  find . -name '*.py' -exec sed -r 's|/usr/bin/env python$|&2|g' -i {} +
  # There are still a lot of relative calls which need a workaround
  [[ -d "$srcdir/python2-path" ]] && rm -rf "$srcdir/python2-path"
  mkdir "$srcdir/python2-path"
  ln -s /usr/bin/python2 "$srcdir/python2-path/python"

  # chromium 46 gives an error about a missing file
  # workaround create empty
  touch chrome/test/data/webui/i18n_process_css_test.html

  patch -p1 -i "$srcdir/chromium-last-commit-position-r1.patch"
  patch -p1 -i "$srcdir/chromium-FORTIFY_SOURCE-r2.patch"
  patch -p1 -i "$srcdir/chromium-gn-bootstrap-r17.patch"
  patch -p1 -i "$srcdir/chromium-gcc5-r2.patch"
}

build() {
  cd "$srcdir/chromium-$pkgver"

  export PATH="$srcdir/python2-path:$PATH"

  local args="ffmpeg_branding=\"ChromeOS\" proprietary_codecs=true enable_hevc_demuxing=true use_gconf=false use_gio=false use_gnome_keyring=false use_pulseaudio=false link_pulseaudio=false use_kerberos=false use_cups=false use_sysroot=false use_gold=false use_allocator=\"none\" linux_use_bundled_binutils=false fatal_linker_warnings=false treat_warnings_as_errors=false enable_nacl=false enable_nacl_nonsfi=false is_clang=false clang_use_chrome_plugins=false is_component_build=true is_debug=false symbol_level=0 use_custom_libcxx=false"

  python2 tools/gn/bootstrap/bootstrap.py -v -s
  out/Release/gn gen out/Release -v --args="$args" --script-executable=/usr/bin/python2

  ninja -C out/Release -v media/ffmpeg
}

package() {
  cd "$srcdir/chromium-$pkgver"

	install -Dm644 out/Release/libffmpeg.so \
    "$pkgdir/opt/vivaldi/libffmpeg.so"
}

# vim:set ts=2 sw=2 et:
