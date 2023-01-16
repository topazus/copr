%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname cobalt

Name:          %{appname}-git
Version:       0.0.0
Release:       %{build_timestamp}%{?dist}
Summary:       Static site generator written in Rust
License:       MIT
URL:           https://github.com/cobalt-org/cobalt.rs
Source0:       https://github.com/cobalt-org/cobalt.rs/archive/master/cobalt.rs-master.tar.gz

BuildRequires: cargo

%description
Static site generator written in Rust.

%prep
%autosetup -n cobalt.rs-master -p1

%build
# Without syntax highlighting / sass
# cargo build --no-default-features
cargo build --release --features 'syntax-highlight sass'

%install
install -Dm 755 target/release/cobalt %{buildroot}%{_bindir}/cobalt

%check
cargo test

%files
%license LICENSE
%doc README.md
%{_bindir}/cobalt

%changelog
