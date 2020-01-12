%global     reponame  rpmfusion
%global     repoversion free

Name:       %{reponame}-%{repoversion}-appstream-data
Version:    8
Release:    1%{?dist}
Summary:    Appstream metadata for the RPM Fusion free el repository
BuildArch:  noarch

License:    CC0
URL:        http://rpmfusion.org

Source0:    %{reponame}-%{repoversion}-el%{version}.xml.gz
Source1:    %{reponame}-%{repoversion}-el%{version}-icons.tar.gz
# script to generate appdata
Source2:    update-appdata-rpmfusion-free.sh

BuildRequires:  libappstream-glib
Supplements:    appstream-data

%description
Appstream metadata for packages in the RPM Fusion free el repository


%prep


%build


%install
DESTDIR=%{buildroot} appstream-util install %{SOURCE0} %{SOURCE1}


%files
%attr(0644,root,root) %{_datadir}/app-info/xmls/%{reponame}-%{repoversion}-el%{version}.xml.gz
%{_datadir}/app-info/icons/%{reponame}-%{repoversion}-el%{version}/
%dir %{_datadir}/app-info
%dir %{_datadir}/app-info/icons
%dir %{_datadir}/app-info/xmls

%changelog
* Sun Jan 12 2020 Leigh Scott <leigh123linux@gmail.com> - 8-1
- Initial el build

