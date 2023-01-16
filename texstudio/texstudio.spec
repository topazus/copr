%global debug_package %{nil}
%define build_date %{lua: print(os.date("%Y%m%d"))}

Name:           texstudio-git
Version:        0.0.0
Release:        %{build_date}%{?dist}
Summary:        fully featured LaTeX editor
License:        GPL v3.0
URL:            https://github.com/texstudio-org/texstudio
Source0:        https://github.com/texstudio-org/texstudio/archive/master/texstudio-master.tar.gz

BuildRequires:  make gcc-c++ pkg-config
BuildRequires:  qt5-qtbase-devel qt5-qtdeclarative-devel
BuildRequires:  qt5-qttools-devel qt5-qttools-static
BuildRequires:  qt5-qtsvg-devel qt5-qtscript-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  qtsingleapplication-qt5-devel
BuildRequires:  qtsinglecoreapplication-qt5-devel
BuildRequires:  quazip-qt5-devel

BuildRequires:  qtermwidget-devel
BuildRequires:  hunspell-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  zlib-devel


Requires:       tex-dvipng qt5-qtsvg qtermwidget

Recommends:     okular evince

%description
TeXstudio is a fully featured LaTeX editor. Our goal is to make writing LaTeX documents as easy and comfortable as possible.

%prep
%autosetup -n %{appname}-master -p1

%build
qmake-qt5 texstudio.pro
make

%install
make install INSTALL_ROOT=%{buildroot}

for size in 16 22 32 48 64; do
  install -Dp -m 0644 utilities/texstudio${size}x${size}.png %{buildroot}%{_datadir}/icons/hicolor/${size}x${size}/apps/texstudio.png
done

rm -rf %{buildroot}%{_datadir}/texstudio/*


%files
%{_bindir}/%{appname}
%dir %{_datadir}/texstudio/

%{_datadir}/applications/texstudio.desktop
%{_datadir}/metainfo/texstudio.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/*/apps/*.svg

%changelog
