# Maintainer: Benjamin Denhartog <ben@sudoforge.com>
# Contributor: Mansour Behabadi <mansour@oxplot.com>
# Contributor: Troy Engel <troyengel+arch@gmail.com>
# Contributor: Geoff Hill <geoff@geoffhill.org>
# Contributor: Sebastien Bariteau <numkem@numkem.org>
# Contributor: Justin Dray <justin@dray.be>

pkgname="google-cloud-sdk"
pkgver=228.0.0
pkgrel=1
pkgdesc="A set of command-line tools for the Google Cloud Platform. Includes gcloud (with beta and alpha commands), gsutil, and bq."
url="https://cloud.google.com/sdk/"
license=("Apache")
arch=('x86_64')
depends=('python2')
optdepends=('python2-crcmod: [gsutil] verify the integrity of GCS object contents')
options=('!strip' 'staticlibs')

source=(
  "https://dl.google.com/dl/cloudsdk/release/downloads/for_packagers/linux/${pkgname}_${pkgver}.orig.tar.gz"
  "google-cloud-sdk.sh"
)
sha256sums=(
  'ecc2ce0347d83812d29450f72828d895c568c633601ae682a25da160833a8d7c'
  '36ac88de630e49ea4b067b1f5f229142e4cf97561b98b3bd3d8115a356946692'
)

prepare() {
  msg2 "Checking for newer upstream release"

  _latest=$(\
    curl -s https://dl.google.com/dl/cloudsdk/release/sha256.txt |\
    egrep "google-cloud-sdk_.*\.orig\.tar\.gz" |\
    awk -e 'BEGIN{FS="/"}{print $4}' |\
    sed 's/[^0-9]*\(\([[:digit:]]\+.\?\)\{2\}[^.]\+\).*/\1/')
      # [^0-9]* :: matches any non-digit character 0-n times
      # \( :: begins group 1
      #   \([[:digit:]]\+.\?\)\{2\}
      #     :: captures the major and minor parts of the version, with dot
      #     :: capture group 2 is created to facilitate repeating with \{2\}
      #   [^.]\+ :: matches the patch without the dot
      # \) :: terminates group 1
      # .* :: matches any character 0-n times
      # /\1/ :: replaces the entire string with the contents of group 1

  msg2 "This AUR release: ${pkgver}"
  msg2 "Latest upstream release: ${_latest}"
  if [ "${_latest}" != "${pkgver}" ]; then
    msg2 "** Please flag out-of-date at https://aur.archlinux.org/packages/${pkgname}"
  fi
}

package() {
  msg2 "Copying core SDK components"
  mkdir "${pkgdir}/opt"
  cp -r "${srcdir}/${pkgname}" "${pkgdir}/opt"

  msg2 "Running bootstrapping script and adding additional components"
  _additional_components=(alpha beta)

  # The Google code uses a _TraceAction() method which spams the screen even
  # in "quiet" mode, we're throwing away output on purpose to keep it clean
  #  ref: lib/googlecloudsdk/core/platforms_install.py
  python2 "${pkgdir}/opt/${pkgname}/bin/bootstrapping/install.py" --quiet \
    --usage-reporting False --path-update False --bash-completion False \
    --additional-components "${_additional_components[@]}" 1 > /dev/null

  msg2 "Cleaning up artifacts of the bootstrap script"
  rm -rf "${pkgdir}/opt/${pkgname}/.install/.backup"
  mkdir "${pkgdir}/opt/${pkgname}/.install/.backup"

  msg2 "Setting up profile environment variables"
  install -Dm755 "${srcdir}/${source[1]}" \
    "${pkgdir}/etc/profile.d/google-cloud-sdk.sh"

  msg2 "Installing bash completion script"
  install -Dm755 "${pkgdir}/opt/${pkgname}/completion.bash.inc" \
    "${pkgdir}/etc/bash_completion.d/google-cloud-sdk"

  msg2 "Fixing python references for python2 and compiling *.pyc"
  grep -Irl 'python' "${pkgdir}/opt/${pkgname}" | \
    xargs sed -i 's|#!.*python\b|#!/usr/bin/env python2|g'
  find "${pkgdir}/opt/${pkgname}/bin/" -maxdepth 1 -type f -exec \
    sed -i 's/CLOUDSDK_PYTHON=python\b/CLOUDSDK_PYTHON=python2/g' {} \;
  python2 -m compileall -q -f -x python3 -d "/opt/google-cloud-sdk" \
    "${pkgdir}/opt/${pkgname}/"

  msg2 "Installing man pages"
  mkdir -p "${pkgdir}/usr/share"
  mv -f "${pkgdir}/opt/${pkgname}/help/man" "${pkgdir}/usr/share/"
  chmod 0755 "${pkgdir}/usr/share/man"
  chmod 0755 "${pkgdir}/usr/share/man/man1"

  msg2 "Creating symlinks for applications"
  mkdir -p "${pkgdir}/usr/bin"
  for i in "${pkgdir}/opt/${pkgname}/bin"/*; do
    ln -st "${pkgdir}/usr/bin/" "${i#${pkgdir}}"
  done
  rm -f "${pkgdir}"/usr/bin/{bq,dev_appserver.py*,endpointscfg.py*,java_dev_appserver.sh}

  msg2 "Fixing file permissions"
  chmod -x "${pkgdir}"/usr/share/man/man1/*
  find "${pkgdir}/opt/${pkgname}" -name "*.html" -o -name "*.json" -exec chmod -x {} \;
  find "${pkgdir}/opt/${pkgname}" -name "*_test.py" -exec chmod +x {} \;
}
