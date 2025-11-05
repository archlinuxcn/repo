# Use environment variable MAKEPKG_AYUGRAM_API_ID and MAKEPKG_AYUGRAM_API_HASH to override default values

pkgname=ayugram-desktop
pkgver=5.16.4
pkgrel=6
pkgdesc="Desktop Telegram client with good customization and Ghost mode."
arch=("x86_64")
url="https://github.com/AyuGram/AyuGramDesktop"
license=("GPL-3.0-or-later WITH OpenSSL-exception")
depends=('abseil-cpp'
         'ada'
         'ffmpeg'
         'glib2'
         'hicolor-icon-theme'
         'hunspell'
         'kcoreaddons'
         'libavif'
         'libdispatch'
         'libheif'
         'libjxl'
         'libxcomposite'
         'libxdamage'
         'libxrandr'
         'libxtst'
         'lz4'
         'minizip'
         'openal'
         'openh264'
         'openssl'
         'pipewire'
         'protobuf'
         'qt6-imageformats'
         'qt6-svg'
         'qt6-wayland'
         'rnnoise'
         'xxhash')
makedepends=('boost'
             'cmake'
             'glib2-devel'
             'gobject-introspection'
             'gperf'
             'libtg_owt'
             'microsoft-gsl'
             'ninja'
             'python'
             'range-v3'
             'tl-expected')
optdepends=('geoclue: geoinformation support'
            'geocode-glib-2: geocoding support'
            'webkit2gtk-4.1: embedded browser features provided by webkit2gtk-4.1'
            'webkitgtk-6.0: embedded browser features provided by webkitgtk-6.0 (Wayland only)'
            'xdg-desktop-portal: desktop integration')
install=ayugram-desktop.install
_tdlib_commit=51743dfd01dff6179e2d8f7095729caa4e2222e9
source=("AyuGram-v$pkgver.tar.gz::https://github.com/AyuGram/AyuGramDesktop/archive/refs/tags/v$pkgver.tar.gz"
        "td-$_tdlib_commit.tar.gz::https://github.com/tdlib/td/archive/$_tdlib_commit.tar.gz"
        "glib2.86.patch"
        "0001-Fix-compatibility-with-ffmpeg-8.patch"
        "https://github.com/desktop-app/cmake_helpers/commit/682f1b57.patch"
        "https://github.com/telegramdesktop/tdesktop/commit/28d19a99.patch")
declare -Ag _modules_name_map=([cmake]=https://github.com/desktop-app/cmake_helpers/archive/f3d6471bd58dbad727d4f8fbccd0fb36632eee9e.tar.gz
                               [cmake/external/glib/cppgir]=https://gitlab.com/mnauw/cppgir/-/archive/33ee935b39efd03bb7ab8f62ad02f7f2cd018dc8/cppgir-33ee935b39efd03bb7ab8f62ad02f7f2cd018dc8.tar.gz
                               [cmake/external/glib/cppgir/expected-lite]=https://github.com/martinmoene/expected-lite/archive/95b9cb015fa17baa749c2b396b335906e1596a9e.tar.gz
                               [Telegram/codegen]=https://github.com/desktop-app/codegen/archive/5a0421e4623f6e2da58620f3818ae19df9309b43.tar.gz
                               [Telegram/lib_base]=https://github.com/desktop-app/lib_base/archive/402034cba675220647c5e2041f38cf9d977d496e.tar.gz
                               [Telegram/lib_crl]=https://github.com/desktop-app/lib_crl/archive/c1d6b0273653095b10b4d0f4f7c30b614b690fd5.tar.gz
                               [Telegram/lib_lottie]=https://github.com/desktop-app/lib_lottie/archive/4fc3ac0ea52f271cc9b108481f83d56fd76ab0ed.tar.gz
                               [Telegram/lib_qr]=https://github.com/desktop-app/lib_qr/archive/6fdf60461444ba150e13ac36009c0ffce72c4c83.tar.gz
                               [Telegram/lib_rpl]=https://github.com/desktop-app/lib_rpl/archive/9a3ce435f4054e6cbd45e1c6e3e27cfff515c829.tar.gz
                               [Telegram/lib_spellcheck]=https://github.com/desktop-app/lib_spellcheck/archive/c8ded8b7585f8819780ea22a40c237625aec0c75.tar.gz
                               [Telegram/lib_storage]=https://github.com/desktop-app/lib_storage/archive/ccdc72548a5065b5991b4e06e610d76bc4f6023e.tar.gz
                               [Telegram/lib_tl]=https://github.com/AyuGram/lib_tl/archive/79243fd193159382c204dde76d87584ed83ad06b.tar.gz
                               [Telegram/lib_ui]=https://github.com/AyuGram/lib_ui/archive/eed6fe4254c3670e48b680a7e0b61f642d3a40e8.tar.gz
                               [Telegram/lib_webrtc]=https://github.com/desktop-app/lib_webrtc/archive/e44439ed95559bfb4730db65f954937e149b7199.tar.gz
                               [Telegram/lib_webview]=https://github.com/desktop-app/lib_webview/archive/04c45d069fc0088740b9637bc5da414ee82be198.tar.gz
                               [Telegram/ThirdParty/GSL]=https://github.com/desktop-app/GSL/archive/87f9d768866548b5b86e72be66c60c5abd4d9b37.tar.gz
                               [Telegram/ThirdParty/QR]=https://github.com/nayuki/QR-Code-generator/archive/720f62bddb7226106071d4728c292cb1df519ceb.tar.gz
                               [Telegram/ThirdParty/cld3]=https://github.com/google/cld3/archive/b48dc46512566f5a2d41118c8c1116c4f96dc661.tar.gz
                               [Telegram/ThirdParty/dispatch]=https://github.com/apple/swift-corelibs-libdispatch/archive/886ca22f659c53dae66a40ee8266c7aae9bb97cd.tar.gz
                               [Telegram/ThirdParty/expected]=https://github.com/TartanLlama/expected/archive/292eff8bd8ee230a7df1d6a1c00c4ea0eb2f0362.tar.gz
                               [Telegram/ThirdParty/fcitx5-qt]=https://github.com/fcitx/fcitx5-qt/archive/c743b12e6780edf1dcfe9071531c80f050cacb95.tar.gz
                               [Telegram/ThirdParty/hime]=https://github.com/hime-ime/hime/archive/9b3e6f9ab59d1fe4d9de73d3bf0fed7789f921c5.tar.gz
                               [Telegram/ThirdParty/hunspell]=https://github.com/hunspell/hunspell/archive/22c3381e2066bed616250d373fc5c935598b564a.tar.gz
                               [Telegram/ThirdParty/kcoreaddons]=https://github.com/KDE/kcoreaddons/archive/fd84da51b554eac25e35b1e3f373edaab3029b15.tar.gz
                               [Telegram/ThirdParty/kimageformats]=https://github.com/KDE/kimageformats/archive/df82311a1081e576c4ac020204578bb8a81b21ec.tar.gz
                               [Telegram/ThirdParty/libprisma]=https://github.com/desktop-app/libprisma/archive/23b0d70f9709da9b38561d5706891a134d18df76.tar.gz
                               [Telegram/ThirdParty/lz4]=https://github.com/lz4/lz4/archive/5ff839680134437dbf4678f3d0c7b371d84f4964.tar.gz
                               [Telegram/ThirdParty/nimf]=https://github.com/hamonikr/nimf/archive/498ec7ffab3ac140c2469638a14451788f03e798.tar.gz
                               [Telegram/ThirdParty/range-v3]=https://github.com/ericniebler/range-v3/archive/a81477931a8aa2ad025c6bda0609f38e09e4d7ec.tar.gz
                               [Telegram/ThirdParty/range-v3/doc/gh-pages]=https://github.com/ericniebler/range-v3/archive/2dae74bb693e42d850fb0adcc9045c5b71fbdeae.tar.gz
                               [Telegram/ThirdParty/rlottie]=https://github.com/desktop-app/rlottie/archive/8c69fc20cf2e150db304311f1233a4b55a8892d7.tar.gz
                               [Telegram/ThirdParty/tgcalls]=https://github.com/TelegramMessenger/tgcalls/archive/d78b0507c54d76d5fe9691c8efe2638dee2c1536.tar.gz
                               [Telegram/ThirdParty/xdg-desktop-portal]=https://github.com/flatpak/xdg-desktop-portal/archive/11c8a96b147aeae70e3f770313f93b367d53fedd.tar.gz
                               [Telegram/ThirdParty/xxHash]=https://github.com/Cyan4973/xxHash/archive/bbb27a5efb85b92a0486cf361a8635715a53f6ba.tar.gz)

_get_source_name_string() {
    local host filename name commit
    host=$(echo "$1" | cut -d / -f 3)
    name=$(echo "$1" | cut -d / -f 5)
    filename=${1##*/}
    commit=${filename%%.*}
    case "$host" in
        gitlab.com)
            # It contains $name in $commit
            echo "$commit"
            ;;
        *)
            echo "$name-$commit"
            ;;
    esac
}

_fill_gitmodules_recursively() {
    local gitmodule
    find "${1:-.}" -type f -name .gitmodules | while read -r gitmodule
    do
        if [[ "$gitmodule" =~ ^\.\/ ]]
        then
            gitmodule=${gitmodule#*\.\/}
        fi
        local prefix
        prefix=$(dirname "$gitmodule")"/"
        if [[ "$prefix" =~ ^\.\/ ]]
        then
            prefix=${prefix#*\.\/}
        fi
        echo "Parsing $gitmodule to fill submodules..."
        local p
        grep path "$gitmodule" | awk '{print $3}' | while read -r p
        do
            p=${p%$'\r'} # Remove control characters
            if [[ -n "$p" ]]
            then
                local target url name commit fname
                target="$prefix$p"
                url="${_modules_name_map[$target]}"
                fname=$(_get_source_name_string "$url")
                echo "Filling $target with $srcdir/$fname..."
                cp -r "$srcdir/$fname/." "$target"
                _fill_gitmodules_recursively "$target"
            fi
        done
    done
}
declare _source_str _uri
for _uri in "${_modules_name_map[@]}"
do
    _source_str="$(_get_source_name_string "$_uri").tar.gz::$_uri"
    if [[ "${source[*]/$_source_str/}" == "${source[*]}" ]]
    then
        source+=("$_source_str")
    fi
done
unset _source_str _uri

sha256sums=('a6342cb3dc5f9112d05942998c50cf0688d6487842541a333b6a94bcbb1bfa8e'
            'f2c6b92533ba41a024b9fdb86d346c8bfc876d5961738ad463effbd844d61405'
            '57b855e701ed29da039431b2688082e6885c368e20dd38bbedffe1633e5efeda'
            'd44a47b0dda36762090bbfcbb8e402d7308f3646d99a882b7d5fc3c18cc63540'
            'beb19d9a662fbb73045bd15ffae6d90462d6c9b46897aea7ae04c7da8081f04c'
            'd73dfc4e16edb22c6060d6672d72006a30c9fa3032670a49fa703528166ddcfa'
            'd0d4ea2fddcbc7d10ace2c37309feb09da87e8ce7ced6ce73592da1359f4765f'
            '269cc8fe51bd6344d2f3924c999912053d2acf8cfeee53e6f3e1ccc9bb3891f6'
            '6c16c9cc1dea66bdd9340735e447906e191caf87133a10ead077fbf1bd3b0121'
            'cbc1f4bf8c28ffeb89852eda7056ff6aa80d49cb45736a583c931d5ceeccdcdd'
            '3e7253b2cc31bdf68fa50d105715158e649812e5ad6b4f1f6e5fd1e89b3ffdfd'
            '7ce0d7b8cfc14b77d42f4dec5e18b9e4b3e67ce806347b16db944f9a0698a636'
            '8a99b7951d6d428118a26ddba9a30175517454efc8e656e6f48b9bd07b873f1c'
            'e54e7c0aa2467d365f235db5b1bcc1919098ade89b9b3637a78bf7b875cf3b6f'
            '024400281b0aa927374dd94618feea171373d95a1cb897be50511a03fb84d04a'
            '8569c9bf5495b19b76ce6e2e53f40604c8618429ce728bf73b2406d1382fdc94'
            '716fbe4fc85ecd36488afbbc635b59b5ab6aba5ed3b69d4a32a46eae5a453d38'
            '11b926f9605b258c35bd9ed806a10cab7ef5edd673ad53a014427b1c71d24a9e'
            'b838912f5fdc830eaab68d5def68734ede1f6025f2c5791184773db1a4333129'
            'fe3b18aecb849029b6af94922be0c25eee1b7b86565b1c8350692ed776cf42fb'
            'eda5df4249051db521c32fb54a8e1864c4f1e50222e431028ba0cad169621ea9'
            'dd9b92f8bb26cf5eb543d4e9c5c1c62e17449588caa9eaf2500db09b5f3aed25'
            '613827512b959831d44ce31138154b4e55500483d3ad318fd2a0646ba5c18f6b'
            '612b5d89f58a578240b28a1304ffb0d085686ebe0137adf175ed0e3382b7ed58'
            '68648a80738681b58ab9c58340f37355c73bd3be96fcc1533660eb90f57c65cd'
            'f211afa22970e7a887d9e16246ab7838ac1c1254d1aa044d227852e9e2877e10'
            '455d1b63d72bad0034dc96ea7696dbd3b4fe48b93721f117ee345574937ff153'
            'd80795686f3e58448c7b76830bb5c40847b7eaae1996c28f0422a029b66c2bb0'
            'aba69c97d466e82a13ae6c1d52628c7f7ec8f85c5224f8634fa26a313ebcc95f'
            '2eaf5f6976f4c990ea2c2f8f8cd0f4ec22a935f799d6f901f10088845707a946'
            '52a2e052beb67492225a38213108f1d7edd1940fd025cad3a4ae28c57d428419'
            '41641c1a7e927662a6722a1d7df4c5f60d67fed9cc1f555b6be7d13d14542a68'
            '3d2eef00fd1739a652ef22f2d081497bc9ae71008ff6736945f2d2676cc6bba9'
            '73e639df3c73136eeb1890fc54acd603849fba01443005fd3c1a288539885792'
            '79612b46ce4473307e1004e5bfa10ce37beb1dbd34cb94fa771b13daf78cae2c'
            '2736d6f36f9f90323f2a0ed6fa59f52b8be71f50939708dffb0eb9f8155bbde1'
            '9620530807f9692ae795af5277457638c8a13ee796692e1789a845b5df79742a'
            '6cea3615f0bd1a6631aa4e65c363854ffbb4e81bbb75a932d61392b16ad5ad4b'
            '7238a966ee6b93fdbf2669736ddd35a6103967eb9d5369af8b740bff2401615c'
            '0bb1ac2b495bf7056a57a1b9bd6020007041eb7b6cc85467ae55d0eb5c8254e8')

prepare() {
    cd "$srcdir/AyuGramDesktop-$pkgver"
    _fill_gitmodules_recursively
    #/usr/bin/ld: /usr/lib/libprotobuf-lite.so: undefined reference to symbol '_ZN4absl12lts_2023080212log_internal17MakeCheckOpStringIllEEPNSt7__cxx1112basic_stringIcSt11char_traitsIcESaIcEEET_T0_PKc'
    #/usr/bin/ld: /usr/lib/libabsl_log_internal_check_op.so.2308.0.0: error adding symbols: DSO missing from command line
    #collect2: error: ld returned 1 exit status
    #
    #https://github.com/telegramdesktop/tdesktop/issues/26489#issuecomment-1627535022
    sed -i 's/find_package(protobuf REQUIRED)/find_package(protobuf REQUIRED CONFIG)/' \
        Telegram/ThirdParty/cld3/CMakeLists.txt
    #https://github.com/telegramdesktop/tdesktop/issues/26489#issuecomment-1627555107
    #CMAKE_BUILD_TYPE must match libtg_owt's
    cd "$srcdir"
    patch -d "AyuGramDesktop-$pkgver" -Np1 -i ../glib2.86.patch
    # Fix compatibility with ffmpeg 8
    patch -d "AyuGramDesktop-$pkgver" -Np1 -i ../0001-Fix-compatibility-with-ffmpeg-8.patch
    # Fix build with Qt 6.10
    patch -d "AyuGramDesktop-$pkgver/cmake" -p1 < 682f1b57.patch
    ## Different with Telegram Desktop:
    # Only `malloc_trim(0)` here.
    # https://github.com/AyuGram/AyuGramDesktop/blob/dev/Telegram/SourceFiles/platform/linux/integration_linux.cpp#L179
    # https://github.com/telegramdesktop/tdesktop/blob/dev/Telegram/SourceFiles/platform/linux/integration_linux.cpp#L182
    head -n 27 28d19a99.patch | patch -d "AyuGramDesktop-$pkgver" -p1
}
build() {
    CXXFLAGS+=' -ffat-lto-objects'
    cmake -B td-$_tdlib_commit/build -S td-$_tdlib_commit \
        -DCMAKE_BUILD_TYPE=None \
        -DCMAKE_INSTALL_PREFIX="$PWD/td-$_tdlib_commit/install" \
        -Wno-dev \
        -DTD_E2E_ONLY=ON
    cmake --build td-$_tdlib_commit/build
    cmake --install td-$_tdlib_commit/build  
    # https://github.com/AyuGram/AyuGramDesktop/blob/dev/docs/building-linux.md#building-the-project
    # for API_ID and API_HASH
    cmake -B build -S AyuGramDesktop-$pkgver -G Ninja \
        -DCMAKE_INSTALL_PREFIX="/usr" \
        -DCMAKE_BUILD_TYPE=Release \
        -DTDESKTOP_API_ID="${MAKEPKG_AYUGRAM_API_ID:-2040}" \
        -DTDESKTOP_API_HASH="${MAKEPKG_AYUGRAM_API_HASH:-b18441a1ff607e10a989891a5462e627}" \
        -DDESKTOP_APP_DISABLE_AUTOUPDATE=True \
        -Dtde2e_DIR="$PWD/td-$_tdlib_commit/install/lib/cmake/tde2e"
    cmake --build build
}
package() {
    DESTDIR="$pkgdir" cmake --install build
}
