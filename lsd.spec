%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname lsd
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        The next gen ls command
License:        ASL 2.0
URL:            https://github.com/Peltoche/lsd
Source:         https://github.com/Peltoche/lsd/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ make pkg-config cargo

%description
This project is heavily inspired by the super colorls project but with some little differences. For example it is written in rust and not in ruby which makes it much faster.

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release

%install
install -pDm755 target/release/lsd %{buildroot}%{_bindir}/lsd

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%changelog
