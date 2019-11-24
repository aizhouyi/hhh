# vim

## 基本模式

### normal模式

默认就是打开就是个模式，G最后一行开头，gg第一行开头

### insert模式

| 按键        | 意义                             |
| ----------- | -------------------------------- |
| 普通模式下a | append，光标之后                 |
| 普通模式下i | insert，光标之前                 |
| 普通模式下A | 定位到行首                       |
| 普通模式下I | 定位到行尾                       |
| 普通模式下o | 在光标所在行的下面另起一新行插入 |
| 普通模式下O | 在光标所在行的上面另起一新行插入 |

### visual可视模式

普通模式按下==v==进入普通可视模式

==shift + v==进入可视行模式

==ctrl + v==进入可视块模式，就是选中每行的同列选中

移动光标可以自由选中

对于选中的，我们有很多操作和动作：

1. 摁下`:`进入命令行模式，输入`normal`，和你需要做的指令

   例如：`I myfile<CR>`就是选中的，开在头插入myfile字符串

   `A .txt<CR>`选中的，在末尾插入.txt

2. 摁下大写的a或者i进入插入模式，修改完成后，摁esc回到普通模式，全部改变了！！！

### command line命令

在normal模式下按下==:==进入

## 配置文件

第二用户 vimrc 文件: "~/.vim/vimrc"

### map映射

1. noremap

   非递归的键位映射

2. map

   一般的，
   
3. leader键，默认vim反斜杠

   let mapleader=" "就是把空格作为leader键

   noremap <LEADER><CR>  :nohlsearch

### 插件

使用github上的vim-plug来管理和安装插件

```shell
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
    https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

打开~/.vim/vimrc写Plug

```
call plug#begin()
Plug 'vim-airline/vim-airline'
call plug#end()
```

Plug ‘插件github的文件地址’

接着进入command模式`PlugInstall<CR>`完成安装，之后选择配置文件

一下是三十四个插件，我们来一一简单说下

```txt
Plug 'vim-airline/vim-airline'
Plug 'connorholyday/vim-snazzy'



" File navigation
Plug 'scrooloose/nerdtree', { 'on': 'NERDTreeToggle' } 文件树ff召唤，还有书签功能
Plug 'Xuyuanp/nerdtree-git-plugin'

" Taglist
Plug 'majutsushi/tagbar', { 'on': 'TagbarOpenAutoClose' }

" Error checking，检查你的代码中错误
Plug 'w0rp/ale'

" Auto Complete，最强大的代码补全！！！！！
Plug 'Valloric/YouCompleteMe'

" Undo Tree，浏览你的文件历史版本
Plug 'mbbill/undotree/'

" Other visual enhancement
Plug 'nathanaelkane/vim-indent-guides'
Plug 'itchyny/vim-cursorword'

" Git
Plug 'rhysd/conflict-marker.vim'
Plug 'tpope/vim-fugitive'
Plug 'mhinz/vim-signify'
Plug 'gisphm/vim-gitignore', { 'for': ['gitignore', 'vim-plug'] }

" HTML, CSS, JavaScript, PHP, JSON, etc.
Plug 'elzr/vim-json'
Plug 'hail2u/vim-css3-syntax'
Plug 'spf13/PIV', { 'for' :['php', 'vim-plug'] }
Plug 'gko/vim-coloresque', { 'for': ['vim-plug', 'php', 'html', 'javascript', 'css', 'less'] }
Plug 'pangloss/vim-javascript', { 'for' :['javascript', 'vim-plug'] }
Plug 'mattn/emmet-vim'

" Python
Plug 'vim-scripts/indentpython.vim'

" Markdown
Plug 'iamcco/markdown-preview.nvim', { 'do': { -> mkdp#util#install_sync() }, 'for' :['markdown', 'vim-plug'] }
Plug 'dhruvasagar/vim-table-mode', { 'on': 'TableModeToggle' }
Plug 'vimwiki/vimwiki'

" Bookmarks
Plug 'kshenoy/vim-signature'

" Other useful utilities
Plug 'terryma/vim-multiple-cursors'
Plug 'junegunn/goyo.vim' " distraction free writing mode
Plug 'tpope/vim-surround' " type ysks' to wrap the word with '' or type cs'` to change 'word' to `word`
Plug 'godlygeek/tabular' " type ;Tabularize /= to align the =
Plug 'gcmt/wildfire.vim' " in Visual mode, type i' to select all text in '', or type i) i] i} ip
Plug 'scrooloose/nerdcommenter' " in <space>cc to comment a line

" Dependencies
Plug 'MarcWeber/vim-addon-mw-utils'
Plug 'kana/vim-textobj-user'
Plug 'fadein/vim-FIGlet'

```



## 操作和动作

<operation><motion>操作和动作都是在normal模式下，组合起来非常的炫酷

### 操作

d使用`d`, `c`, `s`, `x`等删除字符的命令时，被删除字符会进入匿名寄存器`""`。 你可以认为`""`寄存器是一个指针，指向刚才被存到的寄存器。

y复制

p粘贴

### 动作

hjkl就是动作

w移动到下一个单词word词首

e移动到下一个单词word词尾


b移动到上一个单词word词首

f移动到光标右边的指定字符上，fo移动到o字符上

### 两者结合

1. d

   按下d，然后方向键右（动作），动作就是指定对象，d3h，就是删除当前光标的左边3个字符，注意不包括当前光标

   df:

2. y

   同理，操作是y，那么就是复制，y3h就是复制当前光标的左边3个

   yf:

3. change

   c就是change，更改进入插入模式

   cw就是更改词，当前开始改掉

   ciw就是，change in word，整个单词改掉

   当然支持自定义，如，ci"，就是change in ""，引号中的都改掉，（从光标位置往右扫描过去）炫酷啊。同理的y复制，yiw，yi，yi"都是可以的

   cf:
   
   c$
   
   c0
   
4. 搜索

   normal模式下摁下/搜索

   set hlsearch高亮

   exex "nohlsearch"

   set incsearch实时的高亮

   n和N对应下一个和上一个

   set ignorecase忽略大小写

   set smartcase只能大小写，意思是如果只有包含一个大写字母，那么就是大小写敏感

   加\c就是忽略大小写，排除上面的两个设置影响

   加\C就是不忽略大小写，也就是大小写敏感，排除设置影响

## 分屏

:sp横分屏

:vsp竖分屏

ctrl + w 之后w在分屏之间切换

一切都可以用map完成快速的操作

```txt
map sk :set nosplitbelow<CR>:split<CR>
map sj :set splitbelow<CR>:split<CR>
map sh :set nosplitright<CR>:vsplit<CR>
map sl :set splitright<CR>:vsplit<CR>

map <C-up> <C-w>k
map <C-down> <C-w>j
map <C-left> <C-w>h
map <C-right> <C-w>l

map <M-up> :res+5<CR>
map <M-down> :res-5<CR>
map <M-left> :vertical resize-5<CR>
map <M-right> :vertical resize+5<CR>
```

:e filename打开新的文件

将左右分屏变换为垂直分屏

map sb <C-w>t<C-w>H

将垂直分屏变换为左右分屏

map sv <C-w>t<C-w>K

## 标签页

:tabe <filename>打开一个全行的标签

:-tabenext标签切换，减号右边，自然加号就是右边

:tabnext下一个

:tabNext上一个