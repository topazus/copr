%global debug_package %{nil}

Name:           libxml2
Version:        2.10.3
Release:        1%{?dist}
License:        MIT
Summary:        A Library to Manipulate XML Files
URL:            https://gitlab.gnome.org/GNOME/libxml2
Source0:        https://gitlab.gnome.org/GNOME/libxml2/-/archive/v%{version}/libxml2-v%{version}.tar.gz

BuildRequires:  fdupes pkgconfig autoconf automake libtool

BuildRequires:  python3-devel python-rpm-macros readline-devel zlib-devel liblzma5

Requires:       glibc-devel
Requires:       readline-devel
Requires:       xz-devel
Requires:       zlib-devel liblzma5
Requires:       python-extras python-testtools >= 1.8.0

%description
The XML C library was initially developed for the GNOME project. It is
now used by many programs to load and save extensible data structures
or manipulate any kind of XML files.

%prep
%autosetup -n libxml2-v%{version}
sed -i '1 s|/usr/bin/env python|/usr/bin/python3|' doc/apibuild.py

%build
export CFLAGS='%{optflags} -fno-semantic-interposition'
./autogen.sh \
    --prefix=%{_prefix} \
    --disable-silent-rules \
    --disable-static \
    --with-fexceptions \
    --with-history \
    --enable-ipv6 \
    --with-sax1 \
    --with-regexps \
    --with-threads \
    --with-reader \
    --with-ftp \
    --with-http \
    --with-legacy

%make_build

%install
# solve rpath error
export QA_RPATHS=$[ 0x0001 | 0x002 ]
%make_install

%files
/usr/bin/xml2-config
/usr/bin/xmlcatalog
/usr/bin/xmllint

/usr/include/libxml2/libxml/

/usr/lib64/


%{python_sitelib}/
/usr/share/aclocal/libxml.m4
/usr/share/doc/libxml2/

/usr/share/gtk-doc/
/usr/share/man/man1

%changelog
