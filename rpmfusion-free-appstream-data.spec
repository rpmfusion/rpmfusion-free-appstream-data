%global     reponame  rpmfusion
%global     repoversion free

Name:       %{reponame}-%{repoversion}-appstream-data
Version:    22
Release:    5%{?dist}
Summary:    Appstream metadata for the RPM Fusion free repository
BuildArch:  noarch

License:    CC0
URL:        http://rpmfusion.org

# mkdir rpmfusion-free/packages -p

# cd rpmfusion-free/packages
# rsync -avPh rsync://rsync.mirrorservice.org/download1.rpmfusion.org/free/fedora/development/22/x86_64/os/* .
# cd ..

# appstream-builder --verbose --max-threads=6 --log-dir=./logs/ \
# --packages-dir=./packages/ --temp-dir=./tmp/ --output-dir=./appstream-data/ \
# --basename="rpmfusion-free-22"
# --origin="rpmfusion-free-22"
# --screenshot-uri="http://ankursinha.fedorapeople.org/rpmfusion-appdata/free/"

# cp appstream-data/* ~/rpmbuild/SOURCES/
Source0:    %{reponame}-%{repoversion}-%{version}.xml.gz
Source1:    %{reponame}-%{repoversion}-%{version}-icons.tar.gz
#Source2:   %{reponame}-%{repoversion}-%{version}-screenshots.tar

BuildRequires: libappstream-glib

%description
Appstream metadata for packages in the RPM Fusion free repository


%prep


%build


%install
DESTDIR=%{buildroot} appstream-util install %{SOURCE0} %{SOURCE1}


%files
%attr(0644,root,root) %{_datadir}/app-info/xmls/%{reponame}-%{repoversion}-%{version}.xml.gz
%{_datadir}/app-info/icons/%{reponame}-%{repoversion}-%{version}/
%dir %{_datadir}/app-info
%dir %{_datadir}/app-info/icons
%dir %{_datadir}/app-info/xmls

%changelog
* Tue Mar 08 2016 Nicolas Chauvet <kwizart@gmail.com> - 22-5
- Fix project name

* Wed May 27 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 22-4
- Added some more appdata files

* Fri May 22 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 22-3
- regenerate with screenshot support

* Fri May 22 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 22-2
- Update - also specify origin when generating data

* Thu May 21 2015 Ankur Sinha <ankursinha AT fedoraproject DOT org> 22-1
- Initial build
