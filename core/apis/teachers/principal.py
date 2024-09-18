from flask import Blueprint
from core.apis import decorators,responses
from core.models.teachers import Teacher

from .schema import TeacherSchema


principal_teachers_resources = Blueprint("principal_teachers_resources",__name__)

@principal_teachers_resources.route("/",methods=["GET"],strict_slashes=False)
@decorators.authenticate_principal
def get_all_assigments(r):
    """Return All Teachers List"""
    all_teachers = Teacher.get_all_teachers()
    all_teachers_dump = TeacherSchema().dump(all_teachers, many=True)
    return responses.APIResponse.respond(data=all_teachers_dump)