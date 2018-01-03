# $Id$
# Maintainer: Jiachen Yang <farseerfc@archlinux.org>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: ponsfoot <cabezon dot hashimoto at gmail dot com>
# Contributor: UTUMI Hirosi <utuhiro78 at yahoo dot co dot jp>

## Mozc compile option
_bldtype=Debug

_mozc_rev=280e38fe3d9db4df52f0713acf2ca65898cd697a
_japanese_usage_dictionary_rev=e5b3425575734c323e1d947009dd74709437b684
_gyp_rev=920ee58c3d3109dea3cd37d88054014891a93db7
_protobuf_rev=a428e42072765993ff674fda72863c9f1aa2d268
_zipcode_rel=201703

_pkgbase=mozc
pkgname=fcitx5-mozc-git
pkgdesc="Fcitx5 Module of A Japanese Input Method for Chromium OS, Windows, Mac and Linux (the Open Source Edition of Google Japanese Input)"
pkgver=2.18.2612.102.1.r1171.5dd2b693
_fcitx_patchver=2.18.2612.102.1
pkgrel=1.2
arch=('x86_64')
url="https://github.com/google/mozc"
license=('custom')
depends=('qt5-base' 'fcitx5-git' 'zinnia')
makedepends=('pkg-config' 'python2' 'curl' 'gtk2' 'mesa' 'subversion' 'ninja' 'git' 'clang')
replaces=('mozc-fcitx')
conflicts=('mozc' 'mozc-server' 'mozc-utils-gui' 'mozc-fcitx' 'fcitx-mozc')
source=(git+https://github.com/fcitx/mozc.git#branch=fcitx
        japanese_usage_dictionary::git+https://github.com/hiroyuki-komatsu/japanese-usage-dictionary.git#commit=${_japanese_usage_dictionary_rev}
        mozc-gyp::git+https://chromium.googlesource.com/external/gyp#commit=${_gyp_rev}
        git+https://github.com/google/protobuf.git#commit=${_protobuf_rev}
        http://downloads.sourceforge.net/pnsft-aur/x-ken-all-${_zipcode_rel}.zip
        http://downloads.sourceforge.net/pnsft-aur/jigyosyo-${_zipcode_rel}.zip
	)
sha512sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'aecd93a99c460fbbb9790bdf9e024a313b62cf51a1fec23bc19da0f375ddaeec37fe3bdf5d44930d16da9d1ba0b3205a2da008c4be611165ae474c469d173176'
            'e426652cfa1ab6360c00770a76d12089165ba66364aaf8b6dcd3b6bf9fc7b154ec490eea77476eefd7e1551cf84165a45f165bb6cfab4964a1bb682220e11e28')
validpgpkeys=('2CC8A0609AD2A479C65B6D5C8E8B898CBF2412F9')  # Weng Xuetian

pkgver() {
  cd mozc
  printf "%s.r%s.%s" "${_fcitx_patchver}" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

prepare() {
  mv mozc-gyp gyp

  cd mozc

  ## Apply fcitx patch
  #rm unix/fcitx -rf
  #patch -Np2 -i "$srcdir/fcitx-mozc-${_fcitx_patchver}.patch"

  # Adjust to use python2
  find . -name  \*.py        -type f -exec sed -i -e "1s|python.*$|python2|"  {} +
  find scripts               -type f -exec sed -i -e "s|python |python2 |"  {} +
  find . -regex '.*\.gypi?$' -type f -exec sed -i -e "s|'python'|'python2'|g" {} +

  cd src
  # Generate zip code seed
  msg "Generating zip code seed..."
  PYTHONPATH="$PWD:$PYTHONPATH" python2 dictionary/gen_zip_code_seed.py --zip_code="${srcdir}/x-ken-all.csv" --jigyosyo="${srcdir}/JIGYOSYO.CSV" >> data/dictionary_oss/dictionary09.txt
  msg "Done."

  # disable fcitx4 target 
  rm unix/fcitx/fcitx.gyp

  # Copy third party deps
  cd "$srcdir"
  for dep in gyp protobuf japanese_usage_dictionary
  do
    cp -a $dep mozc/src/third_party/
  done
}

build() {
  # Fix compatibility with google-glog 0.3.3 (symbol conflict)
  CFLAGS="${CFLAGS} -fvisibility=hidden"
  CXXFLAGS="${CXXFLAGS} -fvisibility=hidden"

  cd mozc/src

  _targets="server/server.gyp:mozc_server gui/gui.gyp:mozc_tool unix/fcitx5/fcitx5.gyp:fcitx5-mozc"

  QTDIR=/usr GYP_DEFINES="document_dir=/usr/share/licenses/$pkgname use_libzinnia=1" python2 build_mozc.py gyp
  python2 build_mozc.py build -c $_bldtype $_targets

  #cd mozc/src
  #../scripts/configure
  #../scripts/build_fcitx5

  # Extract license part of mozc
  head -n 29 server/mozc_server.cc > LICENSE
}

package() {
  #cd mozc/src
  #install -D -m 755 out_linux/${_bldtype}/mozc_server "${pkgdir}/usr/lib/mozc/mozc_server"
  #install    -m 755 out_linux/${_bldtype}/mozc_tool   "${pkgdir}/usr/lib/mozc/mozc_tool"

  cd mozc/src
  export PREFIX="${pkgdir}/usr"
  ../scripts/install_server

  install -d "${pkgdir}/usr/share/licenses/$pkgname/"
  install -m 644 LICENSE data/installer/*.html "${pkgdir}/usr/share/licenses/${pkgname}/"

  #for mofile in out_linux/${_bldtype}/gen/unix/fcitx/po/*.mo
  #do
  #  filename=`basename $mofile`
  #  lang=${filename/.mo/}
  #  install -D -m 644 "$mofile" "${pkgdir}/usr/share/locale/$lang/LC_MESSAGES/fcitx-mozc.mo"
  #done

  #install -D -m 755 out_linux/${_bldtype}/fcitx-mozc.so "${pkgdir}/usr/lib/fcitx/fcitx-mozc.so"
  #install -D -m 644 unix/fcitx/fcitx-mozc.conf "${pkgdir}/usr/share/fcitx/addon/fcitx-mozc.conf"
  #install -D -m 644 unix/fcitx/mozc.conf "${pkgdir}/usr/share/fcitx/inputmethod/mozc.conf"

  #install -d "${pkgdir}/usr/share/fcitx/mozc/icon"
  #install -m 644 "$srcdir/fcitx-mozc-icons/mozc.png" "${pkgdir}/usr/share/fcitx/mozc/icon/mozc.png"
  #install -m 644 "$srcdir/fcitx-mozc-icons/mozc-alpha_full.png" "${pkgdir}/usr/share/fcitx/mozc/icon/mozc-alpha_full.png"
  #install -m 644 "$srcdir/fcitx-mozc-icons/mozc-alpha_half.png" "${pkgdir}/usr/share/fcitx/mozc/icon/mozc-alpha_half.png"
  #install -m 644 "$srcdir/fcitx-mozc-icons/mozc-direct.png" "${pkgdir}/usr/share/fcitx/mozc/icon/mozc-direct.png"
  #install -m 644 "$srcdir/fcitx-mozc-icons/mozc-hiragana.png" "${pkgdir}/usr/share/fcitx/mozc/icon/mozc-hiragana.png"
  #install -m 644 "$srcdir/fcitx-mozc-icons/mozc-katakana_full.png" "${pkgdir}/usr/share/fcitx/mozc/icon/mozc-katakana_full.png"
  #install -m 644 "$srcdir/fcitx-mozc-icons/mozc-katakana_half.png" "${pkgdir}/usr/share/fcitx/mozc/icon/mozc-katakana_half.png"
  #install -m 644 "$srcdir/fcitx-mozc-icons/mozc-dictionary.png" "${pkgdir}/usr/share/fcitx/mozc/icon/mozc-dictionary.png"
  #install -m 644 "$srcdir/fcitx-mozc-icons/mozc-properties.png" "${pkgdir}/usr/share/fcitx/mozc/icon/mozc-properties.png"
  #install -m 644 "$srcdir/fcitx-mozc-icons/mozc-tool.png" "${pkgdir}/usr/share/fcitx/mozc/icon/mozc-tool.png"
  install -d "${PREFIX}/share/fcitx5/addon"
  install -d "${PREFIX}/share/fcitx5/inputmethod"
  install -d "${PREFIX}/lib/fcitx5"
  ../scripts/install_fcitx5

}
