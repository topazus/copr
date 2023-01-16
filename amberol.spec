%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}

Name:           amberol
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        A small and simple sound and music player that is well integrated with GNOME
License:        GPL-3.0+
URL:            https://gitlab.gnome.org/World/amberol
Source0:        https://gitlab.gnome.org/World/amberol/-/archive/main/amberol-main.tar.gz

BuildRequires:  cargo cargo-packaging
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc m4 meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-player-1.0)
BuildRequires:  rust
BuildRequires:  libxml2-tools

%description
A small and simple sound and music player that is well integrated with GNOME.
Amberol aspires to be as small, unintrusive, and simple as possible. It does
not manage your music collection; it does not let you manage playlists, smart
or otherwise; it does not let you edit the metadata for your songs; it does
not show you lyrics for your songs, or the Wikipedia page for your bands.
Amberol plays music, and nothing else.

%prep
%autosetup -n %{name}-main

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES/GPL-3.0-or-later.txt
%doc README.md
%dir %{_datadir}/amberol
%{_bindir}/amberol
%{_datadir}/%{name}/%{name}.gresource
%{_datadir}/appdata/io.bassi.Amberol.appdata.xml
%{_datadir}/applications/io.bassi.Amberol.desktop
%{_datadir}/dbus-1/services/io.bassi.Amberol.service
%{_datadir}/glib-2.0/schemas/io.bassi.Amberol.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/io.bassi.Amberol.svg
%{_datadir}/icons/hicolor/symbolic/apps/io.bassi.Amberol-symbolic.svg

%changelog
