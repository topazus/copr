%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname lf

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Terminal file manager
License:        MIT
URL:            https://github.com/gokcehan/lf
Source:         https://github.com/gokcehan/lf/archive/master/%{appname}-master.tar.gz

BuildRequires: golang git


%description
lf (as in "list files") is a terminal file manager written in Go. It is heavily inspired by ranger with some missing and extra features.

%prep
%autosetup -n %{appname}-master -p1

%build
go build -v


%install
install -pDm755 lf %{buildroot}%{_bindir}/lf

gzip --best lf.1
install -pDm644 lf.1.gz %{buildroot}%{_datadir}/man/man1/lf.1.gz

install -pDm644 etc/lf.bash %{buildroot}%{_datadir}/bash-completion/completions/lf
install -pDm644 etc/lf.zsh %{buildroot}%{_datadir}/zsh/site-functions/_lf
install -pDm644 etc/lf.fish %{buildroot}%{_datadir}/fish/vendor_conf.d/lf.fish

%check


%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/man/man1/lf.1.gz

%{_datadir}/bash-completion/completions/lf
%{_datadir}/zsh/site-functions/_lf
%{_datadir}/fish/vendor_conf.d/lf.fish

%changelog
