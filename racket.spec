%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname racket

Name:           %{appname}-snapshot
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        a general-purpose programming language
License:        GPLv3 and LGPLv3 and MIT
URL:            https://racket-lang.org
#Source0:

BuildRequires: make gcc racket tar wget git


# Racket heavily utilizes the system ffi library.
BuildRequires:  libffi-devel

# For the racket/gui library (via libffi)
BuildRequires:  gtk3

# For the racket/draw library (via libffi)
BuildRequires: cairo
BuildRequires: pango
BuildRequires: libpng
BuildRequires: libjpeg-turbo

%description
Racket is a general-purpose programming language and an ecosystem for language-oriented programming.

%prep
#git clone --depth=1 https://github.com/racket/racket.git .
wget https://plt.cs.northwestern.edu/snapshots/current/installers/racket-test-current-src.tgz
tar -xf racket-*.tgz && rm racket-*.tgz

%build
cd racket-*/src
%configure \
  --enable-pthread \
  --enable-shared \
  --enable-libffi \
  --disable-strip
%make_build

%install
cd racket-*/src
export QA_SKIP_BUILD_ROOT=1
%make_install

# -i: for system-wide
# --auto: do not ask
raco pkg install --auto -i racket-langserver

%files
/etc/racket/config.rktd

/usr/bin/drracket
/usr/bin/gracket
/usr/bin/gracket-text
/usr/bin/mred
/usr/bin/mred-text
/usr/bin/mzc
/usr/bin/mzpp
/usr/bin/mzscheme
/usr/bin/mztext
/usr/bin/pdf-slatex
/usr/bin/plt-games
/usr/bin/plt-help
/usr/bin/plt-r5rs
/usr/bin/plt-r6rs
/usr/bin/plt-web-server
/usr/bin/racket
/usr/bin/raco
/usr/bin/scribble
/usr/bin/setup-plt
/usr/bin/slatex
/usr/bin/slideshow
/usr/bin/swindle

/usr/include/racket/chezscheme.h
/usr/include/racket/racketcs.h
/usr/include/racket/racketcsboot.h

/usr/lib64/libracketcs.a

/usr/lib64/racket/compiled/usr/share/racket/

/usr/lib64/racket/

/usr/share/applications/drracket.desktop
/usr/share/applications/slideshow.desktop

/usr/share/doc/racket/

/usr/share/man/man1/*.1.gz
/usr/share/racket

%changelog
