Summary:	A free OpenGL game of playing billard.
Name:		foobillard
Version:	2.3
Release:	1
Group:		X11/Applications/Games
Vendor:		Florian Berger (florian.berger@aec.at,harpin_floh@yahoo.de)
License:	GPL
URL:		http://foobillard.sunsite.dk/
Source0:	http://foobillard.sunsite.dk/dnl/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-include.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-devel
BuildRequires:	intltool
BuildRequires:	SDL-devel
BuildRequires:	freetype-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
FooBillard is an attempt to create a free OpenGL-billard for Linux.
Why foo? Well, actually I had this logo (F.B.-Florian Berger) and then
foo sounds a bit like pool (Somehow I wasn't quite attracted by the
name FoolBillard) Actually FooBillard is still under development but
the main physics is implemented. If you are a billard-pro and you're
missing some physics, please tell me. Cause I've implemented it like I
think it should work, which might differ from reality.

%prep
%setup -q
%patch0 -p1

%build
rm -f missing
export X_LIBS='-I%{_includedir}'
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure --enable-SDL
%{__make}


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Games
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Games
%{__make} DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING INSTALL NEWS README ChangeLog TODO README.FONTS foobillardrc.example
%attr(755,root,root) %{_bindir}/*
%{_datadir}/foobillard/*
%{_applnkdir}/Games/%{name}.desktop
