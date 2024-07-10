%global     reponame  rpmfusion
%global     repoversion free

Name:       %{reponame}-%{repoversion}-appstream-data
Version:    41
Release:    1%{?dist}
Summary:    Appstream metadata for the RPM Fusion free repository
BuildArch:  noarch

License:    CC0
URL:        http://rpmfusion.org

Source0:    %{reponame}-%{repoversion}-%{version}.xml.gz
Source1:    %{reponame}-%{repoversion}-%{version}-icons.tar.gz
# script to generate appdata
Source2:    update-appdata-rpmfusion-free.sh

BuildRequires:  libappstream-glib
Supplements:    appstream-data

%description
Appstream metadata for packages in the RPM Fusion free repository


%prep


%build


%install
DESTDIR=%{buildroot} appstream-util install %{SOURCE0} %{SOURCE1}

# temporarily move to make Discover happy:
# https://bugzilla.rpmfusion.org/show_bug.cgi?id=7000
mv %{buildroot}%{_datadir}/app-info %{buildroot}%{_datadir}/swcatalog
mv %{buildroot}%{_datadir}/swcatalog/xmls %{buildroot}%{_datadir}/swcatalog/xml


%files
%attr(0644,root,root) %{_datadir}/swcatalog/xml/%{reponame}-%{repoversion}-%{version}.xml.gz
%{_datadir}/swcatalog/icons/%{reponame}-%{repoversion}-%{version}/
%dir %{_datadir}/swcatalog
%dir %{_datadir}/swcatalog/icons
%dir %{_datadir}/swcatalog/xml

%changelog
* Wed Jul 10 2024 Ankur Sinha <sanjay.ankur@gmail.com> - 40-2
- Regenerate
- Move to new location to keep Discover happy

* Fri Apr 19 2024 Leigh Scott <leigh123linux@gmail.com> - 40-1
- Regenerate for F40

* Thu Oct 19 2023 Leigh Scott <leigh123linux@gmail.com> - 39-1
- Regenerate for F39

* Sun Feb 19 2023 Leigh Scott <leigh123linux@gmail.com> - 38-1
- Regenerate for F38

* Mon Apr 25 2022 Ankur Sinha <sanjay.ankur@gmail.com> - 37-4
- Regenerate

* Mon Apr 25 2022 Ankur Sinha <sanjay.ankur@gmail.com> - 37-3
- Regenerate

* Mon Apr 25 2022 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 37-2
- Regenerate

* Mon Feb 28 2022 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 37-1
- Regenerated for F37

* Wed Nov 03 2021 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 36-1
- Regenerated

* Mon Sep 28 2020 Leigh Scott <leigh123linux@gmail.com> - 34-2
- Regenerate

* Thu Sep 17 2020 Leigh Scott <leigh123linux@gmail.com> - 34-1
- Update for rawhide

* Thu Sep 10 2020 Leigh Scott <leigh123linux@gmail.com> - 33-2
- Regenerate for audacity-freeworld and openmw

* Thu Feb 20 2020 Leigh Scott <leigh123linux@gmail.com> - 33-1
- Update for rawhide

* Wed Nov 13 2019 Leigh Scott <leigh123linux@gmail.com> - 32-2
- Regenerate for chromium-freeworld and chromium-browser-privacy

* Sun Oct 27 2019 Leigh Scott <leigh123linux@gmail.com> - 32-1
- Update for rawhide

* Sun Oct 21 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 30-1.20181021
- Regenerate
- Include generation timestamp so that the package is more informative

* Sun Jul 08 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 29-3
- Update

* Mon Apr 02 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 29-2
- rebuilt

* Sat Mar 31 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 29-1
- Rebuild for f29

* Mon Nov 13 2017 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 28-1
- Update for rawhide

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
