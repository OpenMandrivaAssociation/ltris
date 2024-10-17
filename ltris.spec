Summary:	Nice tetris clone
Name:		ltris
Version:	1.3
Release:	2
Epoch:		1
Url:		https://lgames.sourceforge.net/index.php?project=LTris
Source0:	http://sourceforge.net/projects/lgames/files/%{name}/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Games/Arcade
BuildRequires:	SDL_mixer-devel
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils

%description
o Tetris clone using SDL
o Sound
o Menu
o Controls can be redefined
o Block preview
o Starting level between 0 and 9
o Various backgrounds
o HighScores
o Nice graphics
o Smooth gameplay
o Cool effects (transparency, animations)
o Two player mode
o Two game modes

%prep
%autosetup -p1

%build
%configure	--localstatedir=%{_localstatedir}/games \
		--bindir=%{_gamesbindir}
%make_build

%install
%make_install

# non standard location fix
mkdir %{buildroot}/%{_iconsdir}/hicolor/48x48
mv %{buildroot}/%{_iconsdir}/hicolor/apps  %{buildroot}/%{_iconsdir}/hicolor/48x48
%find_lang %{name}

%files -f %{name}.lang
%doc README INSTALL AUTHORS ChangeLog
%attr(2755, root, games) %{_gamesbindir}/*
%config(noreplace) %attr(664, games, games) %{_localstatedir}/games/%{name}.hscr
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/*/*/*/*


%changelog
* Wed Dec 14 2011 Andrey Bondrov <abondrov@mandriva.org> 1:1.0.18-1
+ Revision: 740872
- New version 1.0.18, spec cleanup

* Tue Mar 08 2011 Zombie Ryushu <ryushu@mandriva.org> 1:1.0.16-1
+ Revision: 642815
- Upgrade to 1.0.16

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 1:1.0.14-2mdv2011.0
+ Revision: 612774
- the mass rebuild of 2010.1 packages

* Fri Dec 25 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.0.14-1mdv2010.1
+ Revision: 482321
- Update to new version 1.0.14
- Remove new upstream desktop and icon files because Mandriva's are better

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1:1.0.13-1mdv2010.1
+ Revision: 462292
- update to new version 1.0.13

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1:1.0.12-2mdv2010.0
+ Revision: 429878
- rebuild

* Mon Aug 11 2008 Funda Wang <fwang@mandriva.org> 1:1.0.12-1mdv2009.0
+ Revision: 270696
- New version 1.0.12

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Sun Mar 23 2008 Emmanuel Andry <eandry@mandriva.org> 1:1.0.11-5mdv2008.1
+ Revision: 189591
- fix BR to enable sound (#39245)

* Thu Jan 03 2008 Olivier Blin <blino@mandriva.org> 1:1.0.11-4mdv2008.1
+ Revision: 140933
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

* Tue Aug 28 2007 Funda Wang <fwang@mandriva.org> 1:1.0.11-4mdv2008.0
+ Revision: 72334
- fix menu entry comment

* Sat Jun 30 2007 Olivier Thauvin <nanardon@mandriva.org> 1:1.0.11-3mdv2008.0
+ Revision: 46107
- kill leading space at end of EOF

  + Guillaume Bedot <littletux@mandriva.org>
    - xdg menu


* Thu Dec 14 2006 Eskild Hustvedt <eskild@mandriva.org> 1.0.11-2mdv2007.0
+ Revision: 97170
- Yearly rebuild
- Import ltris

* Fri Oct 07 2005 Lenny Cartier <lenny@mandriva.com> 1:1.0.11-1mdk
- 1.0.11

* Sat Feb 19 2005 Pixel <pixel@mandrakesoft.com> 1:1.0.10-1mdk
- new release

* Thu Jan 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.0.6-1mdk
- 1.0.6

