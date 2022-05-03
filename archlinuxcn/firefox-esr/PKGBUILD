# Maintainer : Luna Jernberg <droidbittin@gmail.com>
# Contributor: Jonathon Fernyhough <jonathon+m2x+dev>
# Contributor: Figue <ffigue@gmail.com>
# Contributor: Dct Mei <dctxmei@yandex.com>
# Contributor: Felix Golatofski <contact@xdfr.de>
# Contributor: Jan Alexander Steffens (heftig) <heftig@archlinux.org>
# Contributor: Ionut Biru <ibiru@archlinux.org>
# Contributor: Jakub Schmidtke <sjakub@gmail.com>

pkgbase=firefox-esr
pkgname=(firefox-esr)
pkgver=91.9.0
pkgrel=1
pkgdesc="Standalone web browser from mozilla.org, Extended Support Release"
arch=(x86_64)
license=(MPL GPL LGPL)
url="https://www.mozilla.org/en-US/firefox/enterprise/"
depends=(gtk3 libxt mime-types dbus-glib ffmpeg4.4 nss ttf-font libpulse)
makedepends=(unzip zip diffutils yasm mesa imake inetutils xorg-server-xvfb
             autoconf2.13 rust clang llvm jack nodejs cbindgen nasm
             python-setuptools python-psutil python-zstandard lld dump_syms)
optdepends=('networkmanager: Location detection via available WiFi networks'
            'libnotify: Notification integration'
            'pulseaudio: Audio support'
            'speech-dispatcher: Text-to-Speech'
            'hunspell-en_US: Spell checking, American English'
            'xdg-desktop-portal: Screensharing with Wayland')
options=(!emptydirs !makeflags !strip !lto !debug)
source=(https://archive.mozilla.org/pub/firefox/releases/${pkgver}esr/source/firefox-${pkgver}esr.source.tar.xz{,.asc}
        0001-Use-remoting-name-for-GDK-application-names.patch
        $pkgname.desktop identity-icons-brand.svg)
validpgpkeys=('14F26682D0916CDD81E37B6D61B7B526D98F0353') # Mozilla Software Releases <release@mozilla.com>

# Google API keys (see http://www.chromium.org/developers/how-tos/api-keys)
# Note: These are for Arch Linux use ONLY. For your own distribution, please
# get your own set of keys. Feel free to contact foutrelis@archlinux.org for
# more information.
_google_api_key=AIzaSyDwr302FpOSkGRpLlUpPThNTDPbXcIn_FM

# Mozilla API keys (see https://location.services.mozilla.com/api)
# Note: These are for Arch Linux use ONLY. For your own distribution, please
# get your own set of keys. Feel free to contact heftig@archlinux.org for
# more information.
_mozilla_api_key=e05d56db0a694edc8b5aaebda3f2db6a

prepare() {
  mkdir mozbuild
  cd firefox-$pkgver

  echo "${noextract[@]}"

  # https://bugzilla.mozilla.org/show_bug.cgi?id=1530052
  patch -Np1 -i ../0001-Use-remoting-name-for-GDK-application-names.patch

  echo -n "$_google_api_key" >google-api-key
  echo -n "$_mozilla_api_key" >mozilla-api-key

  cat >../mozconfig <<END
ac_add_options --enable-application=browser
mk_add_options MOZ_OBJDIR=${PWD@Q}/obj

ac_add_options --prefix=/usr
ac_add_options --enable-release
ac_add_options --enable-hardening
ac_add_options --enable-optimize
ac_add_options --enable-rust-simd
ac_add_options --enable-linker=lld
ac_add_options --disable-elf-hack
ac_add_options --disable-bootstrap

# Branding
ac_add_options --enable-official-branding
ac_add_options --enable-update-channel=release
ac_add_options --with-distribution-id=org.archlinux
ac_add_options --with-unsigned-addon-scopes=app,system
ac_add_options --allow-addon-sideload
ac_add_options --with-app-name=$pkgname
export MOZILLA_OFFICIAL=1
export MOZ_APP_REMOTINGNAME=$pkgname
export MOZ_APP_PROFILE="mozilla/firefox-esr"

# Keys
ac_add_options --with-google-location-service-api-keyfile=${PWD@Q}/google-api-key
ac_add_options --with-google-safebrowsing-api-keyfile=${PWD@Q}/google-api-key
ac_add_options --with-mozilla-api-keyfile=${PWD@Q}/mozilla-api-key

# System libraries
ac_add_options --with-system-nspr
ac_add_options --with-system-nss

# Features
ac_add_options --enable-alsa
ac_add_options --enable-jack
ac_add_options --enable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-tests
END
}

build() {
  cd firefox-$pkgver

  export MOZ_NOSPAM=1
  export MOZBUILD_STATE_PATH="$srcdir/mozbuild"
  export MOZ_ENABLE_FULL_SYMBOLS=1
  export MACH_USE_SYSTEM_PYTHON=1

  export MOZ_BUILD_DATE=$(head -1 sourcestamp.txt)
  export RUSTFLAGS="-C debuginfo=1"

  # LTO needs more open files
  ulimit -n 4096

  # Do 3-tier PGO
  echo "Building instrumented browser..."
  cat >.mozconfig ../mozconfig - <<END
ac_add_options --enable-profile-generate=cross
END
  ./mach build

  echo "Profiling instrumented browser..."
  ./mach package
  LLVM_PROFDATA=llvm-profdata \
    JARLOG_FILE="$PWD/jarlog" \
    xvfb-run -s "-screen 0 1920x1080x24 -nolisten local" \
    ./mach python build/pgo/profileserver.py

  stat -c "Profile data found (%s bytes)" merged.profdata
  test -s merged.profdata

  stat -c "Jar log found (%s bytes)" jarlog
  test -s jarlog

  echo "Removing instrumented browser..."
  ./mach clobber

  echo "Building optimized browser..."
  cat >.mozconfig ../mozconfig - <<END
ac_add_options --enable-lto=cross
ac_add_options --enable-profile-use=cross
ac_add_options --with-pgo-profile-path=${PWD@Q}/merged.profdata
ac_add_options --with-pgo-jarlog=${PWD@Q}/jarlog
END
  ./mach build

  echo "Building symbol archive..."
  ./mach buildsymbols
}

package_firefox-esr() {
  cd firefox-$pkgver
  DESTDIR="$pkgdir" ./mach install

  local vendorjs="$pkgdir/usr/lib/$pkgname/browser/defaults/preferences/vendor.js"
  install -Dvm644 /dev/stdin "$vendorjs" <<END
// Use LANG environment variable to choose locale
pref("intl.locale.requested", "");

// Use system-provided dictionaries
pref("spellchecker.dictionary_path", "/usr/share/hunspell");

// Disable default browser checking.
pref("browser.shell.checkDefaultBrowser", false);

// Don't disable extensions in the application directory
pref("extensions.autoDisableScopes", 11);
END

  local distini="$pkgdir/usr/lib/$pkgname/distribution/distribution.ini"
  install -Dvm644 /dev/stdin "$distini" <<END
[Global]
id=archlinux
version=1.0
about=Mozilla Firefox ESR for Arch Linux

[Preferences]
app.distributor=archlinux
app.distributor.channel=$pkgname
app.partner.archlinux=archlinux
END

  local i theme=official
  for i in 16 22 24 32 48 64 128 256; do
    install -Dvm644 browser/branding/$theme/default$i.png \
      "$pkgdir/usr/share/icons/hicolor/${i}x${i}/apps/$pkgname.png"
  done
  install -Dvm644 browser/branding/$theme/content/about-logo.png \
    "$pkgdir/usr/share/icons/hicolor/192x192/apps/$pkgname.png"
  install -Dvm644 browser/branding/$theme/content/about-logo@2x.png \
    "$pkgdir/usr/share/icons/hicolor/384x384/apps/$pkgname.png"
  install -Dvm644 browser/branding/$theme/content/about-logo.svg \
    "$pkgdir/usr/share/icons/hicolor/scalable/apps/$pkgname.svg"
  install -Dvm644 ../identity-icons-brand.svg \
    "$pkgdir/usr/share/icons/hicolor/symbolic/apps/$pkgname-symbolic.svg"

  install -Dvm644 ../$pkgname.desktop \
    "$pkgdir/usr/share/applications/$pkgname.desktop"

  # Install a wrapper to avoid confusion about binary path
  install -Dvm755 /dev/stdin "$pkgdir/usr/bin/$pkgname" <<END
#!/bin/sh
exec /usr/lib/$pkgname/firefox-esr "\$@"
END

  # Replace duplicate binary with wrapper
  # https://bugzilla.mozilla.org/show_bug.cgi?id=658850
  ln -srfv "$pkgdir/usr/bin/$pkgname" "$pkgdir/usr/lib/$pkgname/firefox-bin"

  # Use system certificates
  local nssckbi="$pkgdir/usr/lib/$pkgname/libnssckbi.so"
  if [[ -e $nssckbi ]]; then
    ln -srfv "$pkgdir/usr/lib/libnssckbi.so" "$nssckbi"
  fi

  export SOCORRO_SYMBOL_UPLOAD_TOKEN_FILE="$startdir/.crash-stats-api.token"
  if [[ -f $SOCORRO_SYMBOL_UPLOAD_TOKEN_FILE ]]; then
    make -C obj uploadsymbols
  else
    cp -fvt "$startdir" obj/dist/*crashreporter-symbols-full.tar.zst
  fi
}

_package_i18n() {
  pkgdesc="$2 language pack for Firefox ESR"
  depends=("firefox-esr>=$pkgver")
  install -Dm644 firefox-esr-i18n-$pkgver-$1.xpi \
    "$pkgdir/usr/lib/firefox-esr/extensions/langpack-$1@firefox.mozilla.org.xpi"
}

_languages=(
  'ach    "Acholi"'
  'af     "Afrikaans"'
  'an     "Aragonese"'
  'ar     "Arabic"'
  'ast    "Asturian"'
  'az     "Azerbaijani"'
  'be     "Belarusian"'
  'bg     "Bulgarian"'
  'bn     "Bengali"'
  'br     "Breton"'
  'bs     "Bosnian"'
  'ca-valencia "Catalan (Valencian)"'
  'ca     "Catalan"'
  'cak    "Maya Kaqchikel"'
  'cs     "Czech"'
  'cy     "Welsh"'
  'da     "Danish"'
  'de     "German"'
  'dsb    "Lower Sorbian"'
  'el     "Greek"'
  'en-CA  "English (Canadian)"'
  'en-GB  "English (British)"'
  'en-US  "English (US)"'
  'eo     "Esperanto"'
  'es-AR  "Spanish (Argentina)"'
  'es-CL  "Spanish (Chile)"'
  'es-ES  "Spanish (Spain)"'
  'es-MX  "Spanish (Mexico)"'
  'et     "Estonian"'
  'eu     "Basque"'
  'fa     "Persian"'
  'ff     "Fulah"'
  'fi     "Finnish"'
  'fr     "French"'
  'fy-NL  "Frisian"'
  'ga-IE  "Irish"'
  'gd     "Gaelic (Scotland)"'
  'gl     "Galician"'
  'gn     "Guarani"'
  'gu-IN  "Gujarati (India)"'
  'he     "Hebrew"'
  'hi-IN  "Hindi (India)"'
  'hr     "Croatian"'
  'hsb    "Upper Sorbian"'
  'hu     "Hungarian"'
  'hy-AM  "Armenian"'
  'ia     "Interlingua"'
  'id     "Indonesian"'
  'is     "Icelandic"'
  'it     "Italian"'
  'ja     "Japanese"'
  'ka     "Georgian"'
  'kab    "Kabyle"'
  'kk     "Kazakh"'
  'km     "Khmer"'
  'kn     "Kannada"'
  'ko     "Korean"'
  'lij    "Ligurian"'
  'lt     "Lithuanian"'
  'lv     "Latvian"'
  'mk     "Macedonian"'
  'mr     "Marathi"'
  'ms     "Malay"'
  'my     "Burmese"'
  'nb-NO  "Norwegian (Bokmål)"'
  'ne-NP  "Nepali"'
  'nl     "Dutch"'
  'nn-NO  "Norwegian (Nynorsk)"'
  'oc     "Occitan"'
  'pa-IN  "Punjabi (India)"'
  'pl     "Polish"'
  'pt-BR  "Portuguese (Brazilian)"'
  'pt-PT  "Portuguese (Portugal)"'
  'rm     "Romansh"'
  'ro     "Romanian"'
  'ru     "Russian"'
  'si     "Sinhala"'
  'sk     "Slovak"'
  'sl     "Slovenian"'
  'son    "Songhai"'
  'sq     "Albanian"'
  'sr     "Serbian"'
  'sv-SE  "Swedish"'
  'ta     "Tamil"'
  'te     "Telugu"'
  'th     "Thai"'
  'tl     "Tagalog"'
  'tr     "Turkish"'
  'trs    "Chicahuaxtla Triqui"'
  'uk     "Ukrainian"'
  'ur     "Urdu"'
  'uz     "Uzbek"'
  'vi     "Vietnamese"'
  'xh     "Xhosa"'
  'zh-CN  "Chinese (Simplified)"'
  'zh-TW  "Chinese (Traditional)"'
)
_url=https://archive.mozilla.org/pub/mozilla.org/firefox/releases/${pkgver}esr/linux-x86_64/xpi

for _lang in "${_languages[@]}"; do
  _locale=${_lang%% *}
  _pkgname=firefox-esr-i18n-${_locale,,}

  pkgname+=($_pkgname)
  source+=("firefox-esr-i18n-$pkgver-$_locale.xpi::$_url/$_locale.xpi")
  eval "package_$_pkgname() {
    _package_i18n $_lang
  }"
done

# Don't extract languages
noextract=()
for _src in "${source[@]%%::*}"; do
    case "$_src" in
      *.xpi) noextract+=("$_src") ;;
    esac
done

sha512sums=('fd69d489429052013d2c1b8b766a47920ecee62f0688505758f593b27ae66d6343b9107163749406251aedebdf836147e4d562415a811b04d7ab2ae31e32f133'
            'SKIP'
            '88509577b686c995144163538efdba3cfe1a3b01564d3823b9fb7972e64823d1d0a444372636f8d0b355c485f095df8f273a6eb5560fce4c41d4f1c0a0467f75'
            '4b53ee133a4ecaf068e240f6a05a1ebf4b788d67fe9141cc5b3561e1128907c8c3edb49bf2b24ba89daf1552f94ac48adf682dbe7dd070cffe7f78d98f2b3338'
            'b579b73176c72a5ecf36e3f63bba08fdb8041ae99d54e5cab906660fed6a9cf2311f7ca1ec1649e451cc6d5a4b1e6060b974b1d7befe9c8df3c5a89c50383c17'
            '6886cbfcaf422a853811f56077a6b29c432bfa34fdc3768e62dde52d477ce99dedda2aba542e2813343b547b350b8d39d32784e496f8d18a02f9fa0954fcc470'
            '7c374825faa131baa771bc4aa836656b1e456dd862db0d9fb52f13206c43f1162de30a0192ca023f0dc1ed98ad351a921917a6ad56ebffa4cfa3643b8210a478'
            '39069d165df48dea9047dc25dbc2ef8fd2f31249b487638f0769680da4d0a3841fa9bedfc23cdb7f4d563408914c052f388825f331b3a5104169bd79a1c49691'
            '3d90b7d4f3801e0a688e1348f00012ab7112fd401a66fc2463d9b276657061d99a940ce65168232c82e3fb123849e455610f9ea2bb10740de8208df2f8a16ba2'
            '3b63099c5868d483e533608c332247b3522308c49967e0618fe1cf618fbe986d908ce401bc16d66fb7566290f902cead6613369ce00d14ba7ec6f11737aab161'
            '85945e0692a212e1cbb92ba1a8510782362b8626d5e99cc7b61980e22235739ea956330d49fed519317688100209640920eefee974a4161d53f19a0c042ef8b2'
            'de443a0824a345f38c81f38b98c9d2bbbc801e26f0ff0f3ecdd6849cd56d13931141462f116db3f2353a1f90053495712600b96a383a612bb275eed986027455'
            '1284a7c93fff2767d302b39ac5953b8c0a43270b812e19f86692cee0e60ff6e76f3f74627283ad84cf4ab4b3d1d027947e488a7dd6564faad382e7a96775c27e'
            '134fffc2bebdf10871662e5b3fabbc19fa876e089a2fc5fa1d6969489430abc9e43ff8889311bba1f882b1ae884305c5df764a45b0a3bc90d232201f6e6d3baa'
            'df02b6e2468b3bbeadab76959b41ab90946fbd67a0c85337e2a7d90f6e2039faf898f065e2f8098df2882fcb259fb28614da435aba63610036b4e66c6d43a343'
            '48423a302cfdcae7908533f3ab72d54eaad61b82018d1989e17d1b468a5f1813a63ce39ba5f293cc9e88e17716d06833eb15464f69d7dcb210c8b88f76d2358a'
            '8ad48e0b17978fa5a1d41550dfb6a835ae1de0add646a791970e400ebb8ba43c7ebd73c7eca328592bbcb4602d62885e3359734a77c7d018558e2a37470d4697'
            '7c2f82365c95f95f426edd3a27454d3359a8b88a9bd2226904faec52b6fe2327c82034b59a0f97de7b3097fa4ef5983602d4a92e72cea85185067e03b7da9422'
            '782e6440e61d18252a50257f6e1b620a8f625b8c9476d3b3d73680a5bcad5ca8820cc78d36e9c04f67e5a14b95c009c4dcb29266c9471410ca1e655f677e7126'
            '7f5388884709cbb660232a313025ec0c3dc49d2886149302e371efbc945622eafe99b6e0531ed96821b6295baa5de6c5dfdf296cd0fa49b00d5a47d8fcfb5d86'
            '799861607fa3586542594d7690acfa30eb671f803f9b88b3113c6d282bb3934a00ab67d570024778ddf538fd01da9074f68ff0eb91af5afeff7d65a8cb90b8aa'
            '79100cb5d174e2c6ea9d030c48e8d7ce916d8f48c6900b4dbfc9843ca7fac8b2ae274c8a2f41ef19fe211cc962f3220b6acbc2d02690c7a46fe35187fc9c16f8'
            '712937007cb5933c0d7c019486cc63b31e90b6c18c7c9d5e137df5eab9ab4c25aeab704b7fed964373a5bdc8b1522db5fcde76b42a5777df33e0b0860f489214'
            'a6bcdca3e4186b3d1d4f04e40fc5b121345c347cb75571ffddf2674584dcaed85d18c783801253d0c72f9a9d172c56de8d4d55ce642e95d6ee229003b18c56b3'
            'd64604fbed8bb89459ac67d81b65ede139f5e1e6f75118eeb62c48ebe79fdca5cb92d4039f0c2535e9504a4b4307beecb9e5160dce55d0830fe261cecdd04785'
            '511b2ed01269869e7c263f8d9357e5f0c3773fd1cab0217472c44dd32446d94bfe1cc220e433c29bfefeee83d305e646c930326bf77612cb5e04e43de4795745'
            'a36fc58560607119c989cef29ba21f6d370cd958a341f0feee3984a69e6180f7b63af1df00f9003dbc731db02ddd99d80f9ae545eb182da28563ce4ac49f576d'
            'ba60c4d107f07bad3a8a2c1a46d2497fe3eb7c08d9e14f273039092aeaddf8a2293dcbc659c38d0638b136cb624d2f9867b06c4f6a97dd73bb0f06f4403c8fc4'
            '2b9689c52b431ea21a73dbeb5227b934363ba80f56d5335a05fe85b94a8beb4f73c2c7ca8f0d89fce7f4b384acf10d72c0a1b0a221fcaa986e5c61b51353c1e2'
            '9261dda6cabe7b51e0e29d41f631ea2eb8600681b12791f3e4a1793938c0a18c6fda4c12297ff8d274eaf9865bf0c65e3d187aad64b833baeda839d1d6a07813'
            '4e6ab6bdc68e44fb4224d85e8bc395c473fa9d30bc4e1bb3612ed31f2ea59838760720ad4d1345b1a4cc66f931f199be4aeb5d364e1f8c1ea2cbaadb123a6fb0'
            'b33d90f20497babdbb288aa4a048b9b4f49ab6686c64e39d81a63875438a961b97a242a6c09ea7a1a669246147dd2d123ae45c4d1396a2c0dc89e39a346ce8ca'
            'a8cb6a3ad72097092d42b376cc43305e0ca1f371b1bcd08189286c3cd5972f8b581aedbece86b0e64264ebbb59e5b3009ba383f03aa9b0e868610cdf980b1a2c'
            '8b6e3a9a430855649093ff551f510984b76cb91c5243ad056b4d7d9cd1d09b6d6170d3f7174f4665db56227786c0e54b7bb4c4659f903adaca3dc2566079a18c'
            'cacdd1618a84b21ae1e5a6b1b7a9cc7c77f6ab2a0f4a57530850561ab4d3bde17cb49abcc20b9c31638656a82ee4d22a7bce0ec34c59ec28d106b5ee43d14c29'
            'abc61e80ea2f365a9b1a0fd14e173d305d05b386c01c844e3eae14f9e279b927e5512b0d7413455f91049c98940f1529cf3095f054d46ccf8c7acccec3b2c5b5'
            'ed0777632a0626b6d200630d8d6f0892e5095c5aa5232f109cc567f5133cbafc9d747b4bd17eb2a39917d0aa5d0d6801715ba093beec02c4720589795089cf5c'
            '184e0dc3f4cba2e4ebd6fac27d1383e27b07994ce123858c43356d6000c9f873c4eb5c2648b04922394a1a1cc2c12fcbf437d7a7eaca5003fa2f133f34d69a0d'
            'cb22c21540d441c3a274d276a546f664fab3f03be5d9d9c60f57d9693bc769d3a77f215a6b4389f835948c28a779479a3f03e8ab04ffb322a9be15a1a8a9f359'
            'd75eb5c360736e9bb3a85f452e0ebbdc6ffd8ef5fc324aa395a55e0e6a85eeabd4382b6dd6693196196dc4902b9d1da19068daaa350ff96c946bffbc1705eff4'
            '694c419356872a99c86de4351a0cbd9f1b4a67afaab8a55288d54792a8e358182fd7813ae113ccc5596d2e5158337eccbe962dc93f938b45e90dfc46c5a25488'
            '67823a10f89ac9118d6e82e6a7554c4fe911bf02d923a3e1e2665f90ecf4149136d76851a7861d47e5bc4fea672b586e828f4f4288a607d73ab81658b7be586e'
            '5c99f2401f565cf609354b95af45d80f935d84d90f65d998b505e53989c73f4eec5f25859aef60846ce6b7c581d6fd7d53363314a60539b31164fafed4672cb9'
            'd7e828bc0565b75c03c4f72274cfcd13cc3dc77639505010c4925a1ba2d7514a94062b802b46a0469ee033ca60da38dd4a0188cc7ab71f8b43a2e9ffd546319f'
            '3a3a8a263004ac537e216362d5d402aa58ea74e43a4c546683b5bc5529d00df5f032373f799e307deb397b1e0c309073e9aaf826826213e3ebbf7641bcf79688'
            '01b55c052813a53788806c157b15b219b7831e258ff0c547b1da79e8f2af1753a3b36bfbf49dadee6c8fa272f942ea72816a346bf26454b58e451fcd42e634ab'
            'cecefa32bc1d52fc3d330f870173b7fe906681c5bfed6b465cf36291a2dd51af229d6bae1c7a59f6655bcb0ee470e381f47602f834e595d92555f316cc26b8ab'
            'b3f4c6aaffb69d316bfba893563ebea3c71f818e1c81b4a5b873b48a5891d34d042cedb6cba6e34c9dde98a1040cb05015e51b116a525144dc13e2af8c0aab3e'
            '84c3141b76a0a95c1e4df21a56f8687d568fc00d5e63ada95fe06ddd5a0d794b3ba8430b37c03732c2736fbce4a3b40e2860ce8eadd6d74f56c446ce950d093c'
            'a9617431316de400435af7d7c5860239c4b0d75883ff326264506e7d31662b7be02f38a582a04cce81a378a9af7bc8da6dd8090b453e1f86d92d3239be531559'
            'a68be69300c55cbc779f6d040fd28b6f4511584a8c9b49fe1fec57c501b81825fb377a7147bbd76098c379ad5050e74aebed9e4ba3908417c056d6143a9b92ba'
            'b4ed164a5a7e294ef1618e1ca5817131e881b7936fa76fa65362d688a8be198957884bd4c974d1ffe32896079a1b1bbe17b2c9596cf4ce69e6aa1b3674bf26cb'
            '9d410bf3711876a7a4145ed55685b35140dd60562d60693ba98c1e6acf679266c33c6700dba7117047f12509f41549c24899b293c9fa938639895e780bdacec1'
            '80c0c19eb7612fd2ad4b5642639f208e98e44294bc68bcd1d0c93806585bfe1e2dfd8dac1ee543a15e3369851bdba7053dec2adcb92065c75332d587e654f611'
            '59d6707da0fa7e401100173708474d1333a77c1d32d645b44c6cafdb629100fb45092d2438dbf8f26bf1549b695714de31d126fd8cc7d5ead3f3c8db48f56c7c'
            '5e00899ff8813a3a3698ab068fc92b62c1f24e8cc5ae112adb3821a483a2ed3940ac0145d160899023a6adff5ada3fe76d2c98cc6c2931809ed26961783fa703'
            '016647180407fc6bcf92d915260ad57cd7054fd44d7946e6d90910c3aace23742a64685392af47488a5c479e397ac5fa3354b5f3f2c4555edd7f0c265fefd592'
            '5e3536cbee93040fb39409fc78530343555bfededd3885a3088965891f31b478a8bbc5c13ab91b8eca9c5beb968f4c6b589a1d5fa9d7884c848590be42f79eed'
            '1f9af806923e2a1a5e313a2c5ccac55061c8e89e0b50f0cc7c0385f5dbd2619037a7b48a8e59a806926fac863fced3646251a0c72f3c318575c07bf77dcc1dbc'
            '4e9f30d2b14441d739f9a46f6788d1ede20801406a05032122b75ad60c067ad3f2e499e2289b6e46f97d3581a46a6d7d05706e78151e2beec8f33af252368b0f'
            '98d2ef78d63bccfe4297f4c03b8f779a719114338fdf44584b4fa208c86ee2c25d4b9edc96b905b3b1df37ac6dc7fe231d6aabef6eb45ce25d2bf9c69eb916cc'
            'e54c373d97adcd08906bf3af8ac9523bb4637e8424b3b6824c0bfe51d3469f5530120adcbeafd6f8a469d65c68057d2f8ebf4e07a3fbc66b0a426d282554fc33'
            'eff03fa6bc7e0a6b6a59a0997cf487b25d45010c5f797160a0c1645c6812cfdd73dda22d3a58acac9e6abf5b755acb3ed635b96c06d4763be1a1d3579dcf1a43'
            '67a840bd3c7f01d7fa64ef5afddef2919fab37f4c8c3090e6669233946975bde09060fb2c452a10bda620636defb74f2816309a317b3354895b89ef7a258675c'
            '36bd2ef7b0ac2813430247b6d0b922eb7de25af26b0776ffae92c2362f1fc1b6c60d5ee3076d3f8c47d1cd097326b464996b08687a7a9d2fb35f0392cc26b9ba'
            '4a4bba0746607fd7cf7844f78c98b4026636d9a99f5e0191c68871c93ddab94da730927da183eeae49e07be5f763ddeb0b9c075eb631d1db1ac240eaaac4dffd'
            '421c2c36c85850fb61da9c65ae61ea0bdb2273440d472b63511444c4a4345383908e68e95b22b7297f31efc9e2ed9fb816e31618d7929772dc0a528f74c1f033'
            '622d3e6c131aebe3c7aa303fd0007b2ade21ee40128a5d7f7c84d22a59ab53391506a63a7c46efb29ad9e2094352d0a33b390facf34c7457e44c72450f0e08a6'
            'ce6892bb26de06a01f7fdfc45650e6308579c7f2863f9836b57573db7939d7fdd0a27c93f79d6470043ac227fdb61c84de1d7dfefe8ab839e9e3a30b661fbcf6'
            '3980ebdcbd48b96d08dedab50e4d6c28e0006601ccc64f9306b89efff5a4d6fd6cbae4132160dc8fd21d7aec66de4d73fb1b456f87ae19d533a6b72871e511e9'
            'cbe25214852054e08b41af418e5635b20191bd997730c2c096c7ca1cee92882277238ffb8aecc1d406680c2e9fc03c895b20af7cea8ab379958733d578cac93d'
            '683ff16e9f014f594bf2d8ac4feda163f4caca6a0bdf02dd3068600fdc26db0a058c1d5f2fd501668ba59d9d9124cb3026f7eb34761f3235b01e9d5d24930665'
            'ccb7045cb426cc3c372a4e698a752cefd19e6c29d163e1a94b960344b1378b4d73801088488998dc687b36def27de399d7a1f6f34f521402d167a172679aa257'
            'e4392439b229107db88684aa11a47f17d14e24c69db84dcd4ab30ae20119ee5d63784ba0206c19a0326d7a3f66d44afbf808ff6f8d93f3ddef358cb28967bb37'
            'f74438ccf2160196373eddfd4d8839a10ab2ead100f0a05dc9f43bc186b484b79e16eed319c84afa935d4ebb4027094766d5e993ee27e67a6e236497c062b6e1'
            'ac5cec8ca29a4a0424f0c3be1335bb8151291c98790f2c76550c89906f6c0e18d9ad9bb5ead8089148bd9dec92ae40aae753fa083d65493b8a35eb7b6c78e88a'
            'ea4841eba5080cc947bc5ef582d22b46aeb747e8ae1013f6b45b0a961bd9a8456f1e3772e9fc8d8a7d827f2c1b215c4239743716114139b6dff05e01712dfdc8'
            '16d4ef571c5e3922889ad21186cf127c18ed523115476e465882269975cf130e42b9374e79069f225f14be2b391e79e4108dcb541265f6eb590550337655800d'
            '92917d31ad3dfb5b28a571edfa405a3ea530951e2bc2ec32adb149b7c52b7cb8a3872c9ec7e1478da748810ca20c56901726785bd95256d2a65cc40d4f540426'
            'b9faad2a10495334d96eab6502607f7246c3a21b214f80708b7e366747c254289a47761ab415098f4f38fa9ee1243776f91caf7d55b3628a367b5220aa68d1c6'
            'b54221e41b7d46951b127eb0c7398765040b044b86afee4dfb5cf858487639de7fbdca4593cc0d3ef8ce52dd42a4dcc5308e2b6b4118efdbe9b952b8aa58e141'
            'c6d3c0a04ba479baddc3664470d637e4477fb951d10feeb811ddaf536109285e6ce99b3a5ac934ca948ca60afce37222d467ebd365712c88f4886810499ef0e0'
            'eec6e78b7e6da6841401ee90e55f92e64aad166c82e08b6a1b069d19215987ddaa0469dd8821e0fad6db0e5fbbf807c5451fb5b7d44838c87e83ba8cd1696e7e'
            'f4fac9fc17d4d51aec6ad23f3abf4d15606fd2f33bf63dc63d1c15abe818018b72ebb66929d592a009d6b782a6189cdc8e440593afb79be602fb4bc3d84fe245'
            '907ea3f434d2b78e3d62373aa0b12205a6647cbd431e6b92e908d21e20eebec921a82076e3f96e86ee0c3ccf2d57101795cac3724069b9c20698e5f84bb6b329'
            '80102bc8c2cc9ca591a7952637efc2061e4b0737725d43acf4d5b1720d3b7e1bd73f15bf37ae5a4ce9e7eec0593bfae6dd961bff2555f00154f9bae6ec8459d8'
            '862a62ab1b3ca497305085bab269bf47f139be51213aa648689189e739a0fa9ee5687d9c2f54b5201314dea51a5e9ecc5ad4f888eb4028d7aa491aaec055a1a4'
            '1925ff7ca77d873b721af1b00105aa5972538949c930d20019f5b981807fd366061ae602b8b411866c121ce742e0d7876c82da4ffa695a1991dfafa9956708dd'
            '0594c0c7df2d1586a965388ca0411b8cd4073e156befd83940c4e76959ffedae97f4fc312b3ff2028ce70ce2bfb24c59416157f04619cdadbf992b68ce3c347d'
            'f64ede8e879e301b9dc8028695b8c72c79b3fa958dd0e24ee829db1a43a6c3a87c4612463705dd65095df41e21aa57178e5a41df2bb1c8576e0c14674671b274'
            '5779ffd7dc67c007722c1b211f3801ec0a76069f256c36399b016f66302fabe899ebfcbd85e196c62bff744f30d62c84f1ff66206a813d87ff5be12f5666c08d'
            '2e4d5193f7c2aa9d19e9de62aede42b03f50e7f5fa1cd4461e9554c2fac9b49f7e58c6f8043c840571a407d7f5e252bfe0e15b0e8546b6ea2b50ffeadaad9823'
            '5f4ad0d618cdde86a45a270090d696230ead0d13b2edd945d27c19c3adc4d8c1a5176df8a7ef3e8b9fe1efd59d316b30b04bf765c3a5e03e3eba4a45d90ce33b'
            'a4a4ff3d9ae62496b6c1a4ad47a3a8a3d03fb99247ce37b2ad95a8c9f19afba6a8b63bf985a20b6aabbee74763d57803ffe27dc0ab86f737b36a7d2f910f1be3'
            '9a69261c71ddacdc570365847674082439b40e17957ce9509ae226c80ac2c5a117b9a69fb5d11a703de2695db75e427c7be085b4303bdefdcf1265890818f677'
            'a6cd0567c57da68250ab29c240675c9cd3299a078e09057e8bb04d5287c17557582fc16c856ce9c10b5c343152528014571dc225e8b84e4c4d16f4135aca0707'
            '118c5f40b48449e61fd06a9f4ffc39c5203484148e18285d6c7b22fac3429531eee1788ce2211502b4d208852e0cb6d6a604620df9c7761bae40fb38997483db'
            '285e1daffc102e8a25b2d74c0fdcd063dc5542819a6b651b1644e702b0848dafc696facdcedd18c506cd4354f7f501cdc26f68336f66b0bbc710dcbc659a7bdc'
            '59d2d7877d539be879777ac8f48d6e98dee4eefe4cd92c1f1363e7cd7e1a909863d57109b0c47e159a55678677285380b7755e0d3c9f06cdc7eec7cbdb03d098'
            'ab6adcc8f1071aacda8452b0d58d26ee8f1072189b7459f9191e3a4c1b4a9f864ca3483fe6bf9f642f962d5f223d5f11364173349519a7ce7a4c7451c08d27cf'
            '326ae088155fe30964ce58b564dfc0879d5f94b14c31173194e424f3a2862a4619d76852118403ac92ed61581e5419395f219cdb8bc9a3056beded03d3b83d96')

# vim:set sw=2 et:
