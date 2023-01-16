%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname zenith

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        terminal graphical metrics for your *nix system written in Rust
License:        MIT
URL:            https://github.com/bvaisvil/zenith
#Source:

BuildRequires:  gcc-c++ pkg-config git

%description
terminal graphical metrics for your *nix system written in Rust

%prep
git clone --depth=1 https://github.com/bvaisvil/zenith .

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm755 target/release/zenith %{buildroot}/usr/bin/zenith

install -pDm644 assets/zenith.png %{buildroot}%{_datadir}/pixmaps/zenith.png
install -pDm644 assets/zenith.desktop %{buildroot}%{_datadir}/applications/zenith.desktop

%check


%files
%{_bindir}/%{appname}
%{_datadir}/pixmaps/zenith.png
%{_datadir}/applications/zenith.desktop


%changelog
