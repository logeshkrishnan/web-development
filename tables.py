from flask_table import Table, Col, LinkCol

class Results(Table):
    id = Col('Id', show=False)
    material_of_construction = Col('Material of construction')
    moulding_process = Col('Moulding process')
    neck_type = Col('Neck type')
    SKU = Col('SKU')
    product = Col('Product')
    best_suited_for = Col('Best suited for')
    container_type = Col('Container type')
    vendor_name = Col('Vendor name')        
    product_name = Col('Product name')
    ofc = Col('OFC')
    weight = Col('Weight')
    price = Col('Price')
    shape = Col('Shape')
    dowload_image = LinkCol('Image', 'download', url_kwargs=dict(id='id'))
