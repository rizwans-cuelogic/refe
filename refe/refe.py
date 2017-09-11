"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import List,String,Scope, Integer
from xblock.fragment import Fragment
from .utils import loader
from xblockutils.studio_editable import StudioEditableXBlockMixin


def status_list():
    list1=['Available','Not Available']
    return list1

def type_list():
    list2=['Document','Link','Video','Image']
    return list2


@XBlock.needs("i18n")
class ReferXBlock(StudioEditableXBlockMixin,XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    # TO-DO: delete count, and define your own fields.
    

    count = Integer(
        default=0, scope=Scope.user_state,
        help="A simple counter, to show something happening",
    )
    reference_name = String(display_name = "Reference Name",default=None,Scope=Scope.content)
    reference_type = List(list_style='set',values=['Document','Image','Link','Video'],display_name="Reference Link",Scope=Scope.content)
    reference_link = String(display_name = "Reference Link",default=None,Scope=Scope.content)
    reference_description = String(display_name = "Reference Description",multiline_editor=True,default=None,Scope=Scope.content)
    reference_status = List(list_style='set',values=['Document','Image','Link','Video'],display_name="Reference Link",Scope=Scope.content)

    editable_fields = ('reference_name', 'reference_type','reference_description',
                        'reference_link','reference_status')

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    # TO-DO: change this view to display your data your own way.
    def student_view(self, context=None):
        """
        The primary view of the ReferXBlock, shown to students
        when viewing courses.
        """
        context = {
            'reference_name': self.reference_name,
            'reference_description': self.reference_description,
            'reference_status': self.reference_status,
            'reference_link': self.reference_link,
            'reference_type':self.reference_type
        }
        fragment = Fragment()
        fragment.add_content(loader.render_template('/static/html/reference_list.html', context))
        fragment.add_css(self.resource_string("static/css/ref_list.css"))        
        return fragment        

    # TO-DO: change this handler to perform your own actions.  You may need more
    # than one handler, or you may not need any handlers at all.
    # @XBlock.json_handler
    # def increment_count(self, data, suffix=''):
    #     """
    #     An example handler, which increments the data.
    #     """
    #     # Just to show data coming in...
    #     assert data['hello'] == 'world'

    #     self.count += 1
    #     return {"count": self.count}

    # TO-DO: change this to create the scenarios you'd like to see in the
    # workbench while developing your XBlock.
    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ReferXBlock",
             """<refe/>
             """),
            ("Multiple ReferXBlock",
             """<vertical_demo>
                <refe/>
                <refe/>
                <refe/>
                </vertical_demo>
             """),
        ]


def status_list():
    list1=['Available','Not Available']
    return list1


def type_list():
    list2=['Document','Link','Video','Image']
    return list2
