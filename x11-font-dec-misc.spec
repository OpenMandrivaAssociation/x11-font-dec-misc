Name: x11-font-dec-misc
Version: 1.0.3
Release: 6
Summary: Xorg X11 font dec-misc
Group: Development/X11
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-dec-misc-%{version}.tar.bz2
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11 <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font dec-misc

%prep
%setup -q -n font-dec-misc-%{version}

%build
./configure --prefix=/usr --x-includes=%{_includedir}\
	    --x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/misc

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/misc/fonts.scale
rm -f %{buildroot}%_datadir/fonts/misc/fonts.dir

%post
mkfontscale %_datadir/fonts/misc
mkfontdir %_datadir/fonts/misc

%postun
mkfontscale %_datadir/fonts/misc
mkfontdir %_datadir/fonts/misc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING
%_datadir/fonts/misc/deccurs.pcf.gz
%_datadir/fonts/misc/decsess.pcf.gz


%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.3-4mdv2011.0
+ Revision: 675474
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.0.3-3
+ Revision: 675248
- rebuild for new rpm-setup

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2
+ Revision: 671205
- mass rebuild

* Thu Dec 09 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2011.0
+ Revision: 618735
- new release

* Wed Oct 06 2010 Thierry Vignaud <tv@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 583204
- new release

* Wed Jan 13 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.0.1-1mdv2010.1
+ Revision: 490684
- Fix license
- New version: 1.0.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.0-7mdv2009.1
+ Revision: 351313
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-6mdv2009.0
+ Revision: 225989
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.0-5mdv2008.1
+ Revision: 129732
- kill re-definition of %%buildroot on Pixel's request

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild prep


* Thu Aug 03 2006 Helio Chissini de Castro <helio@mandriva.com>
+ 2006-08-03 18:53:52 (51483)
- Fonts packages now are noarch. Moved for new place /usr/share/fonts. Approved by Boiko

* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

