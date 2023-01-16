%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname clapper
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A GNOME media player built using GJS with GTK4 toolkit and powered by GStreamer with OpenGL rendering
License:        GPL-3.0
URL:            https://github.com/Rafostar/clapper
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ desktop-file-utils cmake pkg-config meson ninja-build libappstream-glib
BuildRequires: gobject-introspection-devel gtk4-devel gjs-devel


# gstreamer
BuildRequires: gstreamer1-devel gstreamer1-plugins-base-tools gstreamer1-plugins-base-devel gstreamer1-plugins-good gstreamer1-plugins-good-extras gstreamer1-plugins-ugly-free gstreamer1-plugins-bad-free gstreamer1-plugins-bad-free-devel gstreamer1-plugins-bad-free-extras

Requires: gstreamer1-devel gstreamer1-plugins-base-tools gstreamer1-plugins-base-devel gstreamer1-plugins-good gstreamer1-plugins-good-extras gstreamer1-plugins-ugly-free gstreamer1-plugins-bad-free gstreamer1-plugins-bad-free-devel gstreamer1-plugins-bad-free-extras
%description
A GNOME media player built using GJS with GTK4 toolkit and powered by GStreamer with OpenGL rendering.

%prep
%autosetup -n %{appname}-master -p1

%build
%meson
%meson_build

%install
%meson_install

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.xml

%if %{with check}
%check
%meson_test
%endif

%files
%doc README.md
%{_bindir}/com.github.rafostar.Clapper*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/*.svg

%dir %{_libdir}/com.github.rafostar.Clapper
%{_libdir}/com.github.rafostar.Clapper/*
%dir %{_datadir}/com.github.rafostar.Clapper/
%{_datadir}/com.github.rafostar.Clapper/*

%{_datadir}/gir-1.0/GstClapper-1.0.gir
%{_datadir}/glib-2.0/schemas/*.xml

%{_datadir}/metainfo/*.xml
%{_datadir}/mime/packages/*.xml

%changelog
