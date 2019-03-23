# Maintainer: OriginCode <origincoder@yahoo.com

pkgname=atom-transparent
pkgver=1.35.1
pkgrel=1
pkgdesc='A hackable text editor for the 21st Century, with transparency patch.'
arch=('x86_64')
url='https://github.com/atom/atom'
license=('MIT' 'custom')
depends=('apm' 'electron' 'libxkbfile')
makedepends=('git' 'npm')
optdepends=('ctags: symbol indexing support'
            'git: Git and GitHub integration')
replaces=('atom-editor' 'atom-editor-transparent')
options=(!emptydirs)
source=("atom-${pkgver}.tar.gz::https://github.com/atom/atom/archive/v${pkgver}.tar.gz"
        'atom.js'
        'dugite-use-system-git.patch'
        'electron-3.patch'
        'fix-atom-sh.patch'
        'fix-license-path.patch'
        'fix-middle-click.patch'
        'fix-restart.patch'
        'symbols-view-use-system-ctags.patch'
        'use-system-apm.patch'
        'use-system-electron.patch'
        'enable-transparency.patch')
sha256sums=('a50bcfcda4cfe6017fb76defc3a0eeaca209954d86a631f5963e69a0c064c2e8'
            'cdf87ab82cfcf69e8904684c59b08c35a68540ea16ab173fce06037ac341efcd'
            '530b46d31df0f5e8f5881e1608a66fe75d549092a6db2e72ba3ad69c48714153'
            '328da3b30f4e20e56b38e588d9fe871c01bbbe69865a79e9586919564bdfa869'
            'ab9eed3d4c8bfefea256953428379ab1e636b9c7d4c4af30ddc3f485330183c2'
            '5c77deec5896b658395bdf695c3bc044c9140ad0a5a87f34520c4a31972e51d1'
            '142d540259296396f6d528ecf2f7c6a363f89f8a0d2ad66497f8392da06202bc'
            'c4b883265d16ee30402c449d07be78b7088c1aa60c4f3e712b8bfe857c95f346'
            '3c68e6b3751313e1d386e721f8f819fb051351fb2cf8e753b1d773a0f475fef8'
            '53f43c9328a66e24b3467a0a06d9dfde83475f7e54251bf7a523beafaa043806'
            '457bd1b06604aec1e2ebb6e0ea473742747e183e833fffb36377aad64c37bcd5'
            '2cb262dfd15f67dd1a01a9b314983f535da8b06ce4a814d214e12ec369631d58')

prepare() {
  cd "${srcdir}/atom-${pkgver}"

  patch -Np1 -i "${srcdir}"/fix-atom-sh.patch
  patch -Np1 -i "${srcdir}"/use-system-electron.patch
  patch -Np1 -i "${srcdir}"/use-system-apm.patch
  patch -Np1 -i "${srcdir}"/fix-license-path.patch
  patch -Np1 -i "${srcdir}"/fix-restart.patch
  patch -Np1 -i "${srcdir}"/enable-transparency.patch
  
  # Fix for Electron 3
  patch -Np1 -i "${srcdir}"/electron-3.patch
}

build() {
  cd "${srcdir}/atom-${pkgver}"

  # Fix for Electron 3
  npm install --package-lock-only @atom/nsfw@1.0.20 node-abi

  rm package-lock.json

  ATOM_RESOURCE_PATH="${PWD}" \
  npm_config_target=$(tail -c +2 /usr/lib/electron/version) \
  apm install

  # Use system ctags
  cd node_modules/symbols-view
  patch -Np1 -i "${srcdir}"/symbols-view-use-system-ctags.patch
  rm -r vendor
  cd ../..

  # Use system git
  cd node_modules/dugite
  patch -Np1 -i "${srcdir}"/dugite-use-system-git.patch
  rm -r git
  cd ../..

  # https://bugs.archlinux.org/task/61047
  cd node_modules/tabs
  patch -Np1 -i "${srcdir}"/fix-middle-click.patch
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
      -e "s|<%= installDir %>|/usr|" \
      -e "s|<%= appFileName %>|atom|" \
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
  find "${pkgdir}"/usr/lib/atom/node_modules \
      -name "*.a" -exec rm '{}' \; \
      -or -name "*.bat" -exec rm '{}' \; \
      -or -name "*.c" -exec rm '{}' \; \
      -or -name "*.cpp" -exec rm '{}' \; \
      -or -name "*.node" -exec chmod a-x '{}' \; \
      -or -name "benchmark" -prune -exec rm -r '{}' \; \
      -or -name "doc" -prune -exec rm -r '{}' \; \
      -or -name "html" -prune -exec rm -r '{}' \; \
      -or -name "man" -prune -exec rm -r '{}' \; \
      -or -name "scripts" -prune -exec rm -r '{}' \; \
      -or -path "*/less/gradle" -prune -exec rm -r '{}' \; \
      -or -path "*/task-lists/src" -prune -exec rm -r '{}' \;
}
