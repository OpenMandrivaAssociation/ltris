Summary:	Nice tetris clone
Name:		ltris
Version:	1.0.18
Release:	%mkrel 1
Epoch:		1
Url:		http://lgames.sourceforge.net/index.php?project=LTris
Source0:	http://prdownloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
License:	GPLv2+
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
%setup -q

%build
%configure2_5x	--localstatedir=%{_localstatedir}/games \
		--bindir=%{_gamesbindir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

mkdir -p %{buildroot}{%{_liconsdir},%{_miconsdir}}
convert icons/%{name}48.xpm %{buildroot}%{_liconsdir}/%{name}.png
convert icons/%{name}32.xpm %{buildroot}%{_iconsdir}/%{name}.png
convert icons/%{name}16.xpm %{buildroot}%{_miconsdir}/%{name}.png

rm %{buildroot}%{_datadir}/applications/%{name}.desktop
rm %{buildroot}%{_iconsdir}/%{name}48.gif

mkdir -p %{buildroot}%{_datadir}/applications/
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop <<EOF
[Desktop Entry]
Name=LTris
Comment=Nice Tetris clone
Exec=ltris
Icon=ltris
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README INSTALL AUTHORS ChangeLog
%attr(2755, root, games) %{_gamesbindir}/*
%config(noreplace) %attr(664, games, games) %{_localstatedir}/games/%{name}.hscr
%{_datadir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/*.png
%{_miconsdir}/*
%{_liconsdir}/*

