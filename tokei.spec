%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname tokei
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Count your code quickly
License:        ASL 2.0
URL:            https://github.com/XAMPPRocky/tokei
Source:         https://github.com/XAMPPRocky/tokei/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-c++ make pkg-config cargo

%description
Tokei is a program that displays statistics about your code. Tokei will show the number of files, total lines within those files and code, comments, and blanks grouped by language.

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release

%install
install -pDm755 target/release/tokei %{buildroot}%{_bindir}/tokei

%if %{with check}
%check
cargo test
%endif

%files
%license LICENCE*
%doc README.md
%{_bindir}/%{appname}

%changelog
