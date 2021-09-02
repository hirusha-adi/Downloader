#############################################################################
# Generated by PAGE version 6.2
#  in conjunction with Tcl version 8.6
#  Aug 31, 2021 10:58:26 PM +0530  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m62" -background #ffffff \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 600x370+786+240
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 4644 1274
    wm minsize $top 117 1
    wm overrideredirect $top 0
    wm resizable $top 0 0
    wm deiconify $top
    wm title $top "YouTube Video Downloader by ZeaCeR"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    label $top.lab45 \
        -activebackground #ffffff -activeforeground #fd0006 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 22 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ff2227 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {YouTube Video Downloader} 
    vTcl:DefineAlias "$top.lab45" "Topic" vTcl:WidgetProc "Toplevel1" 1
    entry $top.ent46 \
        -background #eeeeee -disabledforeground #a3a3a3 \
        -font {-family {Courier New} -size 17 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 344 
    vTcl:DefineAlias "$top.ent46" "urlhere" vTcl:WidgetProc "Toplevel1" 1
    button $top.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #1abe07 -disabledforeground #4646ff \
        -font {-family {Showcard Gothic} -size 16 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground #d2dcdf \
        -highlightcolor #000000 -pady 0 -text {+ Paste} 
    vTcl:DefineAlias "$top.but47" "btnpaste" vTcl:WidgetProc "Toplevel1" 1
    button $top.but48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #1681c0 -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 18 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -text {⬇ Download} 
    vTcl:DefineAlias "$top.but48" "btndownload" vTcl:WidgetProc "Toplevel1" 1
    button $top.but49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ff5155 -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 17 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ffffff -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -pady 0 -text X 
    vTcl:DefineAlias "$top.but49" "Button1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab46 \
        -activebackground #ffffff -activeforeground #fd0006 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 17 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground #ff2227 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -text {YouTube Link} 
    vTcl:DefineAlias "$top.lab46" "Topic_1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 1080p 
    vTcl:DefineAlias "$top.rad52" "p1080" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad53 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 720p 
    vTcl:DefineAlias "$top.rad53" "p720" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad54 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 480p 
    vTcl:DefineAlias "$top.rad54" "p480" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad55 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 360p 
    vTcl:DefineAlias "$top.rad55" "p360" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad56 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 240p 
    vTcl:DefineAlias "$top.rad56" "p240" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad57 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background white -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 144p 
    vTcl:DefineAlias "$top.rad57" "p144" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad58 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 64kbps 
    vTcl:DefineAlias "$top.rad58" "f64kbps" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad60 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 32kbps 
    vTcl:DefineAlias "$top.rad60" "f32kbps" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $top.tSe61 \
        -orient vertical 
    vTcl:DefineAlias "$top.tSe61" "TSeparator1" vTcl:WidgetProc "Toplevel1" 1
    menu $top.m62 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    $top.m62 add cascade \
        -menu "$top.m62.men65" -command {{}} -label File 
    set site_3_0 $top.m62
    menu $site_3_0.men65 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    $site_3_0.men65 add command \
        -command {#} -label {Paste URL} 
    $site_3_0.men65 add command \
        -command {#} -label {Paste Save Path} 
    $site_3_0.men65 add command \
        -command {#} -label Exit 
    $top.m62 add separator \
        
    $top.m62 add cascade \
        -menu "$top.m62.men71" -command {{}} -label Others 
    set site_3_0 $top.m62
    menu $site_3_0.men71 \
        -activebackground $vTcl(actual_gui_menu_analog) \
        -activeforeground #000000 -background $vTcl(actual_gui_menu_bg) \
        -font TkMenuFont -foreground $vTcl(actual_gui_menu_fg) -tearoff 0 
    $site_3_0.men71 add command \
        -command {#} -label {Why Free?} 
    $site_3_0.men71 add command \
        -command {#} -label Credits 
    $site_3_0.men71 add command \
        -command {#} -label Contributors 
    $site_3_0.men71 add command \
        -command {#} -label {Privacy Policy} 
    $site_3_0.men71 add command \
        -command {#} -label Help 
    ttk::separator $top.tSe63 \
        -orient vertical 
    vTcl:DefineAlias "$top.tSe63" "TSeparator1_1" vTcl:WidgetProc "Toplevel1" 1
    label $top.lab75 \
        -activebackground #f9f9f9 -activeforeground black -background #ffffff \
        -disabledforeground #a3a3a3 -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {YouTube Video Downloader by ZeaCeR#5641 - v0.2} 
    vTcl:DefineAlias "$top.lab75" "Lcreditsbottom" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 1440p 
    vTcl:DefineAlias "$top.rad45" "p1080_1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 2160p 
    vTcl:DefineAlias "$top.rad46" "p1080_1_1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 128kbps 
    vTcl:DefineAlias "$top.rad47" "f128kbps" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 160kbps 
    vTcl:DefineAlias "$top.rad48" "f160kbps" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 192kbps 
    vTcl:DefineAlias "$top.rad49" "f192kbps" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 256kbps 
    vTcl:DefineAlias "$top.rad50" "f256kbps" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text 320kbps 
    vTcl:DefineAlias "$top.rad51" "f320kbps" vTcl:WidgetProc "Toplevel1" 1
    ttk::separator $top.tSe52
    vTcl:DefineAlias "$top.tSe52" "TSeparator2" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad59 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text Playlist 
    vTcl:DefineAlias "$top.rad59" "p1080_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad61 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text Video 
    vTcl:DefineAlias "$top.rad61" "p1080_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    radiobutton $top.rad62 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background #ffffff -disabledforeground #a3a3a3 \
        -font {-family {Showcard Gothic} -size 9 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text Channel 
    vTcl:DefineAlias "$top.rad62" "p1080_1_1_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.lab45 \
        -in $top -x 0 -relx -0.017 -y 0 -width 0 -relwidth 1.023 -height 0 \
        -relheight 0.135 -anchor nw -bordermode ignore 
    place $top.ent46 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.256 -width 344 -relwidth 0 \
        -height 60 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but47 \
        -in $top -x 0 -relx 0.633 -y 0 -rely 0.243 -width 147 -relwidth 0 \
        -height 54 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but48 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.595 -width 337 -relwidth 0 \
        -height 84 -relheight 0 -anchor nw -bordermode ignore 
    place $top.but49 \
        -in $top -x 0 -relx 0.883 -y 0 -rely 0.243 -width 57 -relwidth 0 \
        -height 54 -relheight 0 -anchor nw -bordermode ignore 
    place $top.lab46 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.156 -width 0 -relwidth 0.273 \
        -height 0 -relheight 0.07 -anchor nw -bordermode ignore 
    place $top.rad52 \
        -in $top -x 0 -relx 0.633 -y 0 -rely 0.59 -width 0 -relwidth 0.18 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.rad53 \
        -in $top -x 0 -relx 0.633 -y 0 -rely 0.667 -width 0 -relwidth 0.18 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.rad54 \
        -in $top -x 0 -relx 0.633 -y 0 -rely 0.733 -width 0 -relwidth 0.18 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.rad55 \
        -in $top -x 0 -relx 0.633 -y 0 -rely 0.8 -width 0 -relwidth 0.18 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.rad56 \
        -in $top -x 0 -relx 0.633 -y 0 -rely 0.872 -width 0 -relwidth 0.18 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.rad57 \
        -in $top -x 0 -relx 0.633 -y 0 -rely 0.933 -width 0 -relwidth 0.18 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.rad58 \
        -in $top -x 0 -relx 0.833 -y 0 -rely 0.846 -width 0 -relwidth 0.147 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.rad60 \
        -in $top -x 0 -relx 0.833 -y 0 -rely 0.923 -width 0 -relwidth 0.147 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.tSe61 \
        -in $top -x 0 -relx 0.817 -y 0 -rely 0.441 -width 0 -relwidth 0.003 \
        -height 0 -relheight 0.538 -anchor nw -bordermode ignore 
    place $top.tSe63 \
        -in $top -x 0 -relx 0.625 -y 0 -rely 0.438 -width 0 -relwidth 0.003 \
        -height 0 -relheight 0.536 -anchor nw -bordermode ignore 
    place $top.lab75 \
        -in $top -x 0 -relx 0.05 -y 0 -rely 0.892 -width 0 -relwidth 0.507 \
        -height 0 -relheight 0.092 -anchor nw -bordermode ignore 
    place $top.rad45 \
        -in $top -x 0 -relx 0.633 -y 0 -rely 0.513 -width 0 -relwidth 0.18 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.rad46 \
        -in $top -x 0 -relx 0.633 -y 0 -rely 0.432 -width 0 -relwidth 0.18 \
        -height 0 -relheight 0.057 -anchor nw -bordermode ignore 
    place $top.rad47 \
        -in $top -x 0 -relx 0.833 -y 0 -rely 0.769 -width 0 -relwidth 0.147 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.rad48 \
        -in $top -x 0 -relx 0.833 -y 0 -rely 0.692 -width 0 -relwidth 0.147 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.rad49 \
        -in $top -x 0 -relx 0.833 -y 0 -rely 0.615 -width 0 -relwidth 0.147 \
        -height 0 -relheight 0.056 -anchor nw -bordermode ignore 
    place $top.rad50 \
        -in $top -x 0 -relx 0.833 -y 0 -rely 0.541 -width 0 -relwidth 0.147 \
        -height 0 -relheight 0.057 -anchor nw -bordermode ignore 
    place $top.rad51 \
        -in $top -x 0 -relx 0.833 -y 0 -rely 0.459 -width 0 -relwidth 0.147 \
        -height 0 -relheight 0.057 -anchor nw -bordermode ignore 
    place $top.tSe52 \
        -in $top -x 0 -relx 0.617 -y 0 -rely 0.432 -width 0 -relwidth 0.4 \
        -height 0 -relheight 0.005 -anchor nw -bordermode ignore 
    place $top.rad59 \
        -in $top -x 0 -relx 0.033 -y 0 -rely 0.459 -width 0 -relwidth 0.18 \
        -height 0 -relheight 0.057 -anchor nw -bordermode ignore 
    place $top.rad61 \
        -in $top -x 0 -relx 0.217 -y 0 -rely 0.459 -width 0 -relwidth 0.18 \
        -height 0 -relheight 0.057 -anchor nw -bordermode ignore 
    place $top.rad62 \
        -in $top -x 0 -relx 0.417 -y 0 -rely 0.459 -width 0 -relwidth 0.18 \
        -height 0 -relheight 0.057 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}



set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
