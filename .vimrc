syntax on
set bg=dark

filetype plugin indent on
set tabstop=4
set shiftwidth=4
set softtabstop=0
set expandtab
set smarttab

set number

set nowrap

filetype plugin indent on

nnoremap <Tab> <Esc>
vnoremap <Tab> <Esc>gV
onoremap <Tab> <Esc>
inoremap <Tab> <Esc>`^
inoremap <Leader><Tab> <Tab>

autocmd BufWritePost *.tex !pdflatex main.tex

set autochdir
