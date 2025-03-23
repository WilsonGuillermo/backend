""" Ejemplo de Script para Iniciar Ambos Backends

Crear un script `run_both_backends.py` que maneje la inicialización de ambos backends:

"""

import multiprocessing
from backend_producto import create_app as create_app_new
from backend_usuario import create_app as create_app_main

def run_main_backend():
    app = create_app_main()
    app.run(host='0.0.0.0', port=5000, debug=True)

def run_new_backend():
    app = create_app_new()
    app.run(host='0.0.0.0', port=5001, debug=True)

if __name__ == '__main__':
    # Crear los procesos para cada backend
    p1 = multiprocessing.Process(target=run_main_backend)
    p2 = multiprocessing.Process(target=run_new_backend)

    # Iniciar ambos procesos
    p1.start()
    p2.start()

    # Esperar a que ambos procesos terminen
    p1.join()
    p2.join()
