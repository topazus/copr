%global debug_package %{nil}

# do not automatically detect and export provides and dependencies on bundled libraries and executables
%global __provides_exclude_from /opt/%{name}/lib/.*|/opt/%{name}/plugins/.*
%global __requires_exclude_from /opt/%{name}/lib/.*|/opt/%{name}/plugins/.*

Name:           clion
Version:        2022.3.1
Release:        1%{?dist}
Summary:        A Cross-Platform IDE for C and C++
License:        custom
URL:            https://www.jetbrains.com/clion/
Source0:        https://download.jetbrains.com/cpp/CLion-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/topazus/fedora-copr/main/jetbrains-clion/clion.desktop

BuildRequires:  pkg-config desktop-file-utils wget
Requires:       jetbrains-jre-git

%description
A Cross-Platform IDE for C and C++

%prep
%autosetup -n clion-%{version}

# Replace python shebangs to make them compatible with fedora
find -type f -name "*.py" -exec sed -e 's|/usr/bin/env python|%{__python3}|g' \
                                    -i "{}" \;
find -type f -name "*.sh" -exec sed -e 's|/bin/sh|/usr/bin/sh|g' \
                                    -i "{}" \;

# remove bundled jre
rm -rf jbr

rm -rf ./plugins/gateway-plugin/lib/remote-dev-workers/remote-dev-worker-darwin-amd64
rm -rf ./plugins/gateway-plugin/lib/remote-dev-workers/remote-dev-worker-darwin-arm64
rm -rf ./plugins/gateway-plugin/lib/remote-dev-workers/remote-dev-worker-windows-amd64.exe
rm -rf ./plugins/gateway-plugin/lib/remote-dev-workers/remote-dev-worker-windows-arm64.exe

rm -rf ./plugins/cwm-plugin/quiche-native/darwin-x86-64
rm -rf ./plugins/cwm-plugin/quiche-native/win32-x86-64
rm -rf ./plugins/cwm-plugin/quiche-native/darwin-aarch64

%build

%install
mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}

install -pDm644 bin/clion.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -pDm644 bin/clion.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -pDm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}/etc/profile.d
echo "export CLION_JDK=/usr/lib/jvm/jetbrains-jre
" >> %{buildroot}/etc/profile.d/clion.sh

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop
/etc/profile.d/clion.sh

%dir /opt/%{name}
/opt/%{name}/*

%changelog
