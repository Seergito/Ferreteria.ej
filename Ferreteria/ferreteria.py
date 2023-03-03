from odoo import models,fields,api

class MiProveedor(models.Model):
    _name='miproveedor'
    codigo=fields.Integer('Codigo Proveedor')
    nombre=fields.Text('Nombre')
    direccion=fields.Text('Direccion')
    tipo=fields.Selection([('empresa','empresa'),('particular','particular')],'Tipo')

class MiArticulo(models.Model):
    _name='miarticulo'
    codigo=fields.Integer('Codigo Articulo')
    descripcion=fields.Text('Descipcion')
    stock=fields.Integer('Stock')
    precio=fields.Float('Precio')
    categoria=fields.Selection([('herrajes','herrajes'),('electricidad','electricidad')],'Categoria')
    codigoproveedor=fields.One2many('miproveedor','codigo','Codigo Proveedor')

class MiCliente(models.Model):
    _name='micliente'
    codigo=fields.Integer('Codigo Cliente')
    nombre=fields.Text('Nombre')
    direccion=fields.Text('Direccion')
    tipo=fields.Selection([('empresa','empresa'),('particular','particular')],'Tipo')
    anhonacimiento=fields.Integer('Año Nacimiento')
    edad=fields.Integer('Edad',compute='calcular_edad')
    
    @api.depends('anhonacimiento')
    def calcular_edad(self):
        self.edad=fields.Date.today().year-self.anhonacimiento

class MiVenta(models.Model):
    _name='miventa'
    codigo=fields.Integer('Codigo Venta')
    codigocliente=fields.One2many('micliente','codigo','Codigo Cliente')
    codigosarticulos=fields.Many2many('miarticulo','Articulos')
    base=fields.Float('Base')
    total=fields.Float('Total',compute='calcular_total')
    
    @api.depends('base')
    def calcular_total(self):
        self.total=self.base*1.21

    

    
    
