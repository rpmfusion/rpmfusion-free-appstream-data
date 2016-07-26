%global     reponame  rpmfusion
%global     repoversion free

Name:       %{reponame}-%{repoversion}-appstream-data
Version:    24
Release:    1%{?dist}
Summary:    Appstream metadata for the RPM Fusion free repository
BuildArch:  noarch

License:    CC0
URL:        http://rpmfusion.org

# mkdir rpmfusion-free

# cd rpmfusion-free
# rsync -avPh rsync://rsync.mirrorservice.org/download1.rpmfusion.org/free/fedora/releases/24/Everything/x86_64/os/* .
# rm -rf repo*

# appstream-builder --verbose --max-threads=6 --log-dir=./logs/ \
# --packages-dir=./Packages/ --temp-dir=./tmp/ --output-dir=./appstream-data/ \
# --enable-hidpi --basename="rpmfusion-free-24" --origin="rpmfusion-free-24"

Source0:    %{reponame}-%{repoversion}-%{version}.xml.gz
# No icons found apparently
#Source1:    %{reponame}-%{repoversion}-%{version}-icons.tar.gz
#Source2:   %{reponame}-%{repoversion}-%{version}-screenshots.tar

BuildRequires: libappstream-glib

%description
Appstream metadata for packages in the RPM Fusion free repository


%prep


%build


%install
DESTDIR=%{buildroot} appstream-util install %{SOURCE0} # %{SOURCE1}


%files
%attr(0644,root,root) %{_datadir}/app-info/xmls/%{reponame}-%{repoversion}-%{version}.xml.gz
# %{_datadir}/app-info/icons/%{reponame}-%{repoversion}-%{version}/
#%dir %{_datadir}/app-info/icons
%dir %{_datadir}/app-info
%dir %{_datadir}/app-info/xmls

%changelog
* Tue Jul 26 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 24-1
- Initial build for f24

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
