title = 'Metafor Interactive Natural Language Programming (hugo@media.mit.edu)'

import Tkinter
import Pmw
import string, sys, os, time
import Metafor
import logging

class MetaforGUI:

    def do_look_and_feel(self):
        # overall
        # Pmw.Color.changecolor(self.menuBar.component('hull'), background='#808080', foreground='#333333')
        
        # left
        Pmw.Color.changecolor(self.left_panel.component('hull'),
                              background='#C0C0C0')
        # right
        Pmw.Color.changecolor(self.right_panel.component('hull'),
                              background='#C0C0C0')

        # menu
        Pmw.Color.changecolor(self.menuBar.component('hull'),
                              background='#4682B4',
                              foreground='black')
        # frame inbetween
        Pmw.Color.changecolor(self.panedWidgetOutside.component('hull'),
                              background='#4682B4')
        # four windows
        self.dialog_history.component('text').config(bg='#CCC2CC')
        self.query.component('text').config(bg='#C0C0C0')
        self.python_viewer.component('text').config(bg='#C1C1C1')
        self.clisp_viewer.component('text').config(bg='#D2D2D2')
        self.model_viewer.component('text').config(bg='#E3E3E3')
        self.visualizer.component('text').config(bg='#C0C0C0')
        return
                
    def __init__(self, parent):
        self.__code_viewer = 'python'
        self.parent = parent
        self.balloon = Pmw.Balloon(parent)
        # default colorscheme
        Pmw.Color.setscheme(self.parent, background='#C0C0C0', foreground="blue")

        # create the menubar
        menuBar = Pmw.MenuBar(parent,
                hull_relief='raised',
                hull_borderwidth=1,
                balloon=self.balloon)
        menuBar.pack(fill='x')
        self.menuBar = menuBar

        # file pulldown
        menuBar.addmenu('File', 'Close this window or exit')
        menuBar.addmenuitem('File', 'command', 'Exit the application',
                command=parent.destroy,
                label='Exit')

        # create the main container below the menu bar
        panedWidgetOutside = Pmw.PanedWidget(parent,
                                             orient='horizontal',
                                             hull_height=540,
                                             hull_width=960)
        panedWidgetOutside.add('left', min=0.05)
        panedWidgetOutside.add('right', min=0.05)
        panedWidgetOutside.pack(fill='both', expand=1)
        self.panedWidgetOutside = panedWidgetOutside

        # the left panes: dialog history and query
        panedWidgetLeft = Pmw.PanedWidget(panedWidgetOutside.pane('left'),
                orient='vertical',
                hull_height=500,
                hull_width=400)
        panedWidgetLeft.add('dialoghistory', size=0.8)
        panedWidgetLeft.add('query', min=0.05, size=0.2)
        panedWidgetLeft.pack(fill='both', expand=1)
        self.left_panel = panedWidgetLeft
        
        # the right panes: visualizer and code_viewer
        panedWidgetRight = Pmw.PanedWidget(panedWidgetOutside.pane('right'),
                orient='vertical',
                hull_height=500,
                hull_width=400)
        panedWidgetRight.add('visualizer', size=0.5)
        panedWidgetRight.add('codeviewer', size=0.5)
        panedWidgetRight.pack(fill='both', expand=1)
        self.right_panel = panedWidgetRight

        # the dialog history pane
        self.dialog_history = Pmw.ScrolledText(panedWidgetLeft.pane('dialoghistory'),
                                               text_wrap='word')
        self.dialog_history.pack(padx=5, pady=2, fill='both', expand=1)
        
        # the query pane
        self.query = Pmw.ScrolledText(panedWidgetLeft.pane('query'), text_wrap='word')
        self.query.pack(padx=5, pady=2, fill='both', expand=1)
        self.query.component('text').bind('<Return>', self.execute_query)

        # the visualizer
        #        self.visualizer = Pmw.ScrolledCanvas(panedWidgetRight.pane('visualizer'))
        self.visualizer = Pmw.ScrolledText(panedWidgetRight.pane('visualizer'))
        self.visualizer.pack(fill='both', expand=5, padx=8, pady=2)

        # the code viewer
        self.code_viewer = Pmw.NoteBook(panedWidgetRight.pane('codeviewer'))
        self.code_viewer.pack(fill='both', expand=1, padx=5, pady=5)

        # a) create python viewer
        self.python_viewer_page = self.code_viewer.add('python')
        self.code_viewer.tab('python').focus_set()
        self.python_viewer = Pmw.ScrolledText(self.python_viewer_page, text_wrap='word')
        self.python_viewer.pack(fill='both', expand=1, padx=5, pady=5)

        # b) create clisp viewer
        self.clisp_viewer_page = self.code_viewer.add('clisp')
        self.code_viewer.tab('clisp').focus_set()
        self.clisp_viewer = Pmw.ScrolledText(self.clisp_viewer_page, text_wrap='word')
        self.clisp_viewer.pack(fill='both', expand=1, padx=5, pady=5)
        
        # c) create model viewer
        self.howTo_viewer_page = self.code_viewer.add('howTo')
        self.code_viewer.tab('howTo').focus_set()
        self.model_viewer = Pmw.ScrolledText(self.howTo_viewer_page, text_wrap='word')
        self.model_viewer.pack(fill='both', expand=1, padx=5, pady=5)

        # look and feel
        self.do_look_and_feel()
        
        # start metafor
        self.theMetafor = Metafor.Metafor()

    def push_dialog_history(self, statement, author):
        # author = user | computer
        if author == 'user':
            header = '[user] (' + string.join(map(lambda x:string.zfill(str(x), 2), time.localtime()[3:6]), ':') + ')  '
        else:
            time.sleep(0.0) # delay
            header = '[agent] (' + string.join(map(lambda x:string.zfill(str(x), 2), time.localtime()[3:6]), ':') + ')  '
        self.dialog_history.see('end')
        self.dialog_history.insert(Tkinter.END, header)
        self.dialog_history.update_idletasks()
            
        statement = statement.strip() + '\n'
        for c in list(statement):
            self.dialog_history.see('end')
            self.dialog_history.insert(Tkinter.END, c)
            self.dialog_history.update_idletasks()
            time.sleep(0.0) # typematic delay
        self.dialog_history.see('end')            
        return
    
    def execute_query(self, *args):
        query = self.query.get().strip()
        self.push_dialog_history(query, 'user')
        response = self.theMetafor.handle_query(query)
        # update code views
        # a) python
        self.python_viewer.clear()
        self.python_viewer.insert(Tkinter.END, self.theMetafor.render_code(full_name='__main__', flavor='python'))
        self.python_viewer.update_idletasks()
        # b) clisp
        self.clisp_viewer.clear()
        self.clisp_viewer.insert(Tkinter.END, self.theMetafor.render_code(full_name='__main__', flavor='clisp'))
        self.clisp_viewer.update_idletasks()
        
        # b) model
        self.model_viewer.clear()
        self.model_viewer.insert(Tkinter.END, self.theMetafor.render_code(full_name='__main__', flavor='howTo'))
        self.model_viewer.update_idletasks()
        
        # update debug view
        self.visualizer.clear()
        self.visualizer.insert(Tkinter.END, self.theMetafor.pp_state_information())
        self.visualizer.update_idletasks()
        # post response
        if response:
            self.push_dialog_history(response, 'agent')
        self.query.clear()
        
######################################################################

if __name__ == '__main__':
    # logging.basicConfig(filename='MetaforGUI.log', level=logging.INFO)
    logging.basicConfig(level=logging.DEBUG, format='%(levelname)-8s %(message)s')
    logging.info('Started')
    
    root = Tkinter.Tk()
    Pmw.initialise(root, fontScheme='pmw1', size=18)
    root.title(title)
#    root.option_add('*Font',('Courier',14,'bold'))
    root.option_add('*Font', ('Serif', 10))

    widget = MetaforGUI(root)
    root.mainloop()
    
    logging.info('Finished')
        
