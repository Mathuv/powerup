# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import DepartmentForm
from forms import WorkItemForm
from .. import db
from ..models import Department
from ..models import WorkItem


def check_admin():
    """
    Prevent non-admins from accessing the page
    """
    if not current_user.is_admin:
        abort(403)

# Department Views


@admin.route('/departments', methods=['GET', 'POST'])
@login_required
def list_departments():
    """
    List all departments
    """
    check_admin()

    departments = Department.query.all()

    return render_template('admin/departments/departments.html',
                           departments=departments, title="Departments")


@admin.route('/departments/add', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add a department to the database
    """
    check_admin()

    add_department = True

    form = DepartmentForm()
    if form.validate_on_submit():
        department = Department(name=form.name.data,
                                description=form.description.data)
        try:
            # add department to the database
            db.session.add(department)
            db.session.commit()
            flash('You have successfully added a new department.')
        except:
            # in case department name already exists
            flash('Error: department name already exists.')

        # redirect to departments page
        return redirect(url_for('admin.list_departments'))

    # load department template
    return render_template('admin/departments/department.html', action="Add",
                           add_department=add_department, form=form,
                           title="Add Department")


@admin.route('/departments/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_department(id):
    """
    Edit a department
    """
    check_admin()

    add_department = False

    department = Department.query.get_or_404(id)
    form = DepartmentForm(obj=department)
    if form.validate_on_submit():
        department.name = form.name.data
        department.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the department.')

        # redirect to the departments page
        return redirect(url_for('admin.list_departments'))

    form.description.data = department.description
    form.name.data = department.name
    return render_template('admin/departments/department.html', action="Edit",
                           add_department=add_department, form=form,
                           department=department, title="Edit Department")


@admin.route('/departments/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_department(id):
    """
    Delete a department from the database
    """
    check_admin()

    department = Department.query.get_or_404(id)
    db.session.delete(department)
    db.session.commit()
    flash('You have successfully deleted the department.')

    # redirect to the departments page
    return redirect(url_for('admin.list_departments'))

    return render_template(title="Delete Department")


# Work Item Views

@admin.route('/workitems', methods=['GET', 'POST'])
@login_required
def list_workitems():
    """
    List all workitems
    """
    check_admin()

    workitems = WorkItem.query.all()

    return render_template('admin/workitems/workitems.html',
                           workitems=workitems, title="WorkItems")


@admin.route('/workitems/add', methods=['GET', 'POST'])
@login_required
def add_workitem():
    """
    Add a workitem to the database
    """
    check_admin()

    add_workitem = True

    form = WorkItemForm()
    if form.validate_on_submit():
        workitem = WorkItem(name=form.name.data,
                            description=form.description.data)
        try:
            # add workitem to the database
            db.session.add(workitem)
            db.session.commit()
            flash('You have successfully added a new workitem.')
        except:
            # in case workitem name already exists
            flash('Error: workitem name already exists.')

        # redirect to workitems page
        return redirect(url_for('admin.list_workitems'))

    # load workitem template
    return render_template('admin/workitems/workitem.html', action="Add",
                           add_workitem=add_workitem, form=form,
                           title="Add WorkItem")


@admin.route('/workitems/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_workitem(id):
    """
    Edit a workitem
    """
    check_admin()

    add_workitem = False

    workitem = WorkItem.query.get_or_404(id)
    form = WorkItemForm(obj=workitem)
    if form.validate_on_submit():
        workitem.name = form.name.data
        workitem.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the workitem.')

        # redirect to the workitems page
        return redirect(url_for('admin.list_workitems'))

    form.description.data = workitem.description
    form.name.data = workitem.name
    return render_template('admin/workitems/workitem.html', action="Edit",
                           add_workitem=add_workitem, form=form,
                           workitem=workitem, title="Edit WorkItem")


@admin.route('/workitems/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_workitem(id):
    """
    Delete a workitem from the database
    """
    check_admin()

    workitem = WorkItem.query.get_or_404(id)
    db.session.delete(workitem)
    db.session.commit()
    flash('You have successfully deleted the workitem.')

    # redirect to the workitems page
    return redirect(url_for('admin.list_workitems'))

    return render_template(title="Delete WorkItem")
