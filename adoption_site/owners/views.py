from flask import Blueprint, render_template, redirect, url_for
from adoption_site import db
from adoption_site.models import Owner
from adoption_site.owners.forms import AddForm

owners_blueprint = Blueprint("owners", __name__, template_folder="templates")


@owners_blueprint.route("/add", methods = ["POST", "GET"])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        new_owner = Owner(name, pup_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for("owners.list"))
    
    return render_template("owners/add.html", form = form)


@owners_blueprint.route("/list")
def list():
    owners = Owner.query.all()
    return render_template("owners/list.html", owners = owners)