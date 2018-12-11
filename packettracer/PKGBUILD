# Maintainer: Runnytu < runnytu at gmail dot com >
# OldMaintainer: Alexey Kharlamov <der@2-47.ru>
# Contributor: David Dufberg Tøttrup <david at dufberg dot se>
# Contributor: Jordi De Groof <jordi(dot)degroof(at)gmail(dot)com>
# Contributor: pyther <pyther@pyther.net>
# Contributor: z3ntu <WEI16416@spengergasse.at>

pkgname=packettracer
pkgver=7.2
pkgrel=1
pkgdesc="Network design and emulation software for Cisco's Networking Academy instructors and students."
arch=( 'x86_64' )
depends_x86_64=('openssl-1.0' 'libpng12' 'icu52')
url="http://www.netacad.com/about-networking-academy/packet-tracer"
license=('custom')

source=('packettracer' 'linguist' 'packettracer.sh')
source_x86_64=('local://Packet Tracer 7.2 for Linux 64 bit.tar.gz')
sha512sums=('7135a62c5e46d9742eb8bdb5b3b171201243487e3681d152595121cfa1b9e5f3a0f89a6e54f25b7aa4cd2ae87156db4351b992a4988d364ba36c7bd71829c4d2'
	    'dab1f7f9c77c900a65899f2d795d9df39136de7e6ab1f544c538311012a212edbbb2101741672fdbe729c43e5bef0cb323800aa40b68b0cacf14342a1b040800'
	    '3f4732213a9ca7c95f742edbdccf4d84c95e1c9e00d3dfa72e79b8039ef86bed29bc5b76586402a233ce3af409c0a56c759c2554e17962c292a6bd333654ce71')
sha512sums_x86_64=('c5315fece36504ea551b8bcc9abc8c92829b90eb986e6e231cbbb7add981bac3d7d15343efe0a74527a25d768dcb60cf603699528ff3bde42251678ce0f70f6d')

# We don't want to strip anything from the static libraries
# We want to keep all binaries orginal (Cisco is goofy)
options=(!strip)
install=pt.install

package() {
  cd "${srcdir}/"

  mkdir -p "${pkgdir}/usr/share/packettracer/"{art,backgrounds,bin,extensions,help,languages,saves,Sounds,templates}

  cp -r ./art/* "${pkgdir}/usr/share/packettracer/art"
  cp -r ./backgrounds/* "${pkgdir}/usr/share/packettracer/backgrounds"
  cp -r ./bin/* "${pkgdir}//usr/share/packettracer/bin"
  cp -r ./extensions/* "${pkgdir}/usr/share/packettracer/extensions"
  cp -r ./languages/* "${pkgdir}/usr/share/packettracer/languages"
  cp -r ./saves/* "${pkgdir}/usr/share/packettracer/saves"
  cp -r ./Sounds/* "${pkgdir}/usr/share/packettracer/Sounds"
  cp -r ./templates/* "${pkgdir}/usr/share/packettracer/templates"

  # Help Files that are optinal uncomment to include them (55 MB)
  # cp -r ./help/* "${pkgdir}/usr/share/packettracer/help"

  # Mime Info for PKA, PKT, PKZ
  install -D -m644 ./bin/Cisco-pka.xml "${pkgdir}/usr/share/mime/packages/Cisco-pka.xml"
  install -D -m644 ./bin/Cisco-pkt.xml "${pkgdir}/usr/share/mime/packages/Cisco-pkt.xml"
  install -D -m644 ./bin/Cisco-pkz.xml "${pkgdir}/usr/share/mime/packages/Cisco-pkz.xml"

  rm "${pkgdir}/usr/share/packettracer/bin/Cisco-pka.xml"
  rm "${pkgdir}/usr/share/packettracer/bin/Cisco-pkt.xml"
  rm "${pkgdir}/usr/share/packettracer/bin/Cisco-pkz.xml"

  # Install Mimetype Icons
  install -D -m644 ./art/pka.png "${pkgdir}/usr/share/icons/hicolor/48x48/mimetypes/application-x-pka.png"
  install -D -m644 ./art/pkt.png "${pkgdir}/usr/share/icons/hicolor/48x48/mimetypes/application-x-pkt.png"
  install -D -m644 ./art/pkz.png "${pkgdir}/usr/share/icons/hicolor/48x48/mimetypes/application-x-pkz.png"

  # EULA
  install -D -m644 eula72.txt "${pkgdir}/usr/share/licenses/$pkgname/eula72.txt"

  # Shell script to start PT and tell it to use included qt files
  # Arch's QT causes PT to crash when saving!
  install -D -m755 "${srcdir}/packettracer" "${pkgdir}/usr/share/packettracer/packettracer"

  # Symlink to /usr/bin
  mkdir -p "${pkgdir}/usr/bin/"
  ln -s /usr/share/packettracer/packettracer "${pkgdir}/usr/bin/packettracer"

  # Improved version of Cisco's linguist script
  install -D -m755 "${srcdir}/linguist" "${pkgdir}/usr/share/packettracer/linguist"

  # Add enviroment variable
  install -D -m755 "${srcdir}/packettracer.sh" "${pkgdir}/etc/profile.d/packettracer.sh"

  # Desktop File
  install -D -m644 ./bin/Cisco-PacketTracer.desktop "${pkgdir}/usr/share/applications/Cisco-PacketTracer.desktop"
  sed 's/\/opt\/pt/\/usr\/share\/packettracer/' -i "${pkgdir}/usr/share/applications/Cisco-PacketTracer.desktop"
  rm "${pkgdir}/usr/share/packettracer/bin/Cisco-PacketTracer.desktop"
}

