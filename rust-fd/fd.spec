%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global _name fd

Name:           %{_name}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        simple, fast and user-friendly alternative to 'find'
License:        MIT
URL:            https://github.com/sharkdp/fd
Source:         %{url}/archive/master/%{_name}-master.tar.gz

BuildRequires: cargo

%description
A simple, fast and user-friendly alternative to 'find'.

%prep
%autosetup -n %{_name}-master -p1

%build

%install
install -p -D -m755 target/release/%{_name} %{buildroot}%{_bindir}/%{_name}

install -Dpm0644 doc/fd.1 %{buildroot}%{_mandir}/man1/fd.1

install -Dpm0644 target/release/build/fd-*/out/fd.bash %{buildroot}%{_datadir}/bash-completion/completions/%{_name}
install -Dpm0644 contrib/completion/_fd %{buildroot}%{_datadir}/zsh/site-functions/_%{_name}
install -Dpm0644 target/release/build/fd-*/out/fd.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/%{_name}.fish

%check
cargo test

%files
%license LICENSE-MIT LICENSE-APACHE
%doc README.md
%{_bindir}/%{_name}
%{_mandir}/man1/fd.1
%{_datadir}/bash-completion/completions/%{_name}
%{_datadir}/zsh/site-functions/_%{_name}
%{_datadir}/fish/vendor_completions.d/%{_name}.fish

%changelog
