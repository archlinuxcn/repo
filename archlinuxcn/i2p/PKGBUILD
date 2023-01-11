# Contributor: skydrome <skydrome@protonmail.com>
# Maintainer:  skydrome <skydrome@protonmail.com>

# uncomment if you do not want to build all language translations
#export LG2=en

pkgname=i2p
pkgver=2.1.0
pkgrel=1
pkgdesc="A distributed anonymous network"
url="https://geti2p.net"
license=('GPL2')
arch=('any')
depends=('java-runtime>=17' 'java-service-wrapper')
makedepends=('java-environment>=17' 'ant')
#optdepends=('gtk2: for rrd graphs')
conflicts=('i2p-bin' 'i2p-dev')
backup=('opt/i2p/wrapper.config')
install='i2p.install'
options=(!strip)

# https://geti2p.net/en/get-involved/develop/release-signing-key
# https://geti2p.net/_static/zzz.key.asc
validpgpkeys=('2D3D2D03910C6504C1210C65EE60C0C8EE7256A8')

_url="https://files.i2p-projekt.de/${pkgver}"
#_url="https://launchpad.net/i2p/trunk/${pkgver}/+download"

source=("${_url}/i2psource_${pkgver}.tar.bz2"{,.sig}
        #"https://download.db-ip.com/free/dbip-country-lite-$(date +%Y-%m).mmdb.gz"
        'i2prouter.service' 'i2p.tmpfiles' 'wrapper.config' 'router.config'
        'i2prouter.bash' 'i2prouter.sh' 'chromium-i2p.sh'
        #upstream.patch::'https://github.com/i2p/i2p.i2p/commit/6c0e18d3.patch'
)

sha256sums=('83098c1277204c5569284b32b37ef137656b27bfe15ef903eca2da7c269288d1'
            'SKIP'
            '644b771ec7f5db3efab3206bf1f896566cdb00d410a54608fda85bdb4c2ad876'
            'fc30dd32f48fe1c93bf36c8297ca48203a1479e4e221ebe62c57cf3c3c0347d3'
            'e3a85d8992a09e8f57498b1eba0aef758ceffdb944d296528e8c5cec970becd9'
            '90f202e5b66d5a5b425522b409e71fb892d34c534e32ce2d6fe5284015cacf94'
            '7a19b9f90c8792460fd58e8b8aa435a065e34d29a942479850472510e9d3078a'
            '8d39f080c7a2e49226db3a785f3e18583159ef2f95e1ab467fd9984c4e38c9f5'
            'a7076156703e2b949331e450455813432caeb4e5712f1c7b668974eb06a69fb9')
prepare() {
    cd "$pkgname-$pkgver"
    #patch -Np1 -i ../upstream.patch ||true
    #cp -f ../dbip-country-lite-$(date +%Y-%m).mmdb.gz installer/resources/GeoLite2-Country.mmdb.gz
}

build() {
    cd "$pkgname-$pkgver"
    export JAVA_HOME="${JAVA_HOME:-/usr/lib/jvm/default}"

    ant -Dfile.encoding=UTF-8 \
        -Djavac.compilerargs=-Xlint:-options \
        -Dbuild.reproducible=true \
        -Djavac.release=17 \
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
    install -Dm754 "$srcdir/i2prouter.sh"      "opt/i2p/i2prouter"
    install -Dm755 "$srcdir/chromium-i2p.sh"   "opt/i2p/scripts/chromium-i2p"

    install -Dm644 "$srcdir/i2prouter.bash"    "usr/share/bash-completion/completions/i2prouter"
    install -Dm644 "$srcdir/$pkgname-$pkgver/installer/resources/bash-completion/eepget" \
                                               "usr/share/bash-completion/completions/eepget"

    install -Dm644 "opt/i2p/man/eepget.1"      "usr/share/man/man1/eepget.1"
    install -Dm644 "opt/i2p/LICENSE.txt"       "usr/share/licenses/i2p/LICENSE"
    mv opt/i2p/licenses/*                      "usr/share/licenses/i2p/"

    ln -s /opt/i2p/{eepget,i2prouter} "usr/bin/"
    chmod +x opt/i2p/eepget

    sed -i opt/i2p/eepget \
        -e 's:%INSTALL_PATH:/opt/i2p:g'

    # dont automatically start the webserver(3) or open a webbrowser(4)
    sed -i opt/i2p/clients.config \
        -e "s:clientApp.3.startOnLoad=.*:clientApp.3.startOnLoad=false:" \
        -e "s:clientApp.4.startOnLoad=.*:clientApp.4.startOnLoad=false:"

    rm -r opt/i2p/{osid,postinstall.sh,runplain.sh,INSTALL-headless.txt,LICENSE.txt,licenses,man,lib/wrapper*}
}
