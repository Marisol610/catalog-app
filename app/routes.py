#!/products/bin/env python3
#-*- coding utf8 -*-
""" This is the routes for product application """







from flask import request, render_template
from app import app
from app.database import create, read, update, delete, scan
from datetime import datetime
from flask import request
from app.forms.product import ProductForm



#product CRUD
@app.route("/")
def index():
    serv_time = datetime.now().strftime("%F %H:%M:%S")
    return {
        "ok": True,
        "version": "1.0.0",
        "server_time": serv_time
    }

@app.route("/product_form", methods=["GET", "POST"])
def product_form():
    if request.method == "POST":
        name = request.form.get("name")
        price = request.form.get("price")
        description = request.form.get("description")
        category = request.form.get("category")
        quantity = request.form.get("quantity")
        unique_tag = request.form.get("unique_tag")


        create(name, price, description, category, quantity, unique_tag)
    form = ProductForm()
    return render_template("form_example.html", form=form)


@app.route("/products")
def get_all_products():
    out = scan()
    out["ok"] = True
    out["message"] = "Success"
    #return out
    return render_template("products.html", products=out["body"])


@app.route("/products/<pid>")
def get_one_product(pid):
    out = read(int(pid))
    out["ok"] = True
    out["message"] = "Success"
    return out


@app.route("/products", methods = ["POST"])
def create_product():
    product_data = request.json
    new_id = create(
        product_data.get("name"),
        product_data.get("price"),
        product_data.get("description"),
        product_data.get("category"),
        product_data.get("quantity"),
        product_data.get("unique_tag")
    )

    return {"ok": True, "message": "Success", "new_id": new_id}


@app.route("/products/<pid>", methods=["GET", "PUT"])
def update_product(pid):
    #product_data = request.jason
    if request.method =="PUT":
        update(pid, request.form)
        return {"ok": True, "message": "Updated"}
    out = read(int(pid))
    update_form = ProductForm()
    if out["body"]:
        return render_template("single_product.html", product=out["body"][0], form=update_form)
    else:
        return render_template("404.html"), 404



@app.route("/products/delete/<pid>", methods=["GET"])
def delete_product(pid):
    out = update(int(pid), {"active": 0})

    return {"ok": out, "message": "Deleted"}



#@app.route("/products/delete/<pid>", methods=["GET"])
#def delete_product(pid):
 #   id= input("Enter the id for the item you wish to delete")

  #  for product in products:
   #     if(str(prod.id) == id):
    #    delete(pid, request.form)
     #   return {"ok": True, "message": "Updated"}


    







@app.route('/agent')
def agent():
    user_agent = request.headers.get("User-Agent")
    return "<p>Your user agent is %s</p>" % user_agent


@app.route("/myroute")
def my_view_function():
    return render_template("index.html")




# user CRUD
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)


@app.route("/user/<name>")
def show_user(name):
    return render_template("user.html", name=name)



@app.route("/about")
def about():
    return render_template("about.html", first_name="Marisol", last_name="Rodriguez", hobbies="Crochet and Baking")


@app.route("/users")
def get_all_users():
    out = scan()
    out["ok"] = True
    out["message"] = "Success"
    return out


@app.route("/users/<uid>")
def get_one_user(uid):
    out = read(int(uid))
    out["ok"] = True
    out["message"] = "Success"
    return out

    
@app.route("/users", methods = ["POST"])
def create_user():
    user_data = request.json
    new_id = create(
        user_data.get("name"),
        user_data.get("last name"),
        user_data.get("hobbies"),
        
    )

    return {"ok": True, "message": "Success", "new_id": new_id}

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


