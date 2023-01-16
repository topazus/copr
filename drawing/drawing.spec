%global debug_package %{nil}
%define build_date %{lua: print(os.date("%Y%m%d"))}
%global _name drawing

Name:           %{_name}-git
Version:        0.0.0
Release:        %{build_date}%{?dist}
Summary:        Simple image editor for the Linux desktops
License:        GPL v3.0
URL:            https://github.com/maoschanz/drawing
Source0:        %{url}/archive/master/%{_name}-master.tar.gz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: meson
BuildRequires: python3-cairo python3-devel python3-gobject
BuildRequires: pkgconfig(gtk+-3.0)

Requires: python3-gobject python3-cairo
Requires: gtk3 hicolor-icon-theme

%description
Simple image editor for the Linux desktops.

%prep
%autosetup -n %{_name}-master -p1

%build
%meson
%meson_build
 
%install
%meson_install
%find_lang %{_name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%license LICENSE
%doc README.md
%{_bindir}/%{_name}
%{_datadir}/applications/*.desktop
%dir %{_datadir}/%{_name}
%{_datadir}/%{_name}/*
%{_datadir}/locale/*
%{_datadir}/help/*
%{_datadir}/glib-2.0/*
%{_datadir}/icons/hicolor/*
%{_metainfodir}/*.xml

%changelog
