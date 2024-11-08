#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-GetoptLong
Version  : 1.0.5
Release  : 28
URL      : https://cran.r-project.org/src/contrib/GetoptLong_1.0.5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/GetoptLong_1.0.5.tar.gz
Summary  : Parsing Command-Line Arguments and Simple Variable Interpolation
Group    : Development/Tools
License  : MIT
Requires: R-GlobalOptions
Requires: R-crayon
Requires: R-rjson
BuildRequires : R-GlobalOptions
BuildRequires : R-crayon
BuildRequires : R-rjson
BuildRequires : buildreq-R

%description
This R package is a wrapper of perl module `Getopt::Long`.
Basically, all Perl distributions contain `Getopt::Long` as a core module and
`JSON` module is already included in this package. So minimal requirement
for you to use this package is you should have Perl to be installed.

%prep
%setup -q -c -n GetoptLong
cd %{_builddir}/GetoptLong

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641026072

%install
export SOURCE_DATE_EPOCH=1641026072
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library GetoptLong
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library GetoptLong
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library GetoptLong
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc GetoptLong || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/GetoptLong/DESCRIPTION
/usr/lib64/R/library/GetoptLong/INDEX
/usr/lib64/R/library/GetoptLong/LICENSE
/usr/lib64/R/library/GetoptLong/Meta/Rd.rds
/usr/lib64/R/library/GetoptLong/Meta/features.rds
/usr/lib64/R/library/GetoptLong/Meta/hsearch.rds
/usr/lib64/R/library/GetoptLong/Meta/links.rds
/usr/lib64/R/library/GetoptLong/Meta/nsInfo.rds
/usr/lib64/R/library/GetoptLong/Meta/package.rds
/usr/lib64/R/library/GetoptLong/Meta/vignette.rds
/usr/lib64/R/library/GetoptLong/NAMESPACE
/usr/lib64/R/library/GetoptLong/NEWS
/usr/lib64/R/library/GetoptLong/R/GetoptLong
/usr/lib64/R/library/GetoptLong/R/GetoptLong.rdb
/usr/lib64/R/library/GetoptLong/R/GetoptLong.rdx
/usr/lib64/R/library/GetoptLong/doc/GetoptLong.R
/usr/lib64/R/library/GetoptLong/doc/GetoptLong.Rmd
/usr/lib64/R/library/GetoptLong/doc/GetoptLong.html
/usr/lib64/R/library/GetoptLong/doc/index.html
/usr/lib64/R/library/GetoptLong/doc/variable_interpolation.R
/usr/lib64/R/library/GetoptLong/doc/variable_interpolation.Rmd
/usr/lib64/R/library/GetoptLong/doc/variable_interpolation.html
/usr/lib64/R/library/GetoptLong/extdata/perl_lib/JSON.pm
/usr/lib64/R/library/GetoptLong/extdata/perl_lib/JSON/Syck.pm
/usr/lib64/R/library/GetoptLong/extdata/perl_lib/JSON/XS.pm
/usr/lib64/R/library/GetoptLong/extdata/perl_lib/JSON/XS/Boolean.pm
/usr/lib64/R/library/GetoptLong/extdata/perl_lib/JSON/backportPP.pm
/usr/lib64/R/library/GetoptLong/extdata/perl_lib/JSON/backportPP/Boolean.pm
/usr/lib64/R/library/GetoptLong/extdata/perl_lib/JSON/backportPP/Compat5005.pm
/usr/lib64/R/library/GetoptLong/extdata/perl_lib/JSON/backportPP/Compat5006.pm
/usr/lib64/R/library/GetoptLong/help/AnIndex
/usr/lib64/R/library/GetoptLong/help/GetoptLong.rdb
/usr/lib64/R/library/GetoptLong/help/GetoptLong.rdx
/usr/lib64/R/library/GetoptLong/help/aliases.rds
/usr/lib64/R/library/GetoptLong/help/paths.rds
/usr/lib64/R/library/GetoptLong/html/00Index.html
/usr/lib64/R/library/GetoptLong/html/R.css
/usr/lib64/R/library/GetoptLong/tests/test-all.R
/usr/lib64/R/library/GetoptLong/tests/testthat/test.R
/usr/lib64/R/library/GetoptLong/tests/testthat/test_GetoptLong.R
/usr/lib64/R/library/GetoptLong/tests/testthat/test_qq.R
