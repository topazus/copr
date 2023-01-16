%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname pazi
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        An autojump "zap to directory" helper
License:        GPL 3.0
URL:            https://github.com/euank/pazi
Source:         https://github.com/euank/pazi/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ make pkg-config cargo

%description
Pazi is an autojump utility. That is to say, pazi remembers visited directories in the past and makes it easier to get back to them.

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release

%install
install -pDm755 target/release/pazi %{buildroot}%{_bindir}/%{appname}

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
