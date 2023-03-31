from fastapi import APIRouter

# al asignar un prefijo ya no es necesario colocar el path en las operaciones get, post, put, delete, etc...
# el tags=["products"].. sirve para que en la documentacion se agrupe todas las peticiones de esta api bajo el nombre dado en este caso ["products"]
router = APIRouter(prefix="/products",
                   tags=["Products"],
                   responses={404: {"message": "No encontrado"}})

products_list = ['Producto1', 'Producto2', 'Producto3', 'Producto4', 'Producto5']

#como ya se asigno un prefijo en el path colocas lo que vendria despues del prefijo (/products)
@router.get('/')
async def products():
    return products_list

@router.get('/{id}')
async def products(id: int):
    return products_list[id]












