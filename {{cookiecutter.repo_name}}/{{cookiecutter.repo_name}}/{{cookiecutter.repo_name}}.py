#coding=utf-8
#author_name: {{cookiecutter.author_name}}
#author_email: {{cookiecutter.email}}


"""
{{cookiecutter.repo_name}}XBlock main Python class
VERSION: {{cookiecutter.version}}
{{cookiecutter.description}}
xblock-tutorial: http://edx.readthedocs.org/projects/xblock-tutorial/en/latest/concepts/index.html
"""

import pkg_resources
from django.template import Context, Template

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean #List, Set, Float, Dict
from xblock.fragment import Fragment

from mako.lookup import TemplateLookup
from lazy import lazy

class {{cookiecutter.repo_name}}XBlock(XBlock):

    '''
    Icon of the XBlock. Values : [other (default), video, problem]
    '''
    icon_class = "video"

    '''
    Fields
    #scope
    *  Scope.content : Block definition / No user
    *  Scope.settings : Block usage / No user
    *  Scope.user_state : Block usage / One user
    *  Scope.preferences : Block type / One user
    *  Scope.user_info : All blocks / One user
    *  Scope.user_state_summary : Block usage / All users
    '''
    display_name = String(display_name="Display Name",
        default="{{cookiecutter.repo_name}}",
        scope=Scope.settings,
        help="This name appears in the horizontal navigation at the top of the page.")

    [[%for field in fields%]]
    <<%field%>> = String(display_name="<<%field%>>",
        default="<<%field%>>",
        scope=Scope.settings,
        help="")
    [[%endfor%]]


    '''
    Util functions
    '''

    '''
    def load_resource(self, resource_path):
        """
        Gets the content of a resource
        """
        resource_content = pkg_resources.resource_string(__name__, resource_path)
        return unicode(resource_content)

    def render_template(self, template_path, context={}):
        """
        Evaluate a template by resource path, applying the provided context
        """
        template_str = self.load_resource(template_path)
        return Template(template_str).render(Context(context))
    '''

    @lazy
    def template_lookup(self):
        return TemplateLookup(
            directories=[pkg_resources.resource_filename(__name__, '.')],input_encoding="utf-8"
        )

    def load_resource(self, resource_path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, resource_path)
        return data.decode("utf8")

    def render_template(self, template_path, context={}):
        """
        """
        #template_str = self.resource_string(template_path)
        return self.template_lookup.get_template(template_path).render_unicode(**context)


    '''
    Main functions
    #frag add :
        *  frag.add_javascript_url("http://echarts.baidu.com/doc/asset/js/codemirror.js")
        *  frag.add_css_url("http://echarts.baidu.com/doc/asset/js/codemirror.css")
    '''
    def student_view(self, context=None):
        """
        The primary view of the XBlock, shown to students
        when viewing courses.
        """
        context = {
            [[%for field in fields%]]
            '<<%field%>>': self.<<%field%>>,
            [[%endfor%]]
            'display_name': self.display_name
        }
        html = self.render_template('static/html/{{cookiecutter.repo_name}}_view.html', context)
        frag = Fragment(html)
        #
        frag.add_javascript(self.load_resource("static/js/{{cookiecutter.repo_name}}_view.js"))
        frag.initialize_js('{{cookiecutter.repo_name}}XBlockInitView')
        return frag

    def studio_view(self, context=None):
        """
        The secondary view of the XBlock, shown to teachers
        when editing the XBlock.
        """
        context = {
            [[%for field in fields%]]
            '<<%field%>>': self.<<%field%>>,
            [[%endfor%]]
            'display_name': self.display_name
        }
        html = self.render_template('static/html/{{cookiecutter.repo_name}}_edit.html', context)

        frag = Fragment(html)
        frag.add_javascript(self.load_resource("static/js/{{cookiecutter.repo_name}}_edit.js"))
        frag.initialize_js('{{cookiecutter.repo_name}}XBlockInitStudio')
        return frag

    @XBlock.json_handler
    def save_{{cookiecutter.repo_name}}(self, data, suffix=''):
        """
        The saving handler.
        """
        [[%for field in fields%]]
        self.<<%field%>> = data['<<%field%>>']
        [[%endfor%]]

        self.display_name = data['display_name']
        return {
            'result': 'success',
        }

    @XBlock.json_handler
    def get_params(self, data, suffix=''):
        '''called when {{cookiecutter.repo_name}} init'''
        return {
            [[%for field in fields%]]
            '<<%field%>>': self.<<%field%>>,
            [[%endfor%]]
            'display_name': self.display_name
                }

    @staticmethod
    def workbench_scenarios():
        return [
              ("{{cookiecutter.repo_name}} demo", "<{{cookiecutter.repo_name}} />")  #the name should be "<{{cookiecutter.repo_name}} />"
        ]
