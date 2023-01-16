%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname zola

Name:           %{appname}-git
Version:       %{build_timestamp}
Release:       1%{?dist}
Summary:       Fast static site generator in a single binary with everything built-in
License:       MIT and ASL 2.0
URL:           https://github.com/getzola/zola
Source0:       %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires: gcc-g++

%description
A fast static site generator in a single binary with everything built-in.

%prep
git clone --depth=1 https://github.com/getzola/zola .

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
install -p -D -m755 target/release/zola %{buildroot}%{_bindir}/zola

install -Dp -m0644 completions/zola.bash %{buildroot}%{_datadir}/bash-completion/completions/%{appname}
install -Dp -m0644 completions/_zola %{buildroot}%{_datadir}/zsh/site-functions/_%{appname}
install -Dp -m0644 completions/zola.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{appname}.fish

%check

%files
%{_bindir}/zola
%{_datadir}/bash-completion/completions/%{appname}
%{_datadir}/zsh/site-functions/_%{appname}
%{_datadir}/fish/vendor_completions.d/%{appname}.fish

%changelog
