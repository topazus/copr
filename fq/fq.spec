%global debug_package %{nil}

Name:           fq
Version:        0.0.2
Release:        1%{?dist}
Summary:        jq for binary formats
License:        MIT
URL:            https://github.com/wader/fq.git
Source:         %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  gcc-c++ pkg-config
BuildRequires:  golang

%description
Tool, language and decoders for inspecting binary data.

%prep
%autosetup -n %{name}-%{version} -p1

%build
go build \
    -trimpath \
    -buildmode=pie \
    -mod=readonly \
    -modcacherw \
    -ldflags \
    "-s -w \
    -X 'github.com/dundee/gdu/v5/build.Version=%{version}' \
    -X 'github.com/dundee/gdu/v5/build.User=$(id -u -n)' \
    -X 'github.com/dundee/gdu/v5/build.Time=$(LC_ALL=en_US.UTF-8 date)'" \
    -o %{name} \
    ./cmd/gdu

%install
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
