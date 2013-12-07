# revision 20031
# category Package
# catalog-ctan /fonts/dictsym
# catalog-date 2007-09-25 10:20:14 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-dictsym
Version:	20070925
Release:	4
Summary:	DictSym font and macro package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/dictsym
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dictsym.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/dictsym.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This directory contains the DictSym Type1 font designed by
Georg Verweyen and all files required to use it with LaTeX on
the Unix or PC platforms. The font provides a number of symbols
commonly used in dictionaries. The accompanying macro package
makes the symbols accessible as LaTeX commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/public/dictsym/dictsym.afm
%{_texmfdistdir}/fonts/map/dvips/dictsym/dictsym.map
%{_texmfdistdir}/fonts/tfm/public/dictsym/dictsym.tfm
%{_texmfdistdir}/fonts/type1/public/dictsym/dictsym.pfb
%{_texmfdistdir}/fonts/type1/public/dictsym/dictsym.pfm
%{_texmfdistdir}/tex/latex/dictsym/dictsym.sty
%doc %{_texmfdistdir}/doc/fonts/dictsym/README
%doc %{_texmfdistdir}/doc/fonts/dictsym/dictsym.pdf
%doc %{_texmfdistdir}/doc/fonts/dictsym/dictsym.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070925-2
+ Revision: 750956
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070925-1
+ Revision: 718229
- texlive-dictsym
- texlive-dictsym
- texlive-dictsym
- texlive-dictsym

