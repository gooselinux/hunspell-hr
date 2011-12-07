Name: hunspell-hr
Summary: Croatian hunspell dictionaries
%define upstreamid 20040608
Version: 0.%{upstreamid}
Release: 4.1%{?dist}
Epoch: 1
Source: http://cvs.linux.hr/spell/myspell/hr_HR.zip
Group: Applications/Text
URL: http://cvs.linux.hr/spell/
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
License: LGPLv2+ or SISSL
BuildArch: noarch

Requires: hunspell

%description
Croatian hunspell dictionaries.

%package -n hyphen-hr
Requires: hyphen
Summary: Croatian hyphenation rules
Group: Applications/Text

%description -n hyphen-hr
Croatian hyphenation rules.

%prep
%setup -q -c -n hunspell-hr

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p hr_HR.dic hr_HR.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/hyphen
cp -p hyph_hr.dic $RPM_BUILD_ROOT/%{_datadir}/hyphen/hyph_hr_HR.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README_hr_HR.txt
%{_datadir}/myspell/*

%files -n hyphen-hr
%defattr(-,root,root,-)
%{_datadir}/hyphen/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 1:0.20040608-4.1
- Rebuilt for RHEL 6

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20040608-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.20040608-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Nov 22 2007 Caolan McNamara <caolanm@redhat.com> - 1:0.20040608-2
- package hyphenation rules

* Tue Aug 21 2007 Caolan McNamara <caolanm@redhat.com> - 1:0.20040608-1
- clarify license
- canonical upstream version

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 0.20060607-1
- initial version
