#!/bin/sh

pkg=$1

# Clean up
for f in *; do
    case "$f" in
        lilac.*)
            continue
            ;;
        get_pkg.sh)
            continue
            ;;
        package.list)
            continue
            ;;
        *)
            rm -v "$f"
            ;;
    esac
done

git clone --depth 1 https://github.com/AsahiLinux/PKGBUILDs
mv PKGBUILDs/$pkg/* .
rm -rf PKGBUILDs/
updpkgsums
