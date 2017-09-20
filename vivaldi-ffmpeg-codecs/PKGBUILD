# Maintainer: BlackEagle < ike DOT devolder AT gmail DOT com >

pkgname=vivaldi-ffmpeg-codecs
pkgver=61.0.3163.91
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
  'https://raw.githubusercontent.com/gentoo/gentoo/master/www-client/chromium/files/chromium-gcc-r1.patch'
  'https://raw.githubusercontent.com/gentoo/gentoo/master/www-client/chromium/files/chromium-gn-bootstrap-r14.patch'
  'https://raw.githubusercontent.com/gentoo/gentoo/master/www-client/chromium/files/chromium-gcc5-r1.patch'
)
sha512sums=('f770d005c52e65bb137f340aaf58c564e120a867425e8fe3e3f4b7f328cfbb49efdc87d421e3c1ac4c7f74424421aa3d448fac59a33a7e6a789e29ed8bef03dc'
            '8f63366ca998e3ee06a79c6df5b4454707bd9865913ecde2f79fcb49fdd86d291f678b9f21807e4eb61d15497cdbe4a4bdc06637882e708f34f6804453bdfd41'
            '2d78092a700788c74b86db636af303fdb63a28ce5b7b0431dd81f6b7ce501e5d0234a6327a1b49bc23e1c1d00ba98fd5334dd07d9a20bb0d81d1a4ca4487a26c'
            '0e3459e58a32e6eee83673e688a75e19a0e6925f5f34c860d60c37b05a7816bbe1fd29712c1259611b856ae6576cbef8fa71425b7acc39f51ded706534c72281'
            'd297728681538fd6d6d48da4477e6e42b0ac1585a243dca60c0d9896387a1bf17770aa70966344c8d3551b774cbea6d6acbeaa0dbbfc3c17367dda5daa912297'
            '11fcfa704c05dbced579329b02844c6dd2c9ff7df59e95499f6778074d24d2b4e6903a53dd12833c322c50873f7aa5bae0d103bf0a1a977868f8cce67b53f15c')


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
  patch -p1 -i "$srcdir/chromium-gcc-r1.patch"
  patch -p1 -i "$srcdir/chromium-gn-bootstrap-r14.patch"
  patch -p1 -i "$srcdir/chromium-gcc5-r1.patch"
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
