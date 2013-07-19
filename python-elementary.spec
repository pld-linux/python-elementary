Summary:	Python bindings for Elementary library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Elementary
Name:		python-elementary
Version:	1.7.0
Release:	6
License:	LGPL v3+
Group:		Development/Languages/Python
Source0:	http://download.enlightenment.org/releases/BINDINGS/python/%{name}-%{version}.tar.bz2
# Source0-md5:	38c8b2ac508ab4e1d12f1557a12169c9
URL:		http://trac.enlightenment.org/e/wiki/Python
BuildRequires:	elementary-devel >= 1.7.0
BuildRequires:	eina-devel >= 1.7.0
BuildRequires:	epydoc
BuildRequires:	evas-devel >= 1.7.0
BuildRequires:	python-Cython >= 0.15.1
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-evas >= 1.7.0
BuildRequires:	rpm-pythonprov
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	elementary-libs >= 1.7.0
Requires:	eina >= 1.7.0
Requires:	evas >= 1.7.0
Requires:	python-evas >= 1.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for Elementary library.

%description -l pl.UTF-8
Wiązania Pythona do biblioteki Elementary.

%package devel
Summary:	Python bindings for Elementary library - development files
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki Elementary - pliki programistyczne
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	elementary-devel >= 1.7.0
Requires:	eina-devel >= 1.7.0
Requires:	evas-devel >= 1.7.0
Requires:	python-evas-devel >= 1.7.0

%description devel
Python bindings for Elementary library - development files.

%description devel -l pl.UTF-8
Wiązania Pythona do biblioteki Elementary - pliki programistyczne.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/elementary/c_elementary.la

install -d $RPM_BUILD_ROOT%{_examplesdir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%dir %{py_sitedir}/elementary
%attr(755,root,root) %{py_sitedir}/elementary/c_elementary.so
%{py_sitedir}/elementary/*.py[co]
%{_examplesdir}/%{name}-%{version}

%files devel
%defattr(644,root,root,755)
%{_pkgconfigdir}/python-elementary.pc
