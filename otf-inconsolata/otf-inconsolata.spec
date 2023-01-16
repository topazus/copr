%global debug_package %{nil}

Name:           otf-inconsolata
Version:        3.000
Release:        1%{?dist}
Summary:        Inconsolata fonts
License:        OFL
URL:            https://github.com/googlefonts/Inconsolata
Source:         https://github.com/googlefonts/Inconsolata/releases/download/v%{version}/fonts_otf.zip

BuildRequires:  gcc make python3
BuildRequires:  libxml2-devel libxslt-devel libgit2-devel

%description
A monospace font, designed for code listings and the like, in print.

%prep
git clone --depth=1 https://github.com/googlefonts/Inconsolata .

if [ ! -d $HOME/miniconda ]; then
    #Downloading the latest Miniconda installer for Linux. Your architecture may vary.
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh -b -p $HOME/miniconda
fi

%build
eval "$($HOME/miniconda/bin/conda shell.YOUR_SHELL_NAME hook)"

$HOME/miniconda/bin/conda create -n build-inconsolata python=3.9
$HOME/miniconda/bin/conda activate build-inconsolata
pip install -r requirements.txt -y

cd sources
sh build.sh

%install
install -d %{buildroot}%{_datadir}/fonts/%{name}
install -pDm644 otf/Inconsolata-Bold.otf -t %{buildroot}%{_datadir}/fonts/%{name}
install -pDm644 otf/Inconsolata-Light.otf -t %{buildroot}%{_datadir}/fonts/%{name}
install -pDm644 otf/Inconsolata-Medium.otf -t %{buildroot}%{_datadir}/fonts/%{name}
install -pDm644 otf/Inconsolata-Regular.otf -t %{buildroot}%{_datadir}/fonts/%{name}
install -pDm644 otf/Ligconsolata-Bold.otf -t %{buildroot}%{_datadir}/fonts/%{name}
install -pDm644 otf/Ligconsolata-Regular.otf -t %{buildroot}%{_datadir}/fonts/%{name}

%check


%files
%dir %{_datadir}/fonts/%{name}
%{_datadir}/fonts/%{name}/*.otf

%changelog
