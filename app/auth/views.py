# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from forms import LoginForm, RegistrationForm, ProjectItemForm
from .. import db
from ..models import Employee, ProjectItem


@auth.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handle requests to the /register route
    Add an employee to the database through the registration form
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        employee = Employee(email=form.email.data,
                            username=form.username.data,
                            first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            postcode=form.postcode.data,
                            phone=form.phone.data,
                            password=form.password.data)

        # add employee to the database
        db.session.add(employee)
        db.session.commit()
        flash('You have successfully registered! You may now login.')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/register.html', form=form, title='Register')


@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        employee = Employee.query.filter_by(email=form.email.data).first()
        if employee is not None and employee.verify_password(
                form.password.data):
            # log employee in
            login_user(employee)

            # redirect to the dashboard page after login
            if employee.is_admin:
                return redirect(url_for('home.admin_dashboard'))
            else:
                return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            flash('Invalid email or password.')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')


@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('You have successfully been logged out.')

    # redirect to the login page
    return redirect(url_for('auth.login'))


# Project Item Views

@auth.route('/projectitems', methods=['GET', 'POST'])
@login_required
def list_projectitems():
    """
    List all projectitems
    """

    projectitems = ProjectItem.query.all()

    return render_template('home/projectitems/projectitems.html',
                           projectitems=projectitems, title="ProjectItems")


@auth.route('/projectitems/add', methods=['GET', 'POST'])
@login_required
def add_projectitem():
    """
    Add a projectitem to the database
    """

    add_projectitem = True

    form = ProjectItemForm()
    if form.validate_on_submit():
        # projectitem = ProjectItem(name=form.name.data,
        #                           description=form.description.data)
        projectitem = ProjectItem(account_id=form.account.data, workitem_id=form.workitem.data,
                                  start_date=form.start_date.data, end_date=form.end_date.data, more_details=form.more_details.data)
        try:
            # add projectitem to the database
            db.session.add(projectitem)
            db.session.commit()
            flash('You have successfully added a new projectitem.')
        except:
            # in case projectitem name already exists
            flash('Error: projectitem name already exists.')

        # redirect to projectitems page
        return redirect(url_for('auth.list_projectitems'))

    # load projectitem template
    return render_template('home/projectitems/projectitem.html', action="Add",
                           add_projectitem=add_projectitem, form=form,
                           title="Add ProjectItem")


@auth.route('/projectitems/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_projectitem(id):
    """
    Edit a projectitem
    """

    add_projectitem = False

    projectitem = ProjectItem.query.get_or_404(id)
    form = ProjectItemForm(obj=projectitem)
    if form.validate_on_submit():
        projectitem.name = form.name.data
        projectitem.description = form.description.data
        db.session.commit()
        flash('You have successfully edited the projectitem.')

        # redirect to the projectitems page
        return redirect(url_for('auth.list_projectitems'))

    form.description.data = projectitem.description
    form.name.data = projectitem.name
    return render_template('home/projectitems/projectitem.html', action="Edit",
                           add_projectitem=add_projectitem, form=form,
                           projectitem=projectitem, title="Edit ProjectItem")


@auth.route('/projectitems/delete/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_projectitem(id):
    """
    Delete a projectitem from the database
    """

    projectitem = ProjectItem.query.get_or_404(id)
    db.session.delete(projectitem)
    db.session.commit()
    flash('You have successfully deleted the projectitem.')

    # redirect to the projectitems page
    return redirect(url_for('auth.list_projectitems'))

    return render_template(title="Delete ProjectItem")
