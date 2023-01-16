#! /bin/sh

set -ex

# Special environment variable to be used when only fetching and extracting
# embedded dependencies should be done, i.e. no system package manager is
# being invoked.
#
# set this as environment variable to ON to activate this mode.
if [ x$PREPARE_ONLY_EMBEDS = x ]
then
    PREPARE_ONLY_EMBEDS=OFF
fi

# if SYSDEP_ASSUME_YES=ON is set, then system package managers are attempted
# to install packages automatically, i.e. without confirmation.
if [ x$SYSDEP_ASSUME_YES = xON ]
then
    SYSDEP_ASSUME_YES='-y'
else
    unset SYSDEP_ASSUME_YES
fi

# {{{ sysdeps fetcher and unpacker for deps that aren't available via sys pkg mgnr
SYSDEPS_BASE_DIR="$(dirname $0)/../_deps"

SYSDEPS_DIST_DIR="$SYSDEPS_BASE_DIR/distfiles"
SYSDEPS_SRC_DIR="$SYSDEPS_BASE_DIR/sources"
SYSDEPS_CMAKE_FILE="$SYSDEPS_SRC_DIR/CMakeLists.txt"

fetch_and_unpack()
{
    NAME=$1
    DISTFILE=$2
    URL=$3

    FULL_DISTFILE="$SYSDEPS_DIST_DIR/$DISTFILE"

    if ! test -f "$FULL_DISTFILE"; then
        if which curl &>/dev/null; then
            curl -L -o "$FULL_DISTFILE" "$URL"
        elif which wget &>/dev/null; then
            wget -O "$FULL_DISTFILE" "$URL"
        elif which fetch &>/dev/null; then
            # FreeBSD
            fetch -o "$FULL_DISTFILE" "$URL"
        else
            echo "Don't know how to fetch from the internet." 1>&2
            exit 1
        fi
    else
        echo "Already fetched $DISTFILE. Skipping."
    fi

    if ! test -d "$SYSDEPS_SRC_DIR/$NAME"; then
        echo "Extracting $DISTFILE"
        tar xzpf $FULL_DISTFILE -C $SYSDEPS_SRC_DIR
    else
        echo "Already extracted $DISTFILE. Skipping."
    fi

    echo "add_subdirectory($NAME EXCLUDE_FROM_ALL)" >> $SYSDEPS_CMAKE_FILE
}

fetch_and_unpack_fmtlib()
{
    fetch_and_unpack \
        fmt-8.1.1 \
        fmtlib-8.1.1.tar.gz \
        https://github.com/fmtlib/fmt/archive/refs/tags/8.1.1.tar.gz
}

prepare_fetch_and_unpack()
{
    mkdir -p "${SYSDEPS_BASE_DIR}"
    mkdir -p "${SYSDEPS_DIST_DIR}"
    mkdir -p "${SYSDEPS_SRC_DIR}"

    # empty out sysdeps CMakeLists.txt
    rm -f $SYSDEPS_CMAKE_FILE
}
# }}}
fetch_and_unpack_embeds()
{
    set -x
    local termbench_pro_git_sha="cd571e3cebb7c00de9168126b28852f32fb204ed"
    fetch_and_unpack \
        termbench-pro-$termbench_pro_git_sha \
        termbench-pro-$termbench_pro_git_sha.tar.gz \
        https://github.com/contour-terminal/termbench-pro/archive/$termbench_pro_git_sha.tar.gz \
        termbench_pro

    local libunicode_git_sha="a511f3995cdf708f2e199276c90e21408db00a50"
    fetch_and_unpack \
        libunicode-$libunicode_git_sha \
        libunicode-$libunicode_git_sha.tar.gz \
        https://github.com/contour-terminal/libunicode/archive/$libunicode_git_sha.tar.gz \
        libunicode
}

install_deps_fedora()
{
    # fetch_and_unpack_gsl
    fetch_and_unpack_fmtlib
    # [ x$PREPARE_ONLY_EMBEDS = xON ] && return
}

main()
{
    prepare_fetch_and_unpack
    install_deps_fedora
    fetch_and_unpack_embeds
}

main $*