%global     reponame  rpmfusion
%global     repoversion free

Name:       %{reponame}-%{repoversion}-appstream-data
Version:    26
Release:    2%{?dist}
Summary:    Appstream metadata for the RPM Fusion free repository
BuildArch:  noarch

License:    CC0
URL:        http://rpmfusion.org

# mkdir rpmfusion-free/packages -p

# cd rpmfusion-free
# rsync -avPh rsync://rsync.mirrorservice.org/download1.rpmfusion.org/free/fedora/development/rawhide/Everything/x86_64/os/* .
# rm -rf repo*

# appstream-builder --verbose --max-threads=6 --log-dir=./logs/ \
# --packages-dir=./Packages/ --temp-dir=./tmp/ --output-dir=./appstream-data/ \
# --basename="rpmfusion-free-26" --origin="rpmfusion-free-26" \
# --enable-hidpi

# cp appstream-data/* ~/rpmbuild/SOURCES/
Source0:    %{reponame}-%{repoversion}-%{version}.xml.gz
Source1:    %{reponame}-%{repoversion}-%{version}-icons.tar.gz

BuildRequires:  libappstream-glib
Supplements:    appstream-data

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
* Sun Jul 09 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 26-2
- Regenerate and update for GA

* Mon Nov 14 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 26-1
- Regenerate and update for f26

* Mon Nov 14 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 25-3
- Add weak dep on Fedora appstream data

* Mon Nov 14 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 25-2
- Regenerate and update

* Mon Jul 25 2016 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 25-1
- Initial build for rawhide

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
