%define		_class		Mail
%define		_subclass	Mime
%define		upstream_name	%{_class}_%{_subclass}

Name:		php-pear-%{upstream_name}
Version:	1.8.1
Release:	%mkrel 4
Summary:	Mail_Mime provides classes to create mime messages
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/%{upstream_name}
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tgz
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Mail_Mime provides classes to deal with the creation and manipulation of mime
messages. It allows people to create Email messages consisting of:
* Text Parts
* HTML Parts
* Inline HTML Images
* Attachments
* Attached messages

Starting with version 1.4.0, it also allows non US-ASCII chars in filenames,
subjects, recipients, etc, etc.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}



%files
%defattr(-,root,root)
%{_datadir}/pear/%{_class}
%{_datadir}/pear/data/%{upstream_name}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.8.1-2mdv2011.0
+ Revision: 667622
- mass rebuild

* Thu Jan 27 2011 Adam Williamson <awilliamson@mandriva.org> 1.8.1-1
+ Revision: 633171
- new release 1.8.1

* Sat Aug 14 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.8.0-1mdv2011.0
+ Revision: 569597
- update to new version 1.8.0

* Sun Apr 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.7.0-1mdv2010.1
+ Revision: 538753
- update to new version 1.7.0

* Sun Apr 04 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.2-1mdv2010.1
+ Revision: 531325
- update to new version 1.6.2

* Sun Feb 21 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.6.0-1mdv2010.1
+ Revision: 508990
- update to new version 1.6.0

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.3-1mdv2010.1
+ Revision: 489152
- update to new version 1.5.3

* Wed Nov 25 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.2-6mdv2010.1
+ Revision: 470147
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Sun Sep 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.5.2-5mdv2010.0
+ Revision: 450223
- use pear installer
- use fedora %%post/%%postun

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.5.2-4mdv2010.0
+ Revision: 441293
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-3mdv2009.1
+ Revision: 322355
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.5.2-2mdv2009.0
+ Revision: 236917
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jul 26 2007 Adam Williamson <awilliamson@mandriva.org> 1.5.2-1mdv2008.0
+ Revision: 55632
- Import php-pear-Mail_Mime

