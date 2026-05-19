import matplotlib.pyplot as plt
import pandas as pd

def crear_graficas_comparativas(df_crudo, df_limpio, ruta_grafica="comparativa_reactor.png"):
    """
    Genera un archivo de imagen con gráficos alineados para comparar la señal ruidosa vs la limpia.
    """
    try:
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8))

        # --- GRÁFICA 1: COMPARATIVA DE TEMPERATURA ---
        ax1.plot(df_crudo["Temperatura"], color="lightcoral", alpha=0.6, label="Señal Cruda (Con Outliers)")
        ax1.plot(df_limpio["Temperatura"], color="firebrick", linewidth=1.5, label="Señal Purificada (3-Sigma)")
        ax1.set_title("Control de Procesos: Historial de Temperatura en el Reactor", fontsize=12, fontweight='bold')
        ax1.set_xlabel("Número de Muestra")
        ax1.set_ylabel("Temperatura (°C)")
        ax1.legend(loc="upper right")
        ax1.grid(True, linestyle=":", alpha=0.6)

        # --- GRÁFICA 2: COMPARATIVA DE PRESIÓN ---
        ax2.plot(df_crudo["Presion"], color="skyblue", alpha=0.6, label="Señal Cruda (Con Outliers)")
        ax2.plot(df_limpio["Presion"], color="dodgerblue", linewidth=1.5, label="Señal Purificada (3-Sigma)")
        ax2.set_title("Control de Procesos: Historial de Presión en el Reactor", fontsize=12, fontweight='bold')
        ax2.set_xlabel("Número de Muestra")
        ax2.set_ylabel("Presión (psi)")
        ax2.legend(loc="upper right")
        ax2.grid(True, linestyle=":", alpha=0.6)

        plt.tight_layout()
        plt.savefig(ruta_grafica, dpi=300)
        plt.close()
        print(f"[Grupo 1 - OK] Gráfica comparativa guardada automáticamente como: '{ruta_grafica}'")
        return True
    except Exception as e:
        print(f"[Grupo 1 - ERROR] Falló la generación de las gráficas: {e}")
        return False
