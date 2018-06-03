# Maintainer: Frantic1048 <archer@frantic1048.com>
# Upstream URL: https://github.com/atom/atom

pkgname=atom-transparent
pkgver=1.27.1
pkgrel=1
pkgdesc='A hackable text editor for the 21st Century - with transparent background support'
arch=('x86_64')
url='https://github.com/atom/atom'
license=('MIT' 'custom')
depends=('apm' 'electron' 'libxkbfile')
makedepends=('git' 'npm')
optdepends=('ctags: symbol indexing support'
            'git: Git and GitHub integration')
conflicts=('atom-editor')
replaces=('atom-editor-transparent')
options=(!emptydirs)
source=("atom-${pkgver}.tar.gz::https://github.com/atom/atom/archive/v${pkgver}.tar.gz"
        'atom.js'
        'dugite-use-system-git.patch'
        'fix-atom-sh.patch'
        'fix-license-path.patch'
        'fix-node8.patch'
        'fix-restart.patch'
        'symbols-view-use-system-ctags.patch'
        'use-system-apm.patch'
        'use-system-electron.patch'
        'enable-transparency.patch')
sha256sums=('147c237d944d0261ac2caf525badd8c76cf92da99bb6901c89e491fb5f0c16bf'
            'cdf87ab82cfcf69e8904684c59b08c35a68540ea16ab173fce06037ac341efcd'
            '3fadee5a2d8c1ff35e085f9b9f3cf2eb71627bda9e8b10c2a0bd85b268591bf6'
            'd8d77adebd7bd4eaf024988c68c30dc6b968044f7a6381227d13b6d77fa2b442'
            '7f0142c91e24236a3a6dcc70af9d4217f65c5a764091876a916e3bbafa4ed0fa'
            'eb771d7c009be8d48c1387ed63f3e575dc12f3bd69455b4be4b78ab57cb49b86'
            'f81a8dd53403fe76d80716b65d69bec141fae0b1a9a6ef56314f9e815e48f132'
            '3c68e6b3751313e1d386e721f8f819fb051351fb2cf8e753b1d773a0f475fef8'
            '4b91a1acd112838bd001f4e3c555de2a5fc7446c9eab6bc5dae0ca640306e81b'
            '1d0ff39e5bc5c0bfbb08a533bff9fb834a8dbc70d280bf93b5e2649fff181221'
            '2cb262dfd15f67dd1a01a9b314983f535da8b06ce4a814d214e12ec369631d58')

prepare() {
  cd "${srcdir}/atom-${pkgver}"

  patch -Np1 -i "${srcdir}"/fix-atom-sh.patch
  patch -Np1 -i "${srcdir}"/use-system-electron.patch
  patch -Np1 -i "${srcdir}"/use-system-apm.patch
  patch -Np1 -i "${srcdir}"/fix-license-path.patch
  patch -Np1 -i "${srcdir}"/fix-node8.patch
  patch -Np1 -i "${srcdir}"/fix-restart.patch
  patch -Np1 -i "${srcdir}"/enable-transparency.patch

  # Workaround for Node 10
  sed -e 's|"electron-link": "0.2.0"|"electron-link": "../../electron-link"|' \
      -i script/package.json
  cd ..
  git clone https://github.com/atom/electron-link.git
  cd electron-link
  git checkout v0.2.0
  sed -e 's/"leveldown": "^1.6.0"/"leveldown": "^2.0.1"/' -i package.json
  npm install
  npx babel src -d lib
  cd node_modules/levelup
  sed -e 's/"leveldown": "^1.1.0"/"leveldown": "^2.0.1"/' -i package.json
}

build() {
  cd "${srcdir}/atom-${pkgver}"

  export ATOM_RESOURCE_PATH="$srcdir/atom-$pkgver"
  # If unset, ~/.atom/.node-gyp/.atom/.npm is used
  export NPM_CONFIG_CACHE="${HOME}/.atom/.npm"
  apm clean
  apm install

  # Use system ctags
  cd node_modules/symbols-view
  patch -Np1 -i "${srcdir}"/symbols-view-use-system-ctags.patch
  rm -r vendor
  cd ../..

  # Use system git (TODO: set LOCAL_GIT_DIRECTORY=/usr)
  cd node_modules/dugite
  patch -Np1 -i "${srcdir}"/dugite-use-system-git.patch
  rm -r git
  cd ../..

  cd script
  npm install
  ./build
}

package() {
  cd "${srcdir}/atom-${pkgver}"

  install -d -m 755 "${pkgdir}"/usr/lib
  cp -r out/app "${pkgdir}"/usr/lib/atom
  install -m 644 out/startup.js "${pkgdir}"/usr/lib/atom
  install -m 755 "${srcdir}/atom.js" "${pkgdir}"/usr/lib/atom/atom

  install -d -m 755 "${pkgdir}/usr/share/applications"
  sed -e "s|<%= appName %>|Atom|" \
      -e "s/<%= description %>/${pkgdesc}/" \
      -e "s|<%= installDir %>/share/<%= appFileName %>/atom|/usr/lib/atom/atom|" \
      -e "s|<%= iconPath %>|atom|" \
      resources/linux/atom.desktop.in > "${pkgdir}/usr/share/applications/atom.desktop"

  for size in 16 24 32 48 64 128 256 512 1024; do
    install -D -m 644 resources/app-icons/stable/png/${size}.png \
            "${pkgdir}"/usr/share/icons/hicolor/${size}x${size}/apps/atom.png
  done
  ln -sf ../../../share/icons/hicolor/1024x1024/apps/atom.png \
      "${pkgdir}"/usr/lib/atom/resources/atom.png

  install -D -m 755 atom.sh "${pkgdir}/usr/bin/atom"

  install -d -m 755 "${pkgdir}/usr/share/licenses/${pkgname}"
  node -e "require('./script/lib/get-license-text')().then((licenseText) => require('fs').writeFileSync('${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.md', licenseText))"

  # Remove useless stuff
  rm "${pkgdir}"/usr/lib/atom/node_modules/.bin/pegjs
  find "${pkgdir}"/usr/lib/atom/node_modules \
      -name "*.a" -exec rm '{}' \; \
      -or -name "*.bat" -exec rm '{}' \; \
      -or -name "*.node" -exec chmod a-x '{}' \; \
      -or -name "benchmark" -prune -exec rm -r '{}' \; \
      -or -name "doc" -prune -exec rm -r '{}' \; \
      -or -name "html" -prune -exec rm -r '{}' \; \
      -or -name "man" -prune -exec rm -r '{}' \; \
      -or -name "scripts" -prune -exec rm -r '{}' \; \
      -or -path "*/less/gradle" -prune -exec rm -r '{}' \; \
      -or -path "*/task-lists/src" -prune -exec rm -r '{}' \;
}
