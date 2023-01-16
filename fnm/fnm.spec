%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname fnm

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Fast and simple Node.js version manager, built in Rust
License:        GPL
URL:            https://github.com/Schniz/fnm
Source:         https://github.com/Schniz/fnm/archive/master/%{appname}-master.tar.gz


BuildRequires: cargo pkg-config

%description
Fast and simple Node.js version manager, built in Rust.

%prep
%autosetup -n %{appname}-master -p1

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi


%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm755 target/release/fnm %{buildroot}%{_bindir}/fnm

./target/release/fnm completions --shell bash > fnm.bash
install -pDm644 fnm.bash %{buildroot}%{_datadir}/bash-completion/completions/fnm
./target/release/fnm completions --shell zsh > fnm.zsh
install -pDm644 fnm.zsh %{buildroot}%{_datadir}/zsh/site-functions/_fnm
./target/release/fnm completions --shell fish > fnm.fish
install -pDm644 fnm.fish %{buildroot}%{_datadir}/fish/vendor_conf.d/fnm.fish

%check


%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}

%{_datadir}/bash-completion/completions/*
%{_datadir}/zsh/site-functions/_*
%{_datadir}/fish/vendor_conf.d/*.fish

%changelog
