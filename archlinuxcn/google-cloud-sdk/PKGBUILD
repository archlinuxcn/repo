# Maintainer: Benjamin Denhartog <ben@sudoforge.com>
# Contributor: Mansour Behabadi <mansour@oxplot.com>
# Contributor: Troy Engel <troyengel+arch@gmail.com>
# Contributor: Geoff Hill <geoff@geoffhill.org>
# Contributor: Sebastien Bariteau <numkem@numkem.org>
# Contributor: Justin Dray <justin@dray.be>

# For ISSUES, REQUESTS, and QUESTIONS:
# https://github.com/sudoforge/pkgbuilds

pkgname="google-cloud-sdk"
pkgver=385.0.0
pkgrel=2
pkgdesc="A set of command-line tools for the Google Cloud Platform. Includes gcloud (with beta and alpha commands), gsutil, and bq."
url="https://cloud.google.com/sdk/"
license=("Apache")
arch=('x86_64')
depends=('python')
optdepends=(
  "python2: for dev_appserver.py and endpointscfg support"
  "python-crcmod: [gsutil] verify the integrity of GCS object contents"
)
options=('!strip' 'staticlibs')
source=(
  "https://dl.google.com/dl/cloudsdk/release/downloads/for_packagers/linux/${pkgname}_${pkgver}.orig.tar.gz"
  "google-cloud-sdk.sh"
  "0001-set-python2-for-dev-appserver-py.patch"
  "0002-set-python2-for-endpointscfg-py.patch"
  "0003-add-compdef-to-zsh-completion.patch"
  "0004-collections-abc.patch"
)
sha256sums=('a26fab7e90788814986e054f07c6fed2e625cbe7a0eb73e860609b49a0c73e52'
            'ecd7b3895f6ecf1c6411f385bee3a4b64139976d72069469d323c8a09b97aaea'
            '62ec7f56e09168d375823e9e99fcdcfbf40b0fffdd75f35cf91122c5902c82e9'
            'ff6065ce2e54ac654605bd5fe554313b1d0def2c31ce56ff39429098dd1e39fe'
            '4694f5191ceea7cf8076861ce5790ba9e809023da278b0f6ed862b9611e5aa93'
            'ea39fc4907d8ddf28ebaeed4b7c4547936a602f907c7523fc62488771e0df043')

prepare() {
  cd "${srcdir}/${pkgname}"

  for f in "${source[@]}"; do
    [[ "$f" =~ \.patch$ ]] && \
    ( \
      patch -p1 -i "${srcdir}/${f}" > /dev/null 2>&1 ||\
      ( \
        echo "failed to apply patch: $(basename ${f})" && \
        exit 1 \
      ) \
    )
  done
}

package() {
  mkdir "${pkgdir}/opt"
  cp -r "${srcdir}/${pkgname}" "${pkgdir}/opt"

  # The Google code uses a _TraceAction() method which spams the screen even
  # in "quiet" mode, we're throwing away output on purpose to keep it clean
  #  ref: lib/googlecloudsdk/core/platforms_install.py
  python "${pkgdir}/opt/${pkgname}/bin/bootstrapping/install.py" \
    --quiet \
    --usage-reporting False \
    --path-update False \
    --bash-completion False \
    --additional-components "" \
    1 > /dev/null

  rm -rf "${pkgdir}/opt/${pkgname}/.install/.backup"
  mkdir "${pkgdir}/opt/${pkgname}/.install/.backup"
  find $pkgdir -name '__pycache__' -type d -exec rm -rf {} +

  install -D -m 0755 "${srcdir}/${source[1]}" \
    "${pkgdir}/etc/profile.d/google-cloud-sdk.sh"

  install -D -m 0644 "${pkgdir}/opt/${pkgname}/completion.bash.inc" \
    "${pkgdir}/etc/bash_completion.d/google-cloud-sdk"

  install -D -m 0644 "${pkgdir}/opt/${pkgname}/completion.zsh.inc" \
    "${pkgdir}/usr/share/zsh/site-functions/_gcloud"

  mkdir -p "${pkgdir}/usr/share"
  mv -f "${pkgdir}/opt/${pkgname}/help/man" "${pkgdir}/usr/share/"
  chmod 0755 "${pkgdir}/usr/share/man"
  chmod 0755 "${pkgdir}/usr/share/man/man1"

  mkdir -p "${pkgdir}/usr/bin"
  for i in "${pkgdir}/opt/${pkgname}/bin"/*; do
    ln -st "${pkgdir}/usr/bin/" "${i#${pkgdir}}"
  done
  rm -f "${pkgdir}"/usr/bin/{bq,dev_appserver.py*,endpointscfg.py*,java_dev_appserver.sh}

  chmod -x "${pkgdir}"/usr/share/man/man1/*
  find "${pkgdir}/opt/${pkgname}" -name "*.html" -o -name "*.json" -exec chmod -x {} \;
  find "${pkgdir}/opt/${pkgname}" -name "*_test.py" -exec chmod +x {} \;
}
