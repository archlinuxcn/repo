# Maintainer: Nicola Squartini <tensor5@gmail.com>

pkgname=electron4
pkgver=4.2.12
_commit=3e0e966662c0ef2994d52566aaeb0850e18cdb3e
_chromiumver=69.0.3497.128
pkgrel=6
pkgdesc='Build cross platform desktop apps with web technologies'
arch=('x86_64')
url='https://electronjs.org/'
license=('MIT' 'custom')
depends=('c-ares' 'ffmpeg' 'gtk3' 'http-parser' 'libevent' 'libnghttp2'
         'libxslt' 'libxss' 'minizip' 'nss' 're2' 'snappy')
makedepends=('clang' 'git' 'gn-m76' 'gperf' 'harfbuzz-icu' 'jsoncpp' 'libnotify'
             'lld' 'llvm' 'ninja' 'npm' 'pciutils' 'python2' 'wget' 'yasm')
optdepends=('kde-cli-tools: file deletion support (kioclient5)'
            'trash-cli: file deletion support (trash-put)'
            "xdg-utils: open URLs with desktop's default (xdg-email, xdg-open)")
source=('git+https://github.com/electron/electron.git'
        'git+https://chromium.googlesource.com/chromium/tools/depot_tools.git'
        'electron4.desktop'
        'default_app-icon.patch'
        'use-system-libraries-in-node.patch'
        'chromium-SIOCGSTAMP.patch'
        'chromium-skia-harmony.patch'
        'icu65.patch'
        'glslang-remove-setAllocator.patch'
        'chromium-system-icu.patch'
        'fix-cfi-icall-failure-with-use_system_libjpeg-true.patch'
        'only-disable-cfi-icall-when-use_system_libjpeg-true.patch'
       )
sha256sums=('SKIP'
            'SKIP'
            '6a4f7164c60aede9bdc866a5f8b6a1bb473e498a6dcea9bf73f64843af34f0aa'
            '37372e8afd7c2405a8e50bca95c98b3c78e4c9b681cbef16da9c7a84b45e41e3'
            '3a81953701ac976a311db4e17999e67ab7c6de97ff63388f287d6497ef9adb9b'
            '7acc4dd59b70fb64f602ceda2846ccddcb46f64a18f912658d1034965f6c1276'
            'feca54ab09ac0fc9d0626770a6b899a6ac5a12173c7d0c1005bc3964ec83e7b3'
            '1de9bdbfed482295dda45c7d4e323cee55a34e42f66b892da1c1a778682b7a41'
            '06738b3f2d3579cd9b4d1ff876ba93d6b10a741b4deb4eab7fe3008cc577c893'
            'c4f2d1bed9034c02b8806f00c2e8165df24de467803855904bff709ceaf11af5'
            '97b421bc60a4abdf37de2d88a51b973e9f68fb44d1eccd464adfb3d9f5d71478'
            '9cae9ded6497afd15ad72d963897425ab6c7f28941bb3c3948e7996610a0d180')

_system_libs=('ffmpeg'
              'flac'
              'fontconfig'
              'freetype'
              'harfbuzz-ng'
              'icu'
              'libdrm'
              'libevent'
              'libjpeg'
#              'libpng'
#              'libvpx'
              'libwebp'
              'libxml'
              'libxslt'
#              'openh264'
              'opus'
              're2'
              'snappy'
              'yasm'
              'zlib'
             )

prepare() {
  mkdir -p "${srcdir}"/python2-path
  ln -sf /usr/bin/python2 "${srcdir}/python2-path/python"
  export PATH="${srcdir}/python2-path:${PATH}:${srcdir}/depot_tools"

  echo "Fetching chromium..."
  git clone --branch=${_chromiumver} --depth=1 \
      https://chromium.googlesource.com/chromium/src.git

  echo "solutions = [
  {
    \"name\": \"src/electron\",
    \"url\": \"file://${srcdir}/electron@${_commit}\",
    \"deps_file\": \"DEPS\",
    \"managed\": False,
    \"custom_deps\": {
      \"src\": None,
    },
    \"custom_vars\": {},
  },
]" > .gclient

  python2 "${srcdir}/depot_tools/gclient.py" sync \
      --with_branch_heads \
      --with_tags \
      --nohooks

  sed -e "s/'am'/'apply'/" -i src/electron/script/lib/git.py

  echo "Running hooks..."
  # python2 "${srcdir}/depot_tools/gclient.py" runhooks
  python2 src/build/landmines.py
  python2 src/build/util/lastchange.py -o src/build/util/LASTCHANGE
  python2 src/build/util/lastchange.py -m GPU_LISTS_VERSION \
    --revision-id-only --header src/gpu/config/gpu_lists_version.h
  python2 src/build/util/lastchange.py -m SKIA_COMMIT_HASH \
    -s src/third_party/skia --header src/skia/ext/skia_commit_hash.h
  # Create sysmlink to system Node.js
  mkdir -p src/third_party/node/linux/node-linux-x64/bin
  ln -sf /usr/bin/node src/third_party/node/linux/node-linux-x64/bin
  python2 src/third_party/depot_tools/download_from_google_storage.py \
    --no_resume --extract --no_auth --bucket chromium-nodejs \
    -s src/third_party/node/node_modules.tar.gz.sha1
  vpython src/chrome/android/profiles/update_afdo_profile.py
  python2 src/electron/script/apply_all_patches.py \
      src/electron/patches/common/config.json
  cd src/electron
  npm install
  cd ..

  echo "Patching Chromium for using system libraries..."
  sed -i 's/OFFICIAL_BUILD/GOOGLE_CHROME_BUILD/' \
      tools/generate_shim_headers/generate_shim_headers.py
  for lib in "${_system_libs[@]}" libjpeg_turbo; do
      third_party_dir="third_party/${lib}"
      if [ ! -d ${third_party_dir} ]; then
        third_party_dir="base/${third_party_dir}"
      fi
      find ${third_party_dir} -type f \
          \! -path "${third_party_dir}/chromium/*" \
          \! -path "${third_party_dir}/google/*" \
          \! -path 'third_party/yasm/run_yasm.py' \
          \! -regex '.*\.\(gn\|gni\|isolate\)' \
          -delete
  done
  python2 build/linux/unbundle/replace_gn_files.py \
      --system-libraries \
      "${_system_libs[@]}"

  echo "Applying local patches..."
  patch -Np1 -i ../chromium-SIOCGSTAMP.patch
  patch -Np4 -i ../chromium-skia-harmony.patch
  patch -Np1 -i ../icu65.patch
  patch -Np1 -d third_party/glslang/src <../glslang-remove-setAllocator.patch
  patch -Np1 -d third_party/angle/third_party/glslang/src <../glslang-remove-setAllocator.patch
  patch -Np1 -i ../chromium-system-icu.patch
  patch -Np1 -i ../fix-cfi-icall-failure-with-use_system_libjpeg-true.patch
  patch -Np1 -i ../only-disable-cfi-icall-when-use_system_libjpeg-true.patch
  patch -Np1 -i ../use-system-libraries-in-node.patch
  patch -Np1 -i ../default_app-icon.patch  # Icon from .desktop file
}

build() {
  export CC=clang
  export CXX=clang++
  export AR=ar
  export NM=nm

  cd src
  export CHROMIUM_BUILDTOOLS_PATH="${PWD}/buildtools"
  GN_EXTRA_ARGS='
    clang_use_chrome_plugins = false
    custom_toolchain = "//build/toolchain/linux/unbundle:default"
    host_toolchain = "//build/toolchain/linux/unbundle:default"
    icu_use_data_file = false
    is_component_ffmpeg = false
    link_pulseaudio = true
    linux_use_bundled_binutils = false
    remove_webcore_debug_symbols = true
    treat_warnings_as_errors = false
    use_custom_libcxx = false
    use_gnome_keyring = false
    use_sysroot = false
  '
  gn-m76 gen out/Release \
      --args="import(\"//electron/build/args/release.gn\") ${GN_EXTRA_ARGS}"
  ninja -C out/Release electron
  # Strip before zip to avoid
  # zipfile.LargeZipFile: Filesize would require ZIP64 extensions
  strip -s out/Release/electron
  ninja -C out/Release electron_dist_zip
  # ninja -C out/Release third_party/electron_node:headers
}

package() {
  install -dm755 "${pkgdir}/usr/lib/${pkgname}"
  bsdtar -xf src/out/Release/dist.zip -C "${pkgdir}/usr/lib/${pkgname}"

  install -dm755 "${pkgdir}/usr/share/licenses/${pkgname}"
  for l in "${pkgdir}/usr/lib/${pkgname}"/{LICENSE,LICENSES.chromium.html}; do
    ln -s  \
      $(realpath --relative-to="${pkgdir}/usr/share/licenses/${pkgname}" ${l}) \
      "${pkgdir}/usr/share/licenses/${pkgname}"
  done

  install -dm755 "${pkgdir}"/usr/bin
  ln -s ../lib/${pkgname}/electron "${pkgdir}"/usr/bin/${pkgname}

  # Install .desktop and icon file (see default_app-icon.patch)
  install -Dm644 -t "${pkgdir}/usr/share/applications" ${pkgname}.desktop
  install -Dm644 src/electron/default_app/icon.png \
          "${pkgdir}/usr/share/pixmaps/${pkgname}.png"  # hicolor has no 1024x1024
}
