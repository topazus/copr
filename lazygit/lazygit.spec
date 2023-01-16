%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname lazygit
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        simple terminal UI for git commands
License:        MIT
URL:            https://github.com/jesseduffield/lazygit
Source:         https://github.com/jesseduffield/lazygit/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ make pkg-config golang git wget


%description
A simple terminal UI for git commands, written in Go with the gocui library.

%prep
%autosetup -n %{appname}-master -p1

%build
go build -v

%install
install -pDm755 lazygit %{buildroot}%{_bindir}/lazygit


%if %{with check}
%check
go test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
