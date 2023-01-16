%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y%m%d"))}
%global appname girouette
%bcond_without check

Name:           %{appname}-git
Version:        0.0.0
Release:        %{build_timestamp}%{?dist}
Summary:        Show the weather in the terminal, in style
License:        MIT and APACHE
URL:            https://github.com/gourlaysama/girouette
Source:         %{url}/archive/main/%{appname}-main.tar.gz

BuildRequires:  cargo dbus-devel openssl-devel

%description
Girouette is a command line tool that displays the current weather (from OpenWeather) in the terminal.

%prep
%autosetup -n %{appname}-main -p1

%build
cargo build --release

%install
install -pDm755 target/release/girouette %{buildroot}%{_bindir}/girouette

install -pDm644 target/release/build/girouette-*/out/girouette.bash %{buildroot}%{_datadir}/bash-completion/completions/girouette
install -pDm644 target/release/build/girouette-*/out/_girouette %{buildroot}%{_datadir}/zsh/site-functions/_girouette
install -pDm644 target/release/build/girouette-*/out/girouette.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/girouette.fish

%if %{with check}
%check
cargo test
%endif

%files
%license LICENSE*
%doc README.md
%{_bindir}/%{appname}
%{_datadir}/bash-completion/completions/girouette
%{_datadir}/zsh/site-functions/_girouette
%{_datadir}/fish/vendor_completions.d/girouette.fish

%changelog
