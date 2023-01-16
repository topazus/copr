%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname flameshot

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Powerful yet simple to use screenshot software
License:        GPL
URL:            https://github.com/flameshot-org/flameshot
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ cmake pkg-config desktop-file-utils
BuildRequires:  qt5-qtbase-devel qt5-linguist qt5-qtsvg-devel

Requires:       qt5-qtbase qt5-qtsvg

%description
Powerful yet simple to use screenshot software.

%prep
%autosetup -n %{appname}-master -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*
%{_metainfodir}/*.metainfo.xml

%{_datadir}/bash-completion/completions/%{appname}
%{_datadir}/zsh/site-functions/_%{appname}
/usr/share/fish/vendor_completions.d/flameshot.fish

%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/services/*.service
%{_mandir}/man1/%{appname}.1*

%{_datadir}/flameshot/translations/Internationalization_*.qm

%changelog
