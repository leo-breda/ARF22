import markdown
import os 
import random

def get_files():
    files = []
    fun_path = "md_files/Functional"
    real_path = "md_files/Real"
    dir_list = os.listdir(real_path)
    files.append(dir_list)
   
    dir_list = os.listdir(fun_path)
    files.append(dir_list)
    
    return files

def get_html(cap):
   
    preable_file_path = "preambe.sty"
    fun_path = "md_files/Functional"
    real_path = "md_files/Real"
    
    md = markdown.Markdown(
        extensions=['mdx_math'],
        extension_configs={
            'mdx-math': {'enable_dollar_delimiter': True}
        }
    )
    
    html = []
    html_Fu = []
    html_Re = []
    for file in cap[0]:
        with open(real_path+"/"+file, 'r') as mdfile:
            raw_data = mdfile.read()
            divided = raw_data.split("#")
            
            for block in divided[1:]:
                quest = []
                more = block.split('\n',1)
                quest.append(md.convert(more[0]))
                quest.append(md.convert(more[1]))
                html_Re.append(quest)
                
    for file in cap[1]:
        with open(fun_path+"/"+file, 'r') as mdfile:
            raw_data = mdfile.read()
            divided = raw_data.split("#")

            for block in divided[1:]:
                quest = []
                more = block.split('\n',1)
                quest.append(md.convert(more[0]))
                quest.append(md.convert(more[1]))
                html_Fu.append(quest)
    
   
    html = html_Re+html_Fu
    return html, list(range(len(html)))

if __name__ == "__main__":
   print(":D")
    
   