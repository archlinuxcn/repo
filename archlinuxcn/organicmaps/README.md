# Traffic-efficient way to update this package:
1. Designate a permanent location for mirroring repositories, in this example
   /path/to/src_git_mirrors. Clone the repositories (do this only once):
```sh
cd /path/to/src_git_mirrors # permanent storage location
git clone --mirror --depth=1 https://github.com/unicode-org/icu.git
git clone --mirror --depth=1 https://github.com/libexpat/libexpat.git
git clone --mirror --depth=1 https://github.com/harfbuzz/harfbuzz.git
git clone --mirror --depth=1 https://github.com/organicmaps/organicmaps.git
```
2. Put a script like this in your $PATH, named e.g. source_url_rewriter.sh:
```sh
case $1 in
  https://*)
    printf "file:///path/to/src_git_mirrors/%s" ${1##*/}
    ;;
  *)
    printf "%s" "$1"
    ;;
esac
```
3. export $SOURCE_URL_REWRITER variable pointing to the script:
```
export SOURCE_URL_REWRITER="source_url_rewriter.sh"
```
4. Run `makepkg` as usual, it will fetch the necessary data in repos in
   /path/to/src_git_mirrors/ and use them as remotes for OMaps submodules
