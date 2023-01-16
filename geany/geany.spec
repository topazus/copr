%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname geany


Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A fast and lightweight IDE
License:        GPL 2.0
URL:            https://github.com/geany/geany
Source:         https://github.com/geany/geany/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++
BuildRequires: python3-docutils
BuildRequires: desktop-file-utils, gettext, pango-devel, intltool
BuildRequires: gtk+-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: perl(XML::Parser)
BuildRequires: make

	
Requires: vte291%{?_isa}
Requires: geany-libgeany


%description


%prep
%autosetup -n %{appname}-master -p1

%build
./autogen.sh
	
%configure --enable-gtk3 --enable-gtkdoc-header --prefix=%{buildroot}%{_prefix}
make
 
%install
make install


%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}


%changelog
