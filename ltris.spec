%define	name	ltris
%define	version	1.0.11
%define	release	%mkrel 3

Summary:	Nice tetris clone
Name:	        %{name}
Version:	%{version}
Release:	%{release}
Epoch:		1
Url:		http://lgames.sourceforge.net/index.php?project=LTris
Source0:	ltris-%{version}.tar.bz2
# Source4:	%{name}.menu
Source5:	%{name}16.png.bz2
Source6:	%{name}32.png.bz2
Source7:	%{name}48.png.bz2
License:	GPL
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	common-licenses
BuildRequires:	libSDL-devel


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
%setup -q

%build
%configure	--with-highscore-path=%{_localstatedir}/games \
		--bindir=%{_gamesbindir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT{%{_liconsdir},%{_miconsdir}}

bzcat %{SOURCE5} > $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
bzcat %{SOURCE6} > $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
bzcat %{SOURCE7} > $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

# install -D -m644 %SOURCE4 $RPM_BUILD_ROOT%{_menudir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_menudir}/

cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}):\
  needs=x11 section=Amusement/Arcade\
  title="LTris"\
  longtitle="Nice tetris clone"\
  command="%{_gamesbindir}/%{name}"\
  icon="ltris.png"\
  xdg="true"
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat >$RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=LTris
Comment=%{Summary}
Exec=/usr/games/ltris
Icon=ltris
Terminal=false
Type=Application
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF 

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post 
%{update_menus}

%postun
%{clean_menus}

%files -f %name.lang
%defattr(-,root,root)
%doc README INSTALL AUTHORS ChangeLog
%attr(2755, root, games) %{_gamesbindir}/*
%attr(664, root, games) %{_localstatedir}/%{name}.hscr
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_menudir}/*
%{_iconsdir}/*.png
%{_miconsdir}/*
%{_liconsdir}/*


