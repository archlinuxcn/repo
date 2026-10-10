# Maintainer: aur.chaotic.cx
# Contributor: Dmytro Meleshko <qzlgeb.zryrfuxb@tznvy.pbz(rot13)>

: ${_java_ver:=17}

_pkgname="mindustry"
pkgbase="$_pkgname"
pkgver=160.5
pkgrel=1
pkgdesc="A sandbox tower defense game"
url="https://github.com/Anuken/Mindustry"
license=('GPL-3.0-only')
arch=('any')

makedepends=(
  "java-environment=${_java_ver:?}"
  'libicns'
)

_build="${pkgver%%.r*}"
_pkgsrc="Mindustry-$_build"
_pkgsrc_arc="Arc-$_build"
_pkgext="tar.gz"
source=(
  "$_pkgname-$_build.$_pkgext"::"https://github.com/Anuken/Mindustry/archive/v$_build.$_pkgext"
  "$_pkgname-arc-$_build.$_pkgext"::"https://github.com/Anuken/Arc/archive/refs/tags/v$_build.$_pkgext"
)
sha256sums=('bab4d829613d0ee64283fc51aecd12ec49ac48943c0c32cbc0027487d7aadf48'
  '9228bda3cfdec72ccd300e852e52d0bda5f37270478d3f7b386d643e868c074e')

prepare() {
  ln -sf "$_pkgsrc_arc" Arc

  cd "$_pkgsrc"
  sed -E -e '/archash/s&archash=.*$&'"archash=v${_build}&" -i gradle.properties
}

build() {
  cd "$_pkgsrc"

  # skip android subproject; see settings.gradle
  unset ANDROID_HOME JITPACK

  JAVA_HOME="/usr/lib/jvm/java-${_java_ver}-openjdk" \
    ./gradlew --warning-mode=all --no-daemon dist -Pbuildversion="${_build}" desktop:dist server:dist

  icns2png --extract core/assets/icons/icon.icns
}

_package_common() {
  depends+=(
    "java-runtime>=$_java_ver"
    'hicolor-icon-theme'
  )

  install -Dm755 /dev/stdin "$pkgdir/usr/share/applications/${pkgname%$_pkgtype}.desktop" << END
[Desktop Entry]
Type=Application
Name=$(sed -E -e "s/-/ /g;s/\b(.)/\u\1/g" <<< "${pkgname%$_pkgtype}")
Comment=$pkgdesc
Exec=${pkgname%$_pkgtype}
Icon=${pkgname%$_pkgtype}
Categories=Game;
Terminal=false
END

  install -Dm755 /dev/stdin "$pkgdir/usr/bin/${pkgname%$_pkgtype}" << END
#!/usr/bin/env bash
_java_ver=${_java_ver}
_best=""
for d in /usr/lib/jvm/java-*-openjdk; do
  if [ -d "\$d" ]; then
    n=\$(grep -Pom1 'java-\K[0-9]+' <<< "\$d")
    if (( \$n >= \${_java_ver} )); then
      _best="\$d"
      break
    fi
  fi
done
if [ -n "\$_best" ]; then
  export JAVA_HOME="\$_best"
fi

: \${JAVA_HOME:=/usr/lib/jvm/default}

exec "\$JAVA_HOME/bin/java" -jar "/usr/share/java/$_pkgname/${pkgname%$_pkgtype}.jar" "\$@"
END

  cd "$_pkgsrc"
  local icon_size
  for icon_size in 256 512 1024; do
    install -Dm644 "icon_${icon_size}x${icon_size}x32.png" \
      "$pkgdir/usr/share/icons/hicolor/${icon_size}x${icon_size}/apps/${pkgname%$_pkgtype}.png"
  done
}

_package_mindustry() {
  install -Dm755 "desktop/build/libs/Mindustry.jar" "$pkgdir/usr/share/java/$_pkgname/${pkgname%$_pkgtype}.jar"
}

_package_mindustry-server() {
  pkgdesc+=" - server"

  install -Dm755 "server/build/libs/server-release.jar" "$pkgdir/usr/share/java/$_pkgname/${pkgname%$_pkgtype}.jar"
}

_pkgtype=${pkgbase#$_pkgname}
pkgname=("$_pkgname${_pkgtype:-}" "$_pkgname-server${_pkgtype:-}")

for _p in "${pkgname[@]}"; do
  eval "package_$_p() {
    $(declare -f "_package_common" | tail -n +2)
    $(declare -f "_package_${_p%$_pkgtype}" | tail -n +2)
  }"
done
