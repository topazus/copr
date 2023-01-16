%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname
%bcond_without check

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        
License:        
URL:            
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ cmake pkg-config meson ninja-build
BuildRequires: desktop-file-utils libappstream-glib
BuildRequires: python3-devel python3-setuptools python3-pytest

Requires:

Recommends:

%description


%prep
%autosetup -n %{appname}-master -p1

%build
%py3_build
%meson
%meson_build
%cmake
%cmake_build
cargo build --release

%install
%py3_install
%meson_install
%cmake_install

install -pDm644  %{buildroot}%{_datadir}/icons/hicolor/*/apps/*.png
install -pDm644 images/logo/clifm.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/*.svg

%if %{with check}
%check
%pytest
%meson_test
%ctest
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*/apps/*.png
%{python3_sitearch}
%{python3_sitelib}
%{python3_sitelib}/%{appname}/*
%{python3_sitelib}/*.egg-info/*
%{_datadir}
%{_datadir}/metainfo/*.appdata.xml

%{_datadir}/man/man1/*.1.gz

%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/_*
%{_datadir}/fish/vendor_conf.d/*.fish

%changelog
