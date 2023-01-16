%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname stacer
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Linux System Optimizer and Monitoring
License:        GPL-3.0
URL:            https://github.com/oguzhaninan/Stacer
Source:         %{url}/archive/native/Stacer-native.tar.gz

BuildRequires:  gcc-c++ desktop-file-utils make cmake
BuildRequires:  qt5-qtbase-devel qt5-qtcharts-devel qt5-linguist
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Charts)
BuildRequires:  pkgconfig(Qt5Svg)


%description
Linux System Optimizer and Monitoring

%prep
%autosetup -n Stacer-native -p1

%build
cmake -DCMAKE_BUILD_TYPE=Release
make
# Build translations
lrelease-qt5 stacer/stacer.pro

%install
mkdir -p %{buildroot}%{_libdir}/stacer
install -pDm0755 output/stacer %{buildroot}%{_libdir}/stacer/stacer
mkdir -p %{buildroot}%{_bindir}
ln -s %{_libdir}/stacer/stacer %{buildroot}%{_bindir}/stacer

install -pDm0644 applications/stacer.desktop %{buildroot}%{_datadir}/applications/%{appname}.desktop

for i in 16 32 64 128 256; do
  install -pDm0644 icons/hicolor/${i}x${i}/apps/stacer.png %{buildroot}%{_datadir}/icons/hicolor/${i}x${i}/apps/%{appname}.png
done

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}%{_libdir}/stacer/translations
install -pDm0644 translations/*qm %{buildroot}%{_libdir}/%{appname}/translations/

%find_lang stacer --with-qt

%files -f stacer.lang
%license LICENSE*
%doc README.md
%{_libdir}/stacer
%{_libdir}/stacer/stacer
%{_bindir}/%{appname}

%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/*/apps/stacer.png

%{_libdir}/%{appname}/translations/*

%changelog
