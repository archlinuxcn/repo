# $Id$
# Maintainer: Jiachen Yang <farseerfc@archlinux.org>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: ponsfoot <cabezon dot hashimoto at gmail dot com>
# Contributor: UTUMI Hirosi <utuhiro78 at yahoo dot co dot jp>

## Mozc compile option
_bldtype=Release

_zipcode_rel=202011

_pkgbase=mozc
pkgname=fcitx5-mozc-git
pkgdesc="Fcitx5 Module of A Japanese Input Method for Chromium OS, Windows, Mac and Linux (the Open Source Edition of Google Japanese Input)"
pkgver=2.26.4220.102.r1394.b862bc18
pkgrel=1
arch=('x86_64')
url="https://github.com/google/mozc"
license=('custom')
depends=('qt5-base' 'fcitx5-git')
makedepends=('pkg-config' 'python' 'curl' 'gtk2' 'mesa' 'subversion' 'ninja' 'git' 'clang' 'python-six')
replaces=('mozc-fcitx')
conflicts=('mozc' 'mozc-server' 'mozc-utils-gui' 'mozc-fcitx' 'fcitx-mozc' 'fcitx5-mozc')
source=(git+https://github.com/fcitx/mozc.git#branch=fcitx
        https://osdn.net/projects/ponsfoot-aur/storage/mozc/jigyosyo-${_zipcode_rel}.zip
        https://osdn.net/projects/ponsfoot-aur/storage/mozc/x-ken-all-${_zipcode_rel}.zip
        git+https://chromium.googlesource.com/breakpad/breakpad
        git+https://github.com/google/googletest.git
        git+https://chromium.googlesource.com/external/gyp
        git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git
        git+https://github.com/open-source-parsers/jsoncpp.git
        git+https://github.com/google/protobuf.git
        git+https://github.com/abseil/abseil-cpp.git
	)
sha512sums=('SKIP'
            '0ef2d0abd9744900f9a50f941cf1f9b47640f3643c14a1be1761bcf0bd1053cb93560203c25280f58fccbd8ec98b9ca2e21c5d5a59844bbbffc9c988dfcf7bed'
            '8a35672b4a525d8e4f3303bd83c6bf6075cd4f10e703bf656a4c9328f18a8783c3049b749092e6e8be57eaddce4f889e9dacae9b3b72ba7bb9240a0f5a93fd34'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP')
validpgpkeys=('2CC8A0609AD2A479C65B6D5C8E8B898CBF2412F9')  # Weng Xuetian

pkgver() {
  cd mozc
  # parse major.minor.buildid from version template, revision is fixed to 102 for Linux
  _bzr_ver=$(sed 's/ //g;$ a echo $MAJOR.$MINOR.$BUILD.102' src/data/version/mozc_version_template.bzl | source /dev/stdin)
  printf "%s.r%s.%s" "${_bzr_ver}" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  cd "$srcdir/mozc"
  git submodule init
  git config submodule.src/third_party/breakpad.url "$srcdir/breakpad"
  git config submodule.src/third_party/gtest.url "$srcdir/googletest"
  git config submodule.src/third_party/gyp.url "$srcdir/gyp"
  git config submodule.src/third_party/japanese_usage_dictionary.url "$srcdir/japanese-usage-dictionary"
  git config submodule.src/third_party/jsoncpp.url "$srcdir/jsoncpp"
  git config submodule.src/third_party/protobuf.url "$srcdir/protobuf"
  git config submodule.src/third_party/abseil-cpp.url "$srcdir/abseil-cpp"
  git submodule update

  cd src
  # Generate zip code seed
  echo "Generating zip code seed..."
  PYTHONPATH="$PWD:$PYTHONPATH" python dictionary/gen_zip_code_seed.py --zip_code="${srcdir}/x-ken-all.csv" --jigyosyo="${srcdir}/JIGYOSYO.CSV" >> data/dictionary_oss/dictionary09.txt
  echo "Done."

  # disable fcitx4 target
  rm unix/fcitx/fcitx.gyp
  
  ## use libstdc++ instead of libc++
  sed "/stdlib=libc++/d;/-lc++/d" -i gyp/common.gypi
}

build() {
  # Fix compatibility with google-glog 0.3.3 (symbol conflict)
  CFLAGS="${CFLAGS} -fvisibility=hidden"
  CXXFLAGS="${CXXFLAGS} -fvisibility=hidden"

  cd mozc/src

  _targets="server/server.gyp:mozc_server gui/gui.gyp:mozc_tool unix/fcitx5/fcitx5.gyp:fcitx5-mozc"

  QTDIR=/usr GYP_DEFINES="document_dir=/usr/share/licenses/$pkgname use_libzinnia=1" python build_mozc.py gyp
  python build_mozc.py build -c $_bldtype $_targets

  # Extract license part of mozc
  head -n 29 server/mozc_server.cc > LICENSE
}

package() {
  cd mozc/src
  export PREFIX="${pkgdir}/usr"
  export _bldtype
  ../scripts/install_server

  install -d "${pkgdir}/usr/share/licenses/$pkgname/"
  install -m 644 LICENSE data/installer/*.html "${pkgdir}/usr/share/licenses/${pkgname}/"

  install -d "${PREFIX}/share/fcitx5/addon"
  install -d "${PREFIX}/share/fcitx5/inputmethod"
  install -d "${PREFIX}/lib/fcitx5"
  ../scripts/install_fcitx5
}
