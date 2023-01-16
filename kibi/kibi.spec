%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname kibi
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A text editor in ≤1024 lines of code, written in Rust
License:        MIT
URL:            https://github.com/ilai-deutel/kibi
Source:         https://github.com/ilai-deutel/kibi/archive/master/%{appname}-master.tar.gz

BuildRequires: pkg-config cargo


%description
A configurable text editor with UTF-8 support, incremental search, syntax highlighting, line numbers and more, written in less than 1024 lines1 of Rust with minimal dependencies.

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release

%install
install -pDm755 target/release/kibi %{buildroot}%{_bindir}/kibi

# Install configuration files
install -pDm644 config_example.ini %{buildroot}/etc/kibi/config.ini
install -pDm644 syntax.d/* -t %{buildroot}%{_datadir}/kibi/syntax.d

%if %{with check}
%check
cargo test
%endif


%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
/etc/kibi/config.ini
%{_datadir}/kibi/syntax.d/

%changelog
