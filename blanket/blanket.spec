%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname blanket

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Listen to different sounds
License:        GPL-3.0
URL:            https://github.com/rafaelmardojai/blanket
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ meson ninja-build libappstream-glib glib2-devel gettext desktop-file-utils

Requires:  libhandy1 python3-gstreamer1 gtk3 python3-gobject

%description
Improve focus and increase your productivity by listening to different sounds. Or allows you to fall asleep in a noisy environment.

%prep
%autosetup -n %{appname}-master -p1

%build
%meson
%meson_build

%install
%meson_install


appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/blanket/*
%{_datadir}/glib-2.0/*
%{_datadir}/icons/hicolor
%{_datadir}/locale
%{_metainfodir}/*.xml

%changelog
