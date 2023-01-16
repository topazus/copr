%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname tre-command

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        Tree command, improved
License:        MIT
URL:            https://github.com/dduan/tre
Source:         https://github.com/dduan/tre/archive/main/%{appname}-main.tar.gz

BuildRequires:  gcc-c++ make pkg-config
BuildRequires:  git

%description
A modern alternative to the tree command.

%prep
git clone --depth=1 https://github.com/dduan/tre .

if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm755 target/release/tre %{buildroot}%{_bindir}/tre

install -pDm644 scripts/completion/tre.bash %{buildroot}%{_datadir}/bash-completion/completions/%{appname}
install -pDm644 extra/completions/_tre %{buildroot}%{_datadir}/zsh/site-functions/_%{appname}
install -pDm644 extra/completions/tre.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{appname}.fish

install -pDm644 manual/tre.1 %{buildroot}%{_mandir}/man1/tre.1

%check

%files
%{_bindir}/tre
%{_datadir}/bash-completion/completions/%{appname}
%{_datadir}/zsh/site-functions/_%{appname}
%{_datadir}/fish/vendor_completions.d/%{appname}.fish
%{_mandir}/man1/tre.1

%changelog
