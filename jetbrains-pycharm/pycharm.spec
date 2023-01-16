%global debug_package %{nil}

# do not automatically detect and export provides and dependencies on bundled libraries and executables
%global __provides_exclude_from /opt/%{name}/lib/.*|/opt/%{name}/plugins/.*
%global __requires_exclude_from /opt/%{name}/lib/.*|/opt/%{name}/plugins/.*

Name:           pycharm
Version:        2022.3.1
Release:        1%{?dist}
Summary:        The Python IDE for Professional Developers
License:        custom
URL:            https://www.jetbrains.com/pycharm/
Source0:        https://download.jetbrains.com/python/pycharm-professional-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/topazus/fedora-copr/main/jetbrains-pycharm/pycharm.desktop

BuildRequires:  pkg-config desktop-file-utils wget
Requires:       jetbrains-jre-git

%description
The Python IDE for Professional Developers.

%prep
%autosetup -n pycharm-%{version}

# Replace python shebangs to make them compatible with fedora
find -type f -name "*.py" -exec sed -e 's|/usr/bin/env python|%{__python3}|g' \
                                    -i "{}" \;
find -type f -name "*.sh" -exec sed -e 's|/bin/sh|/usr/bin/sh|g' \
                                    -i "{}" \;

# remove bundled jre
rm -rf jbr

rm -rf ./plugins/cwm-plugin/quiche-native/win32-x86-64
rm -rf ./plugins/cwm-plugin/quiche-native/darwin-aarch64
rm -rf ./plugins/cwm-plugin/quiche-native/darwin-x86-64

%build

%install
mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 bin/pycharm.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -pDm644 bin/pycharm.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -pDm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}/etc/profile.d
echo "export PYCHARM_JDK=/usr/lib/jvm/jetbrains-jre
" >> %{buildroot}/etc/profile.d/pycharm.sh

%check


%files
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
/etc/profile.d/pycharm.sh

%dir /opt/%{name}
/opt/%{name}/*

%changelog
