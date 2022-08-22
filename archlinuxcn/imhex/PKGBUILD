# Maintainer: KokaKiwi <kokakiwi+aur@kokakiwi.net>
# Contributor: George Rawlinson <george@rawlinson.net.nz>

_pkgname=ImHex
pkgname=${_pkgname,,}
pkgver=1.21.2
pkgrel=1
pkgdesc='A Hex Editor for Reverse Engineers, Programmers and people that value their eye sight when working at 3 AM'
url='https://imhex.werwolv.net'
license=('GPL2')
arch=('x86_64')
depends=('glfw' 'mbedtls' 'libssh2' 'curl' 'dbus'
         'freetype2' 'file' 'hicolor-icon-theme' 'xdg-desktop-portal'
         'fmt' 'yara')
makedepends=('git' 'cmake' 'llvm' 'nlohmann-json' 'librsvg' 'python')
optdepends=(
  'imhex-patterns-git: ImHex base patterns'
)
source=("$pkgname::git+https://github.com/WerWolv/ImHex.git#tag=v$pkgver"
        "nativefiledialog::git+https://github.com/btzy/nativefiledialog-extended.git"
        "xdgpp::git+https://git.sr.ht/~danyspin97/xdgpp"
        "libromfs::git+https://github.com/WerWolv/libromfs"
        "capstone::git+https://github.com/capstone-engine/capstone#branch=next"
        "pattern_language::git+https://github.com/WerWolv/PatternLanguage#tag=ImHex-v$pkgver"
        0001-makepkg-Fix-compiler-check.patch
        0002-makepkg-Fix-build-with-clang.patch
        0003-fix-Deduplicate-resources-directories.patch
        pl-0001-fix-Copy-elision-not-applying.patch
        pl-0002-Use-C-23-standard.patch)
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'SKIP'
            'fe029ddb8ac99bd0cec7ee849ca597eb771a0be29e774afebe890997756d815d'
            '309c303817210ded39d0edaec5c2e9dee59f0a3a34e833227353bcd56931f439'
            '9741c1e3d6c1786c335b578d0ecc68592e29c98c5b9e051257948cd3c137c339'
            '1635946b85e0e228ed75a4e3f3231ddf99b8d3674c1d3cdb1be028571d8e6f57'
            '94ada965ad0be7fe511b42e9f5726cd071385f43393aeaebfca71899aad32ed4')
b2sums=('SKIP'
        'SKIP'
        'SKIP'
        'SKIP'
        'SKIP'
        'SKIP'
        '4e7ad0db57425a05ed78eb5cfa600f1225db11e55ebc2cd399aaa37dd068b5a9fbbc30fc18b65190a3b59ad46393bdc57da79ce8306007c15f74874c6d7cb4e5'
        'c3e7286f3673da385d89b9edc5af218fbdb6bb8465b599668bdfb9bf0d216eec67508302ded50a4d046825c2fafd2b77a71d0d4e4807713cdff5aa416e249140'
        'deb706d01827ae67309d0a0341c79c2255166ba731632d0a29afcf875d57ac9885a5203de65fd9b0fa03ff13197af5a1fb1e1aba2e5a4904093a11e388c0d706'
        '973d4cf8472c132f7e470945bff1ea8afb113834913cce8bf553dd2f29c28a9e8b93f94b331443f2d5c350f1d6141677cda4f7d30e1bd4e547cb489fff435029'
        '029ac69a0824c61ce92a26eafe37e082c25bab633bf48b64b10b212e61b579bd7b35470bba901da5cf0068db28917a50d83140790aad44d28c8d5647e01cd473')
options=(!lto !strip)

prepare() {
  cd "$pkgname"

  git submodule init
  for name in nativefiledialog xdgpp libromfs capstone pattern_language; do
    git config submodule.lib/external/$name.url "$srcdir/$name"
  done
  for name in fmt curl yara/yara; do
    git config --remove-section submodule.lib/external/$name
  done
  git submodule update

  git apply \
    "$srcdir/0001-makepkg-Fix-compiler-check.patch" \
    "$srcdir/0002-makepkg-Fix-build-with-clang.patch" \
    "$srcdir/0003-fix-Deduplicate-resources-directories.patch"

  git -C lib/external/pattern_language apply \
    "$srcdir/pl-0001-fix-Copy-elision-not-applying.patch" \
    "$srcdir/pl-0002-Use-C-23-standard.patch"
}

build() {
  export CXXFLAGS="$CXXFLAGS -Wno-inconsistent-missing-override"

  cmake -B build -S "$pkgname" \
    -Wno-dev \
    -D CMAKE_BUILD_TYPE=Release \
    -D CMAKE_INSTALL_PREFIX=/usr \
    -D CMAKE_SKIP_RPATH=ON \
    -D IMHEX_OFFLINE_BUILD=ON \
    -D IMHEX_IGNORE_BAD_CLONE=ON \
    -D IMHEX_STRIP_RELEASE=OFF \
    -D USE_SYSTEM_LLVM=ON \
    -D USE_SYSTEM_YARA=ON \
    -D USE_SYSTEM_FMT=ON \
    -D USE_SYSTEM_CURL=ON \
    -D USE_SYSTEM_NLOHMANN_JSON=ON \
    -D USE_SYSTEM_CAPSTONE=OFF \
    -D IMHEX_VERSION="$pkgver"

  make -C build
}

package() {
  # Executable
  install -Dm0755 build/imhex "$pkgdir/usr/bin/imhex"

  # Shared lib and plugins
  install -Dm0755 -t "$pkgdir/usr/lib" build/lib/libimhex/libimhex.so

  for plugin in builtin; do
    install -Dm0755 -t "$pkgdir/usr/lib/imhex/plugins" "build/plugins/$plugin.hexplug"
  done

  install -dm0755 "$pkgdir/usr/share/imhex"

  # Desktop file(s)
  install -Dm0644 -t "$pkgdir/usr/share/applications" "$pkgname/dist/imhex.desktop"
  install -Dm0644 "$pkgname/resources/icon.svg" "$pkgdir/usr/share/icons/hicolor/scalable/apps/imhex.svg"
  for size in 32 48 64 128 256; do
    install -dm0755 "$pkgdir/usr/share/icons/hicolor/${size}x${size}/apps"
    rsvg-convert -a -f png -w $size -o "$pkgdir/usr/share/icons/hicolor/${size}x${size}/apps/imhex.png" \
      "$pkgname/resources/icon.svg"
  done

  # License
  install -Dm0644 "$pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"

  # Documentation
  install -Dm0644 -t "$pkgdir/usr/share/doc/$pkgname" \
    "$pkgname/README.md"
}
