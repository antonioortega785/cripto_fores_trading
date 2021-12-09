
class orden:
    def __init__(
            self,
            precio_,
            monto_,
            mercado_,
            fecha_,
            tipo_,
            estado_
        ):
        self.precio = precio_
        self.monto_ = monto_
        self.mercado = mercado_
        self.fecha = fecha_
        self.tipo = tipo_
        self.estado = estado_
class mercado:

    ordenes_compra = []
    ordenes_venta = []

    def __init__(
        self,
        segundos_actualizacion_,
        listas_precios_
        ):
        self.segundos_actualizacion = segundos_actualizacion_
        self.listas_precios = listas_precios_

    def restructurar_ordenes(
        self
        ):

class pedir_precios:

class pedir_ordenes:
