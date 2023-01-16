%global debug_package %{nil}
%global build_timestamp %{lua: print(os.date("%Y.%m.%d"))}
%global appname leiningen

Name:           %{appname}-git
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        automating Clojure projects without setting your hair on fire
License:        EPL-1.0
URL:            https://github.com/technomancy/leiningen
#Source:


BuildRequires:  gcc gcc-c++ make java-17-openjdk git wget

%description
Leiningen is for automating Clojure projects without setting your hair on fire.

%prep
git clone --depth=1 https://github.com/technomancy/leiningen .
wget https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein
chmod +x lein

%build
cd leiningen-core/
../lein bootstrap
cd ../
bin/lein uberjar

%install
mkdir -p %{buildroot}%{_datadir}/java/
cp -r ./target/leiningen-*-standalone.jar %{buildroot}%{_datadir}/java/
install -m 0755 -D bin/lein-pkg %{buildroot}%{_bindir}/lein
install -m 0644 -D bash_completion.bash %{buildroot}%{_datadir}/bash-completion/completions/lein
install -m 0644 -D zsh_completion.zsh %{buildroot}%{_sysconfdir}/zsh_completion.d/_lein
install -m 0644 -D doc/lein.1 %{buildroot}%{_mandir}/man1/lein.1


%check

%files
/etc/zsh_completion.d/_lein
/usr/bin/lein
/usr/share/bash-completion/completions/lein
/usr/share/java/leiningen-*-standalone.jar
/usr/share/man/man1/lein.1.gz

%changelog
