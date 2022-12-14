cd "$(dirname "$0")"

difff="$(git diff)"

eval $(cat PKGBUILD| grep -P '^_pkgname=')
eval $(cat PKGBUILD| grep -P '^pkgrel=')

ver="$(curl https://releases.mozilla.org/pub/${_pkgname}/releases/ | sed -rn 's/([^0-9]*)([0-9]*\.[0-9]*?(\.[0-9]*)).*/\2/p' | sort -V | tail -n1)"
sed -r "s/(pkgver=)(.*)/\1$ver/" -i PKGBUILD

#rm -rf debian
#curl "$(curl https://packages.ubuntu.com/bionic/firefox | grep debian | cut -f2 -d \" | tail -n1)" |
# unxz |
# tar xf -
#cp `find debian/patches/ | grep -v 'armh\|s390\|ppc\|386\|ubuntu'` .
#rm -rf debian

makepkg --printsrcinfo > .SRCINFO
ver_msg="autohook $ver"

[ -z "$(git diff)" ] && [[ ! "$1" == "force" ]] && exit
git commit -am "$ver_msg"

build() (
  rm -rf 'home:nicman23'
  osc co home:nicman23 ${_pkgname}-appmenu-bin
  cp `git ls-tree -r master --name-only | grep -Pv '^\.'` home:nicman23/${_pkgname}-appmenu-bin/
  sed "s/PKGVER/${ver}/g" _service \
   > home:nicman23/${_pkgname}-appmenu-bin/_service
  sed 's/makedepends=(/makedepends=( acl adobe-source-code-pro-fonts adwaita-cursors adwaita-icon-theme alsa-lib alsa-topology-conf alsa-ucm-conf aom archlinux-keyring argon2 at-spi2-core attr audit autoconf autoconf2.13 automake avahi base bash binutils bison brotli bzip2 c-ares ca-certificates ca-certificates-mozilla ca-certificates-utils cairo cantarell-fonts cbindgen clang compiler-rt coreutils cryptsetup curl dav1d db dbus dbus-glib dconf debugedit default-cursors desktop-file-utils device-mapper diffutils duktape dump_syms e2fsprogs expat fakeroot ffmpeg file filesystem findutils flac flex fontconfig freetype2 fribidi gawk gc gcc gcc-libs gdbm gdk-pixbuf2 gettext giflib git glib-networking glib2 glibc gmp gnu-free-fonts gnupg gnutls gpgme graphite grep groff gsettings-desktop-schemas gsm gtk-update-icon-cache gtk3 guile gzip harfbuzz hicolor-icon-theme hidapi hiredis http-parser hwdata iana-etc icu imake inetutils iproute2 iptables iputils iso-codes jack2 jansson json-c json-glib kbd keyutils kmod krb5 l-smash lame lcms2 less libarchive libass libassuan libasyncns libavc1394 libbluray libbpf libbs2b libcap libcap-ng libcloudproviders libcolord libcups libdaemon libdatrie libdrm libedit libelf libepoxy libevent libffi libfontenc libgcrypt libgit2 libglvnd libgpg-error libice libidn2 libiec61883 libisl libjpeg-turbo libksba libldap libmfx libmnl libmodplug libmpc libnetfilter_conntrack libnfnetlink libnftnl libnghttp2 libnl libnsl libogg libomxil-bellagio libp11-kit libpcap libpciaccess libpng libproxy libpsl libpulse libraw1394 librsvg libsamplerate libsasl libseccomp libsecret libsm libsndfile libsoup3 libsoxr libssh libssh2 libstemmer libsysprof-capture libtasn1 libthai libtheora libtiff libtirpc libtool libunistring libunwind libusb libuv libva libvdpau libverto libvorbis libvpx libwebp libx11 libxau libxcb libxcomposite libxcrypt libxcursor libxdamage libxdmcp libxext libxfixes libxfont2 libxft libxi libxinerama libxkbcommon libxkbfile libxml2 libxmu libxrandr libxrender libxshmfence libxss libxt libxtst libxv libxxf86vm libyaml licenses linux linux-api-headers lld llvm llvm-libs lm_sensors lz4 lzo m4 mailcap make mesa mkinitcpio mkinitcpio-busybox mpfr nano nasm ncurses nettle nodejs npth nspr nss ocl-icd opencore-amr openjpeg2 openssl opus p11-kit pacman pacman-mirrorlist pam pambase pango patch pciutils pcre pcre2 perl perl-error perl-mailtools perl-timedate pinentry pixman pkgconf popt procps-ng psmisc python rav1e readline ruby ruby-abbrev ruby-base64 ruby-benchmark ruby-bigdecimal ruby-bundledgems ruby-bundler ruby-cgi ruby-csv ruby-date ruby-delegate ruby-did_you_mean ruby-digest ruby-drb ruby-english ruby-erb ruby-etc ruby-fcntl ruby-fiddle ruby-fileutils ruby-find ruby-forwardable ruby-getoptlong ruby-io-console ruby-io-nonblock ruby-io-wait ruby-ipaddr ruby-irb ruby-json ruby-logger ruby-minitest ruby-mutex_m ruby-net-http ruby-open-uri ruby-power_assert ruby-psych ruby-racc ruby-rake ruby-rdoc ruby-reline ruby-rexml ruby-ruby2_keywords ruby-stdlib ruby-stringio ruby-test-unit ruby-time ruby-tmpdir ruby-uri rubygems rust sdl2 sed shadow shared-mime-info speex speexdsp sqlite srt sudo svt-av1 sysfsutils systemd systemd-libs systemd-sysvcompat tar tcl texinfo tk tpm2-tss tracker3 tzdata unzip util-linux util-linux-libs v4l-utils vid.stab vmaf vulkan-icd-loader wasi-compiler-rt wasi-libc wasi-libc++ wasi-libc++abi wayland which x264 x265 xcb-proto xkeyboard-config xorg-fonts-encodings xorg-server-common xorg-server-xvfb xorg-setxkbmap xorg-xauth xorg-xkbcomp xorg-xrandr xorgproto xvidcore xz yasm zimg zip zlib zsh zstd /g' PKGBUILD > home:nicman23/${_pkgname}-appmenu-bin/PKGBUILD
  cd home:nicman23/${_pkgname}-appmenu-bin/
  osc add *
  osc commit -m "$ver_msg"
  [ -z "$difff" ] || osc rebuild
  osc results -w
)

build && git push || exit 1

sleep 30m
[ -e ${_pkgname}-appmenu-bin ] || git clone ssh://aur@aur.archlinux.org/${_pkgname}-appmenu-bin.git
cd ${_pkgname}-appmenu-bin
sed "s/^pkgver=.*/pkgver=${ver}/g" -i PKGBUILD
sed "s/^pkgrel=.*/pkgrel=${pkgrel}/g" -i PKGBUILD

makepkg --printsrcinfo > .SRCINFO
git commit -am "$ver_msg"
git push
