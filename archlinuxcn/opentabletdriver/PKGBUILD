# Maintainer: Sebastian 'gonX' Jensen <gonx@gonx.dk>
# Contributor: LavaDesu <me@lava.moe>
pkgname=opentabletdriver
_pkgname=OpenTabletDriver
_lpkgname=opentabletdriver
_spkgname=otd
pkgver=0.6.2.0
pkgrel=1
pkgdesc="A cross-platform open source tablet driver"
arch=('x86_64')
url="https://opentabletdriver.net"
license=('LGPL3')
depends=('dotnet-runtime-6.0' 'dotnet-host>=6.0' 'gtk3' 'libevdev')
optdepends=('libxrandr: x11 display querying support' 'libx11')
makedepends=('dotnet-sdk>=6.0')
install="notes.install"
# unified binary dotnet releases break when stripped see https://github.com/dotnet/runtime/issues/54947
options=('!strip')
source=("OpenTabletDriver-$pkgver.tar.gz::https://github.com/OpenTabletDriver/OpenTabletDriver/archive/v$pkgver.tar.gz"
        "$_lpkgname.desktop"
        "notes.install"
        )

sha256sums=('56fd77cbe04d667a05162f01e5bf0e3b246c102465ef8c05560795e6b2d06c20'
            '4399359bf6107b612d10aaa06abb197db540b00a973cfec64c2b40d1fbbb2834'
            'c6f4cab31f62c8b4e34fff74961cd37a68bc486d14b1400638335ee59b0ebc83')

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

    ./generate-rules.sh
}

package() {
    cd "$srcdir"

    sed -i "s/OTD_VERSION/$pkgver/" "$_lpkgname.desktop"

    install -Dm 644 -o root "$_srcdir/bin/99-$_lpkgname.rules" -t "$pkgdir/usr/lib/udev/rules.d"
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
    install -Dm 644 -o root "$_lpkgname.desktop" -t "$pkgdir/usr/share/applications"
    install -Dm 644 -o root "$_srcdir/docs/manpages/$_lpkgname.8" -t "$pkgdir/usr/share/man/man8"
}
