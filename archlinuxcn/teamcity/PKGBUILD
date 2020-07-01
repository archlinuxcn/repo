# Maintainer: Xuanwo <xuanwo@archlinuxcn.org>
# Contributor: Mastacheata <benedikt "at" xenzilla "dot" de>
# Contributor: Yegorius <yegorius@domic.us>

pkgname=teamcity
pkgver=2020.1.1
pkgrel=2
pkgdesc='Continuous integration server from JetBrains'
arch=('any')
url="http://www.jetbrains.com/teamcity/"
license=('custom:JetBrains TeamCity')
depends=('java-runtime-headless')
install="$pkgname.install"
source=('https://download.jetbrains.com/teamcity/TeamCity-2020.1.1.tar.gz'
        'teamcity-agent.service'
        'teamcity-server.service'
        'teamcity-sysusers.conf'
        'teamcity-tmpfiles.conf'
        'teamcity.conf')
sha256sums=('bd6f6d61c6414a1f2de726cac69d7080e90a23d5b828d0e68a3ce5aa4e0851cc'
            'b66ca4d1963138be8f88c4bf7cf358b1bf096711a618f2f501ce9805fafdbb20'
            '59e68ab2524e66f7c074ac4215a0449ed9242160946ef3364d378e015525e749'
            'b74128251ac1943ff48956bb2849731423b712d078ec76f1a8959532f0161c91'
            'f6d9b522a2730f9e6b6e044cb6f76fa31767788a4f7f21ab4e751dc1f88f6143'
            '7d140cac121eb725990edc2323682a0dbaeb15393b8fda10fb043af994843248')
options=('!strip')

package() {
  mkdir -p "$pkgdir/usr/share/licenses"
  mkdir -p "$pkgdir/var/lib/teamcity/buildAgent/"{system,temp,work}
  mkdir -p "$pkgdir/opt/teamcity"

  install -Dm644 "$srcdir/teamcity-agent.service" "$pkgdir/usr/lib/systemd/system/teamcity-agent.service"
  install -Dm644 "$srcdir/teamcity-server.service" "$pkgdir/usr/lib/systemd/system/teamcity-server.service"
  install -Dm644 "$srcdir/teamcity.conf" "$pkgdir/etc/conf.d/teamcity"
  install -Dm644 "$srcdir/teamcity-sysusers.conf" "$pkgdir/usr/lib/sysusers.d/teamcity.conf"
  install -Dm644 "$srcdir/teamcity-tmpfiles.conf" "$pkgdir/usr/lib/tmpfiles.d/teamcity.conf"

  cp -R "$srcdir/TeamCity"/* "$pkgdir/opt/teamcity"
  ln -s /opt/teamcity/licenses "$pkgdir/usr/share/licenses/teamcity"
  sed -e 's|=\.\.|=/var/lib/teamcity/buildAgent|g' -i "$pkgdir/opt/teamcity/buildAgent/conf/buildAgent.properties"

  rm "$pkgdir/opt/teamcity/bin/"*.{bat,cmd,exe}
  rm "$pkgdir/opt/teamcity/buildAgent/bin/"*.{bat,plist,dist}
  rm "$pkgdir/opt/teamcity/buildAgent/bin/mac.launchd.sh"
}
