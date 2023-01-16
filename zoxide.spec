%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname zoxide

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Faster way to navigate your filesystem
License:        MIT
URL:            https://github.com/ajeetdsouza/zoxide
Source:         %{url}/archive/main/%{appname}-main.tar.gz

BuildRequires:  gcc-c++ git

%description
Faster way to navigate your filesystem.

%prep
git clone --depth=1 %{url} .

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm755 target/release/%{appname} %{buildroot}%{_bindir}/%{appname}

install -pDm644 contrib/completions/zoxide.bash %{buildroot}%{_datadir}/bash-completion/completions/zoxide
install -pDm644 zoxide.plugin.zsh %{buildroot}%{_datadir}/zsh/site-functions/_zoxide
install -pDm644 init.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/zoxide.fish

%check

%files
%{_bindir}/zoxide
%{_datadir}/bash-completion/completions/zoxide
%{_datadir}/fish/vendor_completions.d/zoxide.fish
%{_datadir}/zsh/site-functions/_zoxide

%changelog
