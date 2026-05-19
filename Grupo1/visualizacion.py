import matplotlib.pyplot as plt
import pandas as pd

def crear_graficas_comparativas(df_crudo, df_limpio, ruta_grafica="comparativa_reactor.png"):
    """Grafica temperatura y presion antes y despues del filtrado."""
    try:
        df_crudo = df_crudo.reset_index(drop=True)
        df_limpio = df_limpio.reset_index(drop=True)

        x_crudo = range(len(df_crudo))
        x_limpio = range(len(df_limpio))
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 8))

        ax1.plot(x_crudo, df_crudo["Temperatura"], color="lightcoral", alpha=0.6, label="Con outliers")
        ax1.plot(x_limpio, df_limpio["Temperatura"], color="firebrick", linewidth=1.5, label="Filtrado")
        ax1.set_title("Temperatura del reactor")
        ax1.set_xlabel("Muestra")
        ax1.set_ylabel("Temperatura (C)")
        ax1.legend(loc="upper right")
        ax1.grid(True, linestyle=":", alpha=0.6)

        ax2.plot(x_crudo, df_crudo["Presion"], color="skyblue", alpha=0.6, label="Con outliers")
        ax2.plot(x_limpio, df_limpio["Presion"], color="dodgerblue", linewidth=1.5, label="Filtrado")
        ax2.set_title("Presion del reactor")
        ax2.set_xlabel("Muestra")
        ax2.set_ylabel("Presion (psi)")
        ax2.legend(loc="upper right")
        ax2.grid(True, linestyle=":", alpha=0.6)

        plt.tight_layout()
        plt.savefig(ruta_grafica, dpi=300)
        plt.close()
        print(f"Grafica guardada: {ruta_grafica}")
        return True
    except Exception as e:
        print(f"Error al generar la grafica: {e}")
        return False
