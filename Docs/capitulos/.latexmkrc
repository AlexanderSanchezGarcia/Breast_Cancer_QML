# Docs/capitulos/.latexmkrc
use Cwd qw(cwd abs_path);
use File::Basename qw(basename);
use File::Path qw(make_path);

my $cur = basename(cwd());

# Configure search paths for LaTeX (finds Figures/, tablas/, codigo/, Logos/ in Docs/)
$ENV{'TEXINPUTS'} = '.:..:../..:' . ($ENV{'TEXINPUTS'} // '') . ':';

if ($cur eq 'capitulos') {
    $aux_dir = '_build';
    $out_dir = '.';
} else {
    $aux_dir = "../_build/$cur";
    $out_dir = '.';
}

if (! -d $aux_dir) {
    make_path($aux_dir);
}

$emulate_aux = 1;
$pdf_mode = 1;
$pdflatex = 'pdflatex -interaction=nonstopmode -halt-on-error %O %S';

1;
