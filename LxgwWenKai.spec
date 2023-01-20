%global debug_package %{nil}
%define build_timestamp %{lua: print(os.date("%Y.%m.%d"))}

Name:           LxgwWenKai
Version:        %{build_timestamp}
Release:        1%{?dist}
Summary:        An open-source Chinese font derived from Fontworks' Klee One.

License:        ASL 2.0 or MIT
URL:            https://github.com/lxgw/LxgwWenKai
#Source:

BuildRequires:  pkg-config
BuildRequires:  python3 fonttools git

%description
Open source monospace/Nerd Font font with round corner for IDE and command line

%prep
git clone --depth=1 %{url} .

%build
cd sources/
mkdir -p output/otf
python3 build.py

%install
cd source/
%if 0%{?fedora}
mkdir -p %{buildroot}/usr/share/fonts/maple-font
install -pDm 0644 output/otf/*.otf %{buildroot}/usr/share/fonts/maple-font
%elif 0%{?suse_version}
mkdir -p %{buildroot}/usr/share/fonts/truetype/
install -pDm 0644 output/otf/*.otf %{buildroot}/usr/share/fonts/truetype/
%endif

%check

%files
%if 0%{?fedora}
%dir /usr/share/fonts/maple-font
/usr/share/fonts/maple-font/*.otf
%elif 0%{?suse_version}
/usr/share/fonts/truetype/*.otf
%endif

%changelog
