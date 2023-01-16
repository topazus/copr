Name:           ttfautohint
Version:        1.8.4
Release:        3%{?dist}
Summary:        Automated hinting utility for TrueType fonts
License:        FTL or GPLv2
URL:            http://www.freetype.org/ttfautohint
Source0:        http://download.savannah.gnu.org/releases/freetype/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  gcc gcc-c++
BuildRequires:  freetype-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  pkgconfig
%if 0%{?fedora}
BuildRequires:  qt5-qtbase-devel
%elif 0%{?suse_version}
BuildRequires:  libqt5-qtbase-devel
%endif
Provides:       bundled(gnulib)
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description
This is a utility which takes a TrueType font as the input, removes its
bytecode instructions (if any), and returns a new font where all glyphs
are bytecode hinted using the information given by FreeType's autohinting
module. The idea is to provide the excellent quality of the autohinter on
platforms which don't use FreeType.

%prep
%setup -q

%build
%configure --disable-silent-rules --disable-static
%make_build

%install
%make_install

find %{buildroot} -name '*.la' -delete

%files
%license COPYING
%{_bindir}/ttfautohint
%{_mandir}/man1/ttfautohint.1*

/usr/share/doc/ttfautohint/
%{_bindir}/ttfautohintGUI
%{_mandir}/man1/ttfautohintGUI.1*

%{_libdir}/libttfautohint.so.1*

%{_includedir}/ttfautohint*.h
%{_libdir}/libttfautohint.so
%{_libdir}/pkgconfig/ttfautohint.pc

%changelog
