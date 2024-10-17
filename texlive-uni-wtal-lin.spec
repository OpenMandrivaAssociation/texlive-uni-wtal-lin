Name:		texlive-uni-wtal-lin
Version:	31409
Release:	2
Summary:	Citation style for linguistic studies at the University of Wuppertal
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/uni-wtal-lin
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-wtal-lin.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uni-wtal-lin.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
