%define major 1
%define abi 0.1
%define devname %mklibname epubgen -d

Name: libepubgen
Version: 0.1.1
Release: 2
Source0: https://downloads.sourceforge.net/project/libepubgen/libepubgen-%{version}/libepubgen-%{version}.tar.xz
Summary: Library for generating epub files
URL: https://sourceforge.net/projects/libepubgen/
License: LGPLv2.1/MPL
Group: System/Libraries
BuildRequires: pkgconfig(cppunit)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(librevenge-0.0)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: boost-devel
BuildRequires: doxygen

%libpackage epubgen %{abi} %{major}

%define libname %mklibname epubgen %{abi} %{major}

%description
libepubgen is an EPUB generator for librevenge. It supports librevenge's text
document interface and--currently in a very limited way--presentation and
vector drawing interfaces.

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

libepubgen is an EPUB generator for librevenge. It supports librevenge's text
document interface and--currently in a very limited way--presentation and
vector drawing interfaces.

%package doc
Summary: Documentation for %{name}
Group: Development/C

%description doc
Documentation for %{name}.

libepubgen is an EPUB generator for librevenge. It supports librevenge's text
document interface and--currently in a very limited way--presentation and
vector drawing interfaces.

%prep
%setup -q
%configure

%build
%make

%install
%makeinstall_std

%files -n %{devname}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files doc
%{_docdir}/%{name}
