" --------------------------------
" Add our plugin to the path
" --------------------------------
python import sys
python import vim
python sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
"
"
function! DefineWord(currentWord)
python << endOfPython

from definer import *

currentWord = vim.eval("a:currentWord")
DefineWord(currentWord);
endOfPython
endfunction

function! VimDefineWord()
   let wordValue = expand("<cword>")
   call DefineWord(wordValue)
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! Definer call VimDefineWord()
