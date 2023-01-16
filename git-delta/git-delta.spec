%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname git-delta
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        A viewer for git and diff output
License:        MIT
URL:            https://github.com/dandavison/delta
Source:         https://github.com/dandavison/delta/archive/master/delta-master.tar.gz

BuildRequires: gcc-c++ make pkg-config

%description
A viewer for git and diff output

Code evolves, and we all spend time studying diffs. Delta aims to make this both efficient and enjoyable: it allows you to make extensive changes to the layout and styling of diffs, as well as allowing you to stay arbitrarily close to the default git/diff output.

%prep
%autosetup -n delta-master -p1
if [ ! -d $HOME/.cargo ]; then
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
fi

%build
$HOME/.cargo/bin/cargo build --release

%install
install -pDm755 target/release/delta %{buildroot}%{_bindir}/delta

install -pDm644 etc/completion/completion.bash %{buildroot}%{_datadir}/bash-completion/delta.bash
install -Dpm644 etc/completion/completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/_delta

%if %{with check}
%check

%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/delta
%{_datadir}/bash-completion/delta.bash
%{_datadir}/zsh/site-functions/_delta

%changelog
