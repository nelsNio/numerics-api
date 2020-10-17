# API  ENCARGADA DE aplanar una secuencia anidada en una sola lista de valores.


### Ejecución:
1) Descargar repositorio
2) Ubicarse dentro del proyecto descargado
3) Instalar dependencias con el comando **pip3 install -r requirements.txt**
4) Hacer migraciones  con **python3 manage.py migrate**
5) Ejecutar servidor en local con **python3 manage.py runserver**


### Host 
**Local**:  http://127.0.0.1:8000/


## Endpoints 
1) **Listar historico de resultados**: Method ```GET```, API: ```numbers/history/```
2) **Aplanar una lista**: Method ```POST```, API: ```numbers/render_list/```, Body ```{
    "items": [1, 2, [3, 4, [5, 6], 7], 8]
}```

## Autor:
NELSON ANDRES NIÑO VERDUGO
