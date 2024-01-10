# Maintainer: Sebastian 'gonX' Jensen <gonx@gonx.dk>
# Contributor: LavaDesu <me@lava.moe>
pkgname=opentabletdriver
_pkgname=OpenTabletDriver
_lpkgname=opentabletdriver
_spkgname=otd
pkgver=0.6.3.0
pkgrel=5
pkgdesc="A cross-platform open source tablet driver"
arch=('x86_64')
url="https://opentabletdriver.net"
license=('LGPL3')
depends=('dotnet-runtime-6.0' 'gtk3' 'libevdev')
optdepends=('libxrandr: x11 display querying support' 'libx11')
makedepends=('dotnet-sdk>=6.0')
conflicts=('digimend-kernel-drivers-dkms-git' 'digimend-drivers-git-dkms' 'digimend-kernel-drivers-dkms' 'digimend-kernel-drivers')
install="notes.install"
# unified binary dotnet releases break when stripped see https://github.com/dotnet/runtime/issues/54947
options=('!strip')
source=("OpenTabletDriver-$pkgver.tar.gz::https://github.com/OpenTabletDriver/OpenTabletDriver/archive/v$pkgver.tar.gz"
        "$_lpkgname.desktop"
        "notes.install"
        )

sha256sums=('7c38d92bb8176eead8f58d84532abd49e915254208c568a5618c92c093c1fdd0'
            '4399359bf6107b612d10aaa06abb197db540b00a973cfec64c2b40d1fbbb2834'
            '35f48af6cb7ce0d53fb4efd1a932937f806d55f520e73ac99292e49d7d7e33fd')

_srcdir="OpenTabletDriver-$pkgver"

# TODO: use eng/lib.sh
#prepare() {
#    cd "$srcdir"
#    source eng/lib.sh
#}

build() {
    export DOTNET_CLI_TELEMETRY_OPTOUT=1
    export DOTNET_SKIP_FIRST_TIME_EXPERIENCE=true

    cd "$srcdir/$_srcdir"

    if check_option "strip" y; then
        EXTRA_OPTIONS="/p:DebugType=None /p:DebugSymbols=false"
    fi

    ./eng/linux/package.sh -- $EXTRA_OPTIONS

    ./generate-rules.sh > 70-$_lpkgname.rules
}

package() {
    cd "$srcdir"

    sed -i "s/OTD_VERSION/$pkgver/" "$_lpkgname.desktop"

    install -Dm 644 -o root "$_srcdir/70-$_lpkgname.rules" -t "$pkgdir/usr/lib/udev/rules.d"
    install -Dm 644 -o root "$_srcdir/$_pkgname.UX/Assets/$_spkgname.png" -t "$pkgdir/usr/share/pixmaps"

    install -Dm 755 -o root -t "$pkgdir/usr/bin" \
                    "$_srcdir/eng/linux/Generic/usr/bin/$_spkgname" \
                    "$_srcdir/eng/linux/Generic/usr/bin/$_spkgname-daemon" \
                    "$_srcdir/eng/linux/Generic/usr/bin/$_spkgname-gui"

    install -Dm 755 -o root -t "$pkgdir/usr/lib/$_lpkgname" \
                    "$_srcdir/dist/$_pkgname.Console" \
                    "$_srcdir/dist/$_pkgname.Daemon" \
                    "$_srcdir/dist/$_pkgname.UX.Gtk"

    install -Dm 644 -o root "$_srcdir/eng/linux/Generic/usr/lib/systemd/user/$_lpkgname.service" -t "$pkgdir/usr/lib/systemd/user"
    install -Dm 644 -o root "$_srcdir/eng/linux/Generic/usr/lib/modprobe.d/99-$_lpkgname.conf" -t "$pkgdir/usr/lib/modprobe.d"
    install -Dm 644 -o root "$_srcdir/eng/linux/Generic/usr/lib/modules-load.d/$_lpkgname.conf" -t "$pkgdir/usr/lib/modules-load.d"
    install -Dm 644 -o root "$_lpkgname.desktop" -t "$pkgdir/usr/share/applications"
    install -Dm 644 -o root "$_srcdir/docs/manpages/$_lpkgname.8" -t "$pkgdir/usr/share/man/man8"
}
