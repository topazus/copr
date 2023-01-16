%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname croc
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Easily and securely send things from one computer to another
License:        MIT
URL:            https://github.com/schollz/croc
Source:         https://github.com/schollz/croc/archive/master/%{appname}-master.tar.gz

BuildRequires: golang git


%description
croc is a tool that allows any two computers to simply and securely transfer files and folders.

%prep
%autosetup -n %{appname}-master -p1

%build
go build

%install
install -pDm755 croc %{buildroot}%{_bindir}/croc
install -pDm644 croc.service %{buildroot}%{_prefix}/lib/systemd/system/croc.service

%if %{with check}
%check
go test ./...
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_prefix}/lib/systemd/system/croc.service

%changelog
