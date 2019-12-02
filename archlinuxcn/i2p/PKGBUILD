# Contributor: skydrome <skydrome@protonmail.com>
# Maintainer:  skydrome <skydrome@protonmail.com>

# uncomment if you do not want to build all language translations
#export LG2=en

pkgname=i2p
pkgver=0.9.44
pkgrel=1
pkgdesc="A distributed anonymous network"
url="https://geti2p.net"
license=('GPL2')
arch=('any')
depends=('java-runtime>=8' 'java-service-wrapper')
makedepends=('java-environment>=8' 'ant')
#optdepends=('gtk2: for rrd graphs')
conflicts=('i2p-bin' 'i2p-dev')
backup=('opt/i2p/wrapper.config')
install='i2p.install'
options=(!strip)

# https://geti2p.net/en/get-involved/develop/release-signing-key
# https://geti2p.net/_static/zzz.key.asc
validpgpkeys=('2D3D2D03910C6504C1210C65EE60C0C8EE7256A8')

#_url="https://download.i2p2.de/releases/${pkgver}"
_url="https://launchpad.net/i2p/trunk/${pkgver}/+download"

source=("${_url}/i2psource_${pkgver}.tar.bz2"{,.sig}
        'i2prouter.service' 'i2p.tmpfiles' 'wrapper.config' 'router.config'
        'i2prouter.bash' 'i2prouter.sh')

sha256sums=('9f03a636e2dc7e25455fb75869b3a8313fd177d231e056b0556159efec4d6d9d'
            'SKIP'
            '644b771ec7f5db3efab3206bf1f896566cdb00d410a54608fda85bdb4c2ad876'
            'df26da04c8415ac24ec73b0dd08d3459a8964553bb77e5da5ab9833b0a31d865'
            '5d134ee5bc614b54ec48de7c5214f6dbe08abcfab7d286c5b1c7616e39b478ed'
            '7a4688db826c3dddb762976cd8c9a5d465255c3577069243d8e5af941a4126e2'
            '7a19b9f90c8792460fd58e8b8aa435a065e34d29a942479850472510e9d3078a'
            'b5f1a5bb354552acebe2857b9579410f7fd589f2f7d6b12fbbfe4127a2d33fd8')

# prepare() {
#     cd "$pkgname-$pkgver"
# }

build() {
    cd "$pkgname-$pkgver"
    export JAVA_HOME="${JAVA_HOME:-/usr/lib/jvm/default}"

    ant -Dfile.encoding=UTF-8 \
        -Djavac.compilerargs=-Xlint:-options \
        -Dbuild.reproducible=true \
        -Djavac.version=8 \
        preppkg-linux-only
}

package() {
    cd "$pkgdir"

    install -dm755 "usr/bin"
    install -dm755 "opt/i2p"

    cp -r "$srcdir/$pkgname-$pkgver"/pkg-temp/* "opt/i2p"

    install -Dm644 "$srcdir/i2prouter.service" "usr/lib/systemd/system/i2prouter.service"
    install -Dm644 "$srcdir/i2p.tmpfiles"      "usr/lib/tmpfiles.d/i2p.conf"
    echo 'u i2p - "I2P Router" /opt/i2p /bin/sh' |
    install -Dm644 /dev/stdin                  "usr/lib/sysusers.d/i2p.conf"

    install -Dm644 "$srcdir/router.config"     "opt/i2p/router.config"
    install -Dm644 "$srcdir/wrapper.config"    "opt/i2p/wrapper.config"
    install -Dm755 "$srcdir/i2prouter.sh"      "opt/i2p/i2prouter"

    install -Dm644 "$srcdir/i2prouter.bash"    "usr/share/bash-completion/completions/i2prouter"
    install -Dm644 "$srcdir/$pkgname-$pkgver/installer/resources/bash-completion/eepget" \
                                               "usr/share/bash-completion/completions/eepget"

    install -Dm644 "opt/i2p/man/eepget.1"      "usr/share/man/man1/eepget.1"
    install -Dm644 "opt/i2p/LICENSE.txt"       "usr/share/licenses/i2p/LICENSE"
    mv opt/i2p/licenses/*                      "usr/share/licenses/i2p/"

    ln -s /opt/i2p/{eepget,i2prouter} "usr/bin/"
    chmod +x opt/i2p/{eepget,i2prouter}
    chmod -x opt/i2p/*.config

    sed -i opt/i2p/eepget \
        -e 's:%INSTALL_PATH:/opt/i2p:g'

    # dont automatically start the webserver (3) or open a webbrowser (4)
    sed -i opt/i2p/clients.config \
        -e "s:clientApp.3.startOnLoad=.*:clientApp.3.startOnLoad=false:" \
        -e "s:clientApp.4.startOnLoad=.*:clientApp.4.startOnLoad=false:"

    rm -r opt/i2p/{osid,postinstall.sh,runplain.sh,INSTALL-headless.txt,LICENSE.txt,licenses,man,lib/wrapper*}
}
