
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname pqiv
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Powerful image viewer with minimal UI
License:        GPL-3.0
URL:            https://github.com/phillipberndt/pqiv
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ desktop-file-utils make pkg-config

BuildRequires: gtk3-devel gdk-pixbuf2-devel cairo-devel glib2-devel gtk+-devel
BuildRequires: libavc1394-devel libarchive-devel libspectre-devel libwebp-devel ImageMagick-devel poppler-devel


%description
pqiv is a powerful GTK 3 based command-line image viewer with a minimal UI.

%prep
%autosetup -n %{appname}-master -p1

%build
./configure --backends-build=shared
make %{?_smp_mflags}

%install
%make_install

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README*
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop

%dir %{_prefix}/lib/pqiv
%{_prefix}/lib/pqiv/*
%{_datadir}/man/man1/*.1.gz

%changelog
