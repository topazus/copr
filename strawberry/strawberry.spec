%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname strawberry
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        🍓 Strawberry Music Player
License:        GPL-3.0
URL:            https://github.com/strawberrymusicplayer/strawberry
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ desktop-file-utils make cmake appstream libappstream-glib
BuildRequires: qt5-qttools-devel boost-devel protobuf-devel sqlite-devel
BuildRequires: libchromaprint-devel alsa-lib-devel dbus-devel
BuildRequires: pulseaudio-libs-devel gstreamer1-devel gnutls-devel
BuildRequires: taglib-devel libcdio-devel libmtp-devel libgpod-devel
BuildRequires: fftw-devel

# gstreamer
BuildRequires: gstreamer1-devel gstreamer1-plugins-base-tools gstreamer1-plugins-base-devel gstreamer1-plugins-good gstreamer1-plugins-good-extras gstreamer1-plugins-ugly-free gstreamer1-plugins-bad-free gstreamer1-plugins-bad-free-devel gstreamer1-plugins-bad-free-extras

Requires: gstreamer1-devel gstreamer1-plugins-base-tools gstreamer1-plugins-base-devel gstreamer1-plugins-good gstreamer1-plugins-good-extras gstreamer1-plugins-ugly-free gstreamer1-plugins-bad-free gstreamer1-plugins-bad-free-devel gstreamer1-plugins-bad-free-extras


%description
Strawberry is a music player and music collection organizer. It is a fork of Clementine released in 2018 aimed at music collectors and audiophiles. It's written in C++ using the Qt toolkit.

%prep
%autosetup -n %{appname}-master -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%if %{with check}
%check
%ctest
%endif

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc README.md
%{_bindir}/%{appname}
%{_bindir}/strawberry-tagreader
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/strawberry.png
%{_datadir}/man/man1/strawberry-tagreader.1.gz
%{_datadir}/man/man1/strawberry.1.gz
%{_metainfodir}/*.xml

%changelog
