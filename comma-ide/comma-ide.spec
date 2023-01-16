%global debug_package %{nil}

# Disable build-id symlinks to avoid conflicts
%global _build_id_links none
# don't strip bundled binaries because pycharm checks length (!!!) of binary fsnotif
# and if you strip debug stuff from it, it will complain
%global __strip /bin/true
# dont repack jars
%global __jar_repack %{nil}
# disable rpath checks
%define __brp_check_rpaths %{nil}

%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}

Name:           comma-ide
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        The Integrated Development Environment for Raku.
License:        custom
URL:            https://commaide.com/
Source1:        https://raw.githubusercontent.com/topazus/fedora-copr/main/comma-ide/comma-ide.desktop

BuildRequires:  pkg-config desktop-file-utils wget
Requires:       jetbrains-jre

%description
The Integrated Development Environment for Raku.

%prep
wget https://commaide.com/download/community/linux
tar xf linux
cd comma-community-*/

# Replace python shebangs to make them compatible with fedora
find -type f -name "*.py" -exec sed -e 's|/usr/bin/env python|%{__python3}|g' \
                                    -i "{}" \;
find -type f -name "*.sh" -exec sed -e 's|/bin/sh|/usr/bin/sh|g' \
                                    -i "{}" \;

# remove bundled jre
rm -rf jbr

rm -rf ./lib/pty4j-native/linux/{aarch64,arm,mips64el,ppc64le}

%build

%install
cd comma-community-*/
mkdir -p %{buildroot}/opt/%{name}
cp -a * %{buildroot}/opt/%{name}
mkdir -p %{buildroot}/etc/profile.d/
echo "export COMMA_JDK=/usr/lib/jvm/jetbrains-jre" \
  >> %{buildroot}/etc/profile.d/comma.sh

install -pDm644 bin/comma.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

install -pDm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop

%check


%files
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop
%dir /opt/%{name}
/opt/%{name}/*

/etc/profile.d/comma.sh

%changelog
