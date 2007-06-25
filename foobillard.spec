#
# Conditional build:
%bcond_with	glut	# use glut instead of SDL
%bcond_with	nvidia	# enable NVidia specific extensions
#
Summary:	A free OpenGL game of playing billard
Summary(pl.UTF-8):	Wolnodostępna gra w bilard oparta na OpenGL
Name:		foobillard
Version:	3.0a
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://foobillard.sunsite.dk/dnl/%{name}-%{version}.tar.gz
# Source0-md5:	c2d92edeaaf8bfb18aa26f1c79931b7d
Source1:	%{name}.desktop
Source2:	%{name}.xpm
URL:		http://foobillard.sunsite.dk/
BuildRequires:	OpenGL-devel
%{!?with_glut:BuildRequires:	SDL-devel}
%{?with_nvidia:BuildRequires:	xorg-driver-video-nvidia-devel}
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
%{?with_glut:BuildRequires:	glut-devel}
BuildRequires:	intltool
BuildRequires:	libpng-devel
BuildRequires:	libtool
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXi-devel
Requires:	OpenGL
%{?with_nvidia:Requires:	xorg-driver-video-nvidia}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1

%description
FooBillard is an attempt to create a free OpenGL-billard for Linux.
Why foo? Well, actually I had this logo (F.B.-Florian Berger) and then
foo sounds a bit like pool (Somehow I wasn't quite attracted by the
name FoolBillard). Actually FooBillard is still under development but
the main physics is implemented. If you are a billard-pro and you're
missing some physics, please tell me. Cause I've implemented it like I
think it should work, which might differ from reality.

%description -l pl.UTF-8
FooBillard to próba stworzenia wolnodostępnego bilarda OpenGL dla
Linuksa. Dlaczego foo? Bo autor miał już to logo (F.B. - Florian
Berger) i "foo" brzmi trochę jak "pool" (a nazwa "FoolBillard" nie
brzmiała zbyt przyciągająco). FooBillard jest nadal w stadium rozwoju,
ale główna fizyka jest już zaimplementowana. Jeżeli w grze brakuje
jakiejś fizyki, dobrze jest zgłosić to autorowi, ponieważ on
zaimplementował ją tak, jak myślał, że powinna działać, co może się
nieco różnić od rzeczywistości.

%prep
%setup -q

%build
rm -f missing
X_LIBS='-I/usr/X11R6/include'; export X_LIBS
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
%if %{with glut}
	--enable-glut \
	--disable-SDL \
%else
	--disable-glut \
	--enable-SDL \
%endif
	--%{?with_nvidia:en}%{!?with_nvidia:dis}able-nvidia \
	--enable-sound

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README ChangeLog TODO README.FONTS foobillardrc.example
%attr(755,root,root) %{_bindir}/*
%{_datadir}/foobillard
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*
