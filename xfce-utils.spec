Summary:	Utilities for the XFce Desktop Environment
Summary(pl):	Narzêdzia dla ¶rodowiska XFce
Name:		xfce-utils
Version:	4.0.6
Release:	1
License:	GPL
Group:		X11/Applications
#Source0:	ftp://ftp.berlios.de/pub/xfce-goodies/%{version}/%{name}-%{version}.tar.gz
Source0:	http://hannelore.f1.fhtw-berlin.de/mirrors/xfce4/xfce-%{version}/src/%{name}-%{version}.tar.gz
# Source0-md5:	d42a01aa03a9eafb9bc2cc546d988b4b
Source1:	xfce4-xsession.desktop
Patch0:		%{name}-locale-names.patch
URL:		http://www.xfce.org/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libxfce4mcs-devel >= %{version}
BuildRequires:	libxfcegui4-devel >= %{version}
BuildRequires:	pkgconfig >= 0.9.0
BuildRequires:	xfce-mcs-manager-devel >= %{version}
Requires:	libxfce4mcs >= %{version}
Requires:	libxfcegui4 >= %{version}
Requires:	xfce-mcs-manager >= %{version}
Conflicts:	xfce4-session < 0.1.1-2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xfce-utils contains utilities for the XFce Desktop Environment.

%description -l pl
xfce-utils zawiera narzêdzia dla ¶rodowiska XFce.

%prep
%setup -q
%patch0 -p1

mv -f po/{fa_IR,fa}.po
mv -f po/{no,nb}.po
mv -f po/{pt_PT,pt}.po

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-gdm
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xfce4/mcs-plugins/*.{la,a}

install -d $RPM_BUILD_ROOT%{_datadir}/xsessions
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/xsessions/xfce4.desktop

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/xfce4/mcs-plugins/*.so
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/xfce4/xinitrc
%{_datadir}/xfce4/AUTHORS
%lang(az) %{_datadir}/xfce4/AUTHORS.az
%lang(ca) %{_datadir}/xfce4/AUTHORS.ca
%lang(de) %{_datadir}/xfce4/AUTHORS.de
%lang(es) %{_datadir}/xfce4/AUTHORS.es
%lang(fr) %{_datadir}/xfce4/AUTHORS.fr
%lang(it) %{_datadir}/xfce4/AUTHORS.it
%lang(vi) %{_datadir}/xfce4/AUTHORS.vi
%{_datadir}/xfce4/AUTHORS.html
%lang(az) %{_datadir}/xfce4/AUTHORS.html.az
%lang(ca) %{_datadir}/xfce4/AUTHORS.html.ca
%lang(de) %{_datadir}/xfce4/AUTHORS.html.de
%lang(es) %{_datadir}/xfce4/AUTHORS.html.es
%lang(fr) %{_datadir}/xfce4/AUTHORS.html.fr
%lang(it) %{_datadir}/xfce4/AUTHORS.html.it
%{_datadir}/xfce4/BSD
%{_datadir}/xfce4/BSD.html
%{_datadir}/xfce4/COPYING
%lang(vi) %{_datadir}/xfce4/COPYING.vi
%{_datadir}/xfce4/COPYING.html
%{_datadir}/xfce4/GPL
%{_datadir}/xfce4/GPL.html
%{_datadir}/xfce4/INFO
%{_datadir}/xfce4/INFO.html
%lang(ca) %{_datadir}/xfce4/INFO.ca
%lang(es) %{_datadir}/xfce4/INFO.es
%lang(fr) %{_datadir}/xfce4/INFO.fr
%lang(it) %{_datadir}/xfce4/INFO.it
%lang(vi) %{_datadir}/xfce4/INFO.vi
%lang(ca) %{_datadir}/xfce4/INFO.html.ca
%lang(de) %{_datadir}/xfce4/INFO.html.de
%lang(es) %{_datadir}/xfce4/INFO.html.es
%lang(fr) %{_datadir}/xfce4/INFO.html.fr
%lang(it) %{_datadir}/xfce4/INFO.html.it
%{_datadir}/xfce4/LGPL
%{_datadir}/xfce4/LGPL.html
%docdir %{_datadir}/xfce4/doc
%{_datadir}/xfce4/doc/xfce.css
%{_datadir}/xfce4/doc/C/*.html
%{_datadir}/xfce4/doc/C/images/*
%lang(fr) %{_datadir}/xfce4/doc/fr/*.html
%lang(fr) %{_datadir}/xfce4/doc/fr/images/*

%{_datadir}/apps/switchdesk/Xclients.xfce4
%{_datadir}/xsessions/xfce4.desktop
