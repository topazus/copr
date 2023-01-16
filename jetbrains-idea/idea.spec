%global debug_package %{nil}

# do not automatically detect and export provides and dependencies on bundled libraries and executables
%global __provides_exclude_from /opt/%{name}/lib/.*|/opt/%{name}/plugins/.*
%global __requires_exclude_from /opt/%{name}/lib/.*|/opt/%{name}/plugins/.*

%global build_number 223.8214.52
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}

Name:           idea
Version:        2022.3.1
Release:        1%{?dist}
Summary:        An intelligent IDE for Java, Groovy and other programming languages
License:        custom
URL:            https://www.jetbrains.com/idea/
Source0:        https://download.jetbrains.com/idea/ideaIU-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/topazus/fedora-copr/main/jetbrains-idea/idea.desktop

BuildRequires:  pkg-config desktop-file-utils wget
Requires:       jetbrains-jre

%description
An intelligent IDE for Java, Groovy and other programming languages with advanced refactoring features intensely focused on developer productivity.

%prep
%setup -q -n idea-IU-%{build_number}

# Replace python shebangs to make them compatible with fedora
find -type f -name "*.py" -exec sed -e 's|/usr/bin/env python|%{__python3}|g' \
                                    -i "{}" \;
find -type f -name "*.sh" -exec sed -e 's|/bin/sh|/usr/bin/sh|g' \
                                    -i "{}" \;

# remove bundled jre
rm -rf jbr

%build

%install
mkdir -p %{buildroot}/opt/%{name}
cp -r * %{buildroot}/opt/%{name}

install -pDm644 bin/idea.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -pDm644 bin/idea.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg

install -pDm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

mkdir -p %{buildroot}/etc/profile.d
echo "export IDEA_JDK=%{_libdir}/jetbrains-jre
" >> %{buildroot}/etc/profile.d/idea.sh

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%dir /opt/%{name}
/opt/%{name}/*

/etc/profile.d/idea.sh
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/applications/%{name}.desktop

%changelog
