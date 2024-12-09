#!/usr/bin/env python3

"""
copyright (c), 2021 antlas
"""



template_content = """
\\documentclass[]{deedy-resume-openfont}
\\usepackage{tikz}
\\usepackage{xcolor}
\\usepackage[most]{tcolorbox}
\\usepackage{eso-pic,graphicx}
\\usepackage{ragged2e}

\\tcbset{
	frame code={}
	center title,
	left=5pt,
	%right=0pt,
	top=0pt,
	%bottom=0pt,
	colback=blue!20,
	colframe=white,
	width=150pt,
	enlarge left by=0mm,
	boxsep=0pt,
	arc=0pt,outer arc=0pt,
}

\\usepackage{eso-pic}% http://ctan.org/pkg/eso-pic



\\usepackage{background}
\\usepackage{tikzpagenodes}

\\backgroundsetup{%
	scale=1,
	angle=0,
	opacity=0.7,
	contents={\\includegraphics[width=2.5cm]{image1}},
	position=current page text area.north west,
	anchor=below right,
}

\\linespread{1.3}
\\begin{document}

\\author{author1}

\\lastupdated

\\namesection{Projects}{report}{ \\urlstyle{same} Report\\\\
	\\href{mailto:email1}{email1} | \\\\
	\\vspace{0.5cm}
	%\\large\\textsc{report}
	\\normalfont
}


%\\definecolor{ggreen}{HTML}{97e5d8}
%\\noindent\\fcolorbox{white}{white}{%
\\begin{minipage}[t]{0.01\\textwidth}
	%{\\dimexpr0.25\\textwidth-2\\fboxrule-2\\fboxsep\\relax}

\\vspace{0.5cm}
\\end{minipage}
%}%
\\hfill


\\begin{minipage}[t]{0.90\\textwidth}


\\vspace{0.5cm}
\\section{Projects}

\\includegraphics[width=1cm]{image1}\\\\
\\sectionsep


\\end{minipage}
\\end{document}
"""
