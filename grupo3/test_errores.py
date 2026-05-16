import os
import sys
 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
from grupo3.data_carga import cargar_datos
 
VERDE   = "\033[92m"
ROJO    = "\033[91m"
NEGRITA = "\033[1m"
RESET   = "\033[0m"
 
_resultados = []
 
 
def _probar(nombre: str, ruta: str, excepcion_esperada=None):
    try:
        df = cargar_datos(ruta)
        if excepcion_esperada is None:
            print(f"{VERDE}  ✔ PASÓ{RESET}  {nombre}")
            print(f"         DataFrame: {df.shape[0]} filas × {df.shape[1]} cols "
                  f"— columnas: {list(df.columns)}")
            _resultados.append(True)
        else:
            print(f"{ROJO}  ✘ FALLÓ{RESET}  {nombre}")
            print(f"         Se esperaba {excepcion_esperada.__name__} "
                  "pero no se lanzó ninguna excepción.")
            _resultados.append(False)
    except Exception as exc:
        if excepcion_esperada and isinstance(exc, excepcion_esperada):
            print(f"{VERDE}  ✔ PASÓ{RESET}  {nombre}")
            print(f"         {type(exc).__name__} capturada → {exc}")
            _resultados.append(True)
        else:
            print(f"{ROJO}  ✘ FALLÓ{RESET}  {nombre}")
            print(f"         Excepción inesperada ({type(exc).__name__}): {exc}")
            _resultados.append(False)
 
 
def ejecutar_pruebas(carpeta: str = "grupo2/datos_prueba"):
    print("=" * 60)
    print("  PRUEBAS DE MANEJO DE ERRORES – GRUPO 3")
    print("=" * 60)
 
    print(f"\n{NEGRITA}[1] Ruta inexistente{RESET}")
    _probar(
        excepcion_esperada=FileNotFoundError,
    )
 
    print(f"\n{NEGRITA}[2] CSV vacío  →  vacio.csv{RESET}")
    _probar(
    
        os.path.join(carpeta, "vacio.csv"),
        excepcion_esperada=ValueError,
    )
 
    print(f"\n{NEGRITA}[3] Solo encabezados  →  sin_filas.csv{RESET}")
    _probar(
    
        os.path.join(carpeta, "sin_filas.csv"),
        excepcion_esperada=ValueError,
    )
 
    print(f"\n{NEGRITA}[4] Todo texto, sin números  →  letras.csv{RESET}")
    _probar(
    
        os.path.join(carpeta, "letras.csv"),
        excepcion_esperada=ValueError,
    )
 
    print(f"\n{NEGRITA}[5] Columnas incompletas  →  columnas_incompletas.csv{RESET}")
    _probar(

        os.path.join(carpeta, "columnas_incompletas.csv"),
        excepcion_esperada=None,
    )
 
    print(f"\n{NEGRITA}[6] CSV válido  →  correcto.csv{RESET}")
    _probar(
        os.path.join(carpeta, "correcto.csv"),
        excepcion_esperada=None,
    )
 
    total   = len(_resultados)
    pasaron = sum(_resultados)
    color   = VERDE if pasaron == total else ROJO
    print("\n" + "=" * 60)
    print(f"  Resultado: {pasaron}/{total} pruebas pasaron.  "
          f"{color}{'✔ Todo en orden.' if pasaron == total else f'✘ {total - pasaron} fallo(s).'}{RESET}")
    print("=" * 60)
 
 
if __name__ == "__main__":
    CARPETA = "grupo2/datos_prueba"
    if not os.path.isdir(CARPETA):
        print(f"Generando CSVs de prueba del Grupo 2...")
        try:
            from grupo2.testing import generar_csvs_corruptos
            generar_csvs_corruptos(CARPETA)
        except ImportError:
            print("ERROR: No se encontró grupo2/testing.py.")
            sys.exit(1)
 
    ejecutar_pruebas(CARPETA)