
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname skim
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Fuzzy Finder in rust!
License:        MIT
URL:            https://github.com/lotabout/skim
Source:         %{url}/archive/master/%{appname}-master.tar.gz

BuildRequires:  gcc-c++ cargo rust-packaging


%description
Half of our life is spent on navigation: files, lines, commands… You need skim! It is a general fuzzy finder that saves you time.

%prep
%autosetup -n %{appname}-master -p1

%build
cargo build --release

%install
install -pDm755 target/release/sk %{buildroot}%{_bindir}/sk
install -pDm755 bin/sk-tmux %{buildroot}%{_bindir}/sk-tmux

install -pDm644 shell/completion.bash %{buildroot}%{_datadir}/bash-completion/completions/skim
install -pDm644 shell/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/_skim

install -Dpm0644 -t %{buildroot}%{_mandir}/man1 man/man1/*

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/sk
%{_datadir}/bash-completion/completions/skim
%{_datadir}/zsh/site-functions/_skim
%{_datadir}/man/man1/sk.1
%{_datadir}/man/man1/sk-tmux.1

%changelog
