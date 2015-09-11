"""
The script will run after built the project
"""
import os
import shutil
from jinja2 import Environment,FileSystemLoader
import re
import glob

#fake data
fields=["name","age","school"]

project_directory = os.path.realpath(os.path.curdir) #the generate project
html_directory = os.path.join(
                project_directory,
                'static/html'
                )
js_directory = os.path.join(
                project_directory,
                'static/js'
                )


env = Environment(loader=FileSystemLoader([html_directory,js_directory,project_directory]),variable_start_string="<<%",variable_end_string="%>>",
        block_start_string="[[%",block_end_string="%]]")
html_files = os.listdir(html_directory)


#render html
for html_file in html_files:
    #print html_file
    template = env.get_template(html_file)
    output =  template.render(fields=fields)
    #replace value for {{field}}
    html_file_realpsth =  os.path.join(html_directory,html_file)
    #output = re.sub(r'value=\"(?P<field>[^\"\']*)\"',r"{{\g<field>}}",str(output))
    with open(html_file_realpsth, 'w') as f:
        f.write(output)

#render js
#js_files = glob.glob(js_directory+"/*.js")
js_files = os.listdir(js_directory)
for js_file in js_files:
    #print js_file
    template = env.get_template(js_file)
    output =  template.render(fields=fields)
    js_file_realpsth =  os.path.join(js_directory,js_file)
    with open(js_file_realpsth, 'w') as f:
        f.write(output)

#render py
py_files = glob.glob("*.py")
#print py_files
for py_file in py_files:
    template = env.get_template(py_file)
    output =  template.render(fields=fields)
    py_file_realpsth =  os.path.join(project_directory,py_file)
    with open(py_file_realpsth, 'w') as f:
        f.write(output)
