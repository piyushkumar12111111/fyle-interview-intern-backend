from flask import Blueprint
from core import db
from core.apis import decorators,responses
from core.models.assignments import Assignment, AssignmentStateEnum
from core.models.teachers import Teacher

from .schema import AssignmentSchema, AssignmentGradeSchema
principal_assignments_resources = Blueprint("principal_assignments_resources",__name__)

@principal_assignments_resources.route("/assignments",methods=["GET"],strict_slashes=False)
@decorators.authenticate_principal
def get_all_assigments(r):
    """Return All Assignments that are Graded and Submited"""
    all_assignments = Assignment.get_all_assignments_for_principal()
    all_assignments_dump = AssignmentSchema().dump(all_assignments, many=True)
    return responses.APIResponse.respond(data=all_assignments_dump)

@principal_assignments_resources.route("/assignments/grade", methods=["POST"], strict_slashes=False)
@decorators.accept_payload
@decorators.authenticate_principal
def principal_grades_assignments(p, incoming_payload):
    """Principal Grades or re-grade an assignment"""
    grade_payload = AssignmentGradeSchema().load(incoming_payload)

    graded_assignment = Assignment.mark_grade_principal(
        _id=grade_payload.id,
        grade=grade_payload.grade,
        auth_principal=p
    )
    db.session.commit()
    graded_assignment_dump = AssignmentSchema().dump(graded_assignment)
    return responses.APIResponse.respond(data=graded_assignment_dump)

    