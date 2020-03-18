from app import db

class Master(db.Model):

    __tablename__ = "master"

    id = db.Column(db.Integer(), primary_key = True)
    material_of_construction = db.Column(db.String(255))
    moulding_process = db.Column(db.String(255))
    neck_type = db.Column(db.String(255))
    SKU = db.Column(db.String(255))
    product = db.Column(db.String(255))
    best_suited_for = db.Column(db.String(255))
    container_type = db.Column(db.String(255))
    vendor_name = db.Column(db.String(255))
    product_name = db.Column(db.String(255))
    ofc = db.Column(db.String(255))
    weight = db.Column(db.String(255))
    price = db.Column(db.String(255))
    shape = db.Column(db.String(255))

class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(300))
    data = db.Column(db.LargeBinary)
