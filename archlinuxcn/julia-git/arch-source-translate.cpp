//

#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#include <string>

static std::string get_srcdir(void)
{
    auto env = getenv("JL_MAKEPKG_SRCDIR");
    if (env) {
        std::string src = env;
        while (src.back() == '/')
            src.pop_back();
        return src;
    }
    return {};
}
static auto srcdir = get_srcdir();
static std::string juliadir = "/usr/share/julia";
static std::string basedir = "/usr/share/julia/base";

extern "C" const char *jl_archlinux_translate_filename(const char *_filename)
{
    if (srcdir.empty())
        return _filename;
    while (_filename[0] == '.' && _filename[1] == '/')
        _filename += 2;
    static std::string filename;
    filename = _filename;
    if (filename[0] != '/') {
        // relative path, assume to be base
        filename = basedir + '/' + filename;
    }
    else if (filename.starts_with(srcdir + "/base/")) {
        filename = juliadir + filename.substr(srcdir.size());
    }
    else if (filename.starts_with(srcdir + "/usr/")) {
        filename = filename.substr(srcdir.size());
    }
    return filename.c_str();
}
