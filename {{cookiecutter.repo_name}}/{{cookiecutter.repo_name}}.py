#coding=utf-8
#author: wwj718
#author_email: wuwenjie718@gmail.com
#author_blog: wwj718.github.io

""" {{cookiecutter.repo_name}}XBlock main Python class"""

import pkg_resources
from django.template import Context, Template

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String, Boolean
from xblock.fragment import Fragment

class {{cookiecutter.repo_name}}XBlock(XBlock):

    '''
    Icon of the XBlock. Values : [other (default), video, problem]
    '''
    icon_class = "video"

    '''
    Fields
    '''
    display_name = String(display_name="Display Name",
        default="{{cookiecutter.repo_name}} player",
        scope=Scope.settings,
        help="This name appears in the horizontal navigation at the top of the page.")

    iframe = String(display_name="iframe",
        default="{{cookiecutter.repo_name}} player",
        scope=Scope.settings,
        help="iframe")



    width = Integer(display_name="Video player width",
	default="560",
	scope=Scope.content,
	help="The width for your video player.")
    height = Integer(display_name="Video player height",
	default="320",
	scope=Scope.content,
	help="The height for your video player.")

    '''
    Util functions
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
    Main functions
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
