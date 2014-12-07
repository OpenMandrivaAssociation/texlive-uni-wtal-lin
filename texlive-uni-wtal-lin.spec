# revision 31409
# category Package
# catalog-ctan /macros/latex/contrib/biblatex-contrib/uni-wtal-lin
# catalog-date 2013-08-10 17:37:59 +0200
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-uni-wtal-lin
Version:	0.2
Release:	8
Summary:	Citation style for linguistic studies at the University of Wuppertal
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/uni-wtal-lin
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-wtal-lin.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-wtal-lin.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a biblatex citation style based on the
standard author-year style. The citations are optimised for
linguistic studies at the Institute of Linguistics at the
Bergische Universitat Wuppertal.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/uni-wtal-lin/uni-wtal-lin.bbx
%{_texmfdistdir}/tex/latex/uni-wtal-lin/uni-wtal-lin.cbx
%doc %{_texmfdistdir}/doc/latex/uni-wtal-lin/CHANGES
%doc %{_texmfdistdir}/doc/latex/uni-wtal-lin/LIESMICH
%doc %{_texmfdistdir}/doc/latex/uni-wtal-lin/README
%doc %{_texmfdistdir}/doc/latex/uni-wtal-lin/uni-wtal-lin.bib
%doc %{_texmfdistdir}/doc/latex/uni-wtal-lin/uni-wtal-lin.pdf
%doc %{_texmfdistdir}/doc/latex/uni-wtal-lin/uni-wtal-lin.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
