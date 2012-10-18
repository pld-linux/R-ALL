%define		packname	ALL

Summary:	A data package
Name:		R-%{packname}
Version:	1.4.13
Release:	1
License:	Artistic 2.0
Group:		Applications/Engineering
Source0:	http://www.bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	82a9bef4b94bf5de355f9aa0921e19b3
URL:		http://www.bioconductor.org/packages/release/data/experiment/html/ALL.html
BuildRequires:	R-Biobase
BuildRequires:	R
BuildRequires:	texlive-latex
Requires:	R-Biobase
Requires:	R
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Data of T- and B-cell Acute Lymphocytic Leukemia from the Ritz
Laboratory at the DFCI (includes Apr 2004 versions).

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%dir %{_libdir}/R/library/%{packname}
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
