from app import app
from db_setup import init_db, db_session
from forms import SearchForm, ProductForm
from flask import flash, render_template, request, redirect, send_file
from models import Master, FileContents
from tables import Results
from io import BytesIO

init_db()

@app.route('/', methods = ['GET', 'POST'])
def index():
    search = SearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)

    return render_template('index.html', form = search)


@app.route('/results')
def search_results(search):
    results = []

    qry = db_session.query(Master).filter(
        Master.product.contains(search.data['product_select']), Master.shape.contains(search.data['shape_select']),
        Master.container_type.contains(search.data['type_select']), Master.SKU.contains(search.data['sku_search']))
    results = qry.all()

    if not results:
        flash('No results found!')
        return redirect('/')

    else:
        # display results
        table = Results(results)
        table.border = True
        return render_template('results.html', table = table)

@app.route('/new_product', methods = ['GET', 'POST'])
def new_product():
    # add a new product
    form = ProductForm(request.form)

    if request.method == 'POST' and form.validate():
        # saving new product
        product = Master()
        save_changes(product, form, new=True)
        file = request.files['inputFile']
        newFile = FileContents(name = file.filename, data = file.read())
        db_session.add(newFile)
        db_session.commit()
        flash('New product added successfully!')
        return redirect('/')

    return render_template('new_product.html', form=form)

'''@app.route('/upload', methods = ['GET', 'POST'])
def upload():

    if request.method == 'POST':
        file = request.files['inputFile']

        newFile = FileContents(name = file.filename, data = file.read())
        db_session.add(newFile)
        db_session.commit()

        return 'Saved' + file.filename + 'successfully'
    return render_template('upload.html')'''

@app.route('/item/<int:id>', methods = ['GET', 'POST'])
def download(id):
    qry = db_session.query(FileContents).filter(FileContents.id==id)
    image = qry.first()

    if image:
        return send_file(BytesIO(image.data), attachment_filename='image.jpg', as_attachment=True)

def save_changes(product, form, new=False):

    product.material_of_construction = form.material_of_construction.data
    product.moulding_process = form.moulding_process.data
    product.neck_type = form.neck_type.data
    product.SKU = form.SKU.data
    product.product = form.product.data
    product.best_suited_for = form.best_suited_for.data
    product.container_type = form.container_type.data
    product.vendor_name = form.vendor_name.data
    product.product_name = form.product_name.data
    product.ofc = form.ofc.data
    product.weight = form.weight.data
    product.price = form.price.data
    product.shape = form.shape.data

    if new:
        # add new product to the database
        db_session.add(product)

    # commit the data to the database
    db_session.commit()

if __name__ == '__main__':
    app.run()
