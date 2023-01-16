%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname micro
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A modern and intuitive terminal-based text editor
License:        MIT
URL:            https://github.com/zyedidia/micro
Source:         https://github.com/zyedidia/micro/archive/master/%{appname}-master.tar.gz

BuildRequires: golang git


%description
lf (as in "list files") is a terminal file manager written in Go. It is heavily inspired by ranger with some missing and extra features.

%prep
%autosetup -n %{appname}-master -p1

%build
go build -v ./cmd/micro

%install
install -pDm755 micro %{buildroot}%{_bindir}/micro

install -pDm644 assets/packaging/micro.desktop %{buildroot}%{_datadir}/applications/*.desktop
install -pDm644 assets/micro-logo-mark.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/micro.svg

gzip --best assets/packaging/micro.1
install -pDm644 assets/packaging/micro.1.gz %{buildroot}%{_datadir}/man/man1/micro.1.gz

%if %{with check}
%check
go test ./internal/...
go test ./cmd/...
%endif


%files
%license LICENSE*
%doc README.md
%{_bindir}/micro

%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/scalable/apps/micro.svg
%{_datadir}/man/man1/micro.1.gz

%changelog
