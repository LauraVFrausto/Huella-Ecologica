#Autor: Christian Gutierrez
import streamlit as st
from PIL import Image

# Configuración del título de la app y el puntaje en session_state
if "puntaje_total" not in st.session_state:
    st.session_state.puntaje_total = 0
if "pregunta_actual" not in st.session_state:
    st.session_state.pregunta_actual = 1
if "seleccion" not in st.session_state:
    st.session_state.seleccion = None

# Lista de preguntas con opciones y puntos
preguntas = [
    {
        "texto": "¿Cuál es tu principal medio de transporte?",
        "opciones": [
            ("Transporte público", 0),
            ("Coche compartido", 1),
            ("Coche propio", 3),
            ("Moto propia", 2),
            ("Bicicleta o a pie", 0)
        ]
    },
    {
        "texto": "¿Cuántas veces viajas en avión cada año?",
        "opciones": [
            ("Cero", 0),
            ("1-2 veces", 2),
            ("3-5 veces", 4),
            ("Más de 5 veces", 6)
        ]
    },
    {
        "texto": "¿Con qué frecuencia consumes carne?",
        "opciones": [
            ("A diario", 3),
            ("2-4 veces a la semana", 2),
            ("1 vez a la semana", 1),
            ("Rara vez o nunca", 0)
        ]
    },
    {
        "texto": "¿Qué porcentaje de tus alimentos son procesados o vienen en envases desechables?",
        "opciones": [
            ("Más del 75%", 3),
            ("Entre 50% y 75%", 2),
            ("Entre 25% y 50%", 1),
            ("Menos del 25%", 0)
        ]
    },
    {
        "texto": "¿Qué tipo de energía usas principalmente en tu hogar?",
        "opciones": [
            ("Energía renovable", 0),
            ("Gas natural", 1),
            ("Electricidad", 2),
            ("Carbón o madera", 3)
        ]
    },
    {
        "texto": "¿Cuántos residuos generas aproximadamente cada semana?",
        "opciones": [
            ("Menos de una bolsa de basura", 0),
            ("1-2 bolsas de basura", 1),
            ("3-4 bolsas de basura", 2),
            ("Más de 4 bolsas de basura", 3)
        ]
    },
    {
        "texto": "¿Reciclas en casa?",
        "opciones": [
            ("Siempre", 0),
            ("Frecuentemente", 1),
            ("A veces", 2),
            ("Nunca", 3)
        ]
    }
]

# Si no se ha respondido la última pregunta, muestra la pregunta actual
if st.session_state.pregunta_actual <= len(preguntas):
    pregunta = preguntas[st.session_state.pregunta_actual - 1]
    st.header(f"Pregunta {st.session_state.pregunta_actual}: {pregunta['texto']}")

    # Carga y muestra el GIF correspondiente a la pregunta actual
    gif_path = f"images/{st.session_state.pregunta_actual}.gif"
    st.image(gif_path, use_column_width=True)

    # Opciones para la pregunta actual
    st.session_state.seleccion = st.radio(
        "Selecciona una opción:",
        [texto for texto, _ in pregunta["opciones"]],
        index=None,  # Desactiva la selección por defecto
        key=f"pregunta_{st.session_state.pregunta_actual}"
    )

    # Extrae los puntos de la selección y avanza a la siguiente pregunta
    if st.button("Siguiente"):
        if st.session_state.seleccion is not None:
            # Encuentra los puntos de la opción seleccionada
            puntos = next(p for texto, p in pregunta["opciones"] if texto == st.session_state.seleccion)
            st.session_state.puntaje_total += puntos
            st.session_state.pregunta_actual += 1
            st.session_state.seleccion = None  # Resetea la selección
        else:
            st.warning("Por favor, selecciona una opción antes de continuar.")

# Si ya se respondieron todas las preguntas, muestra el resultado final
else:
    st.subheader("Tu puntaje total es:")
    st.write(f"**{st.session_state.puntaje_total} puntos**")

    # Interpretación de los resultados
    st.header("Interpretación de los resultados")

    if st.session_state.puntaje_total <= 6:
        st.write("""
        ### Huella ecológica baja
        ¡Felicidades! Tienes hábitos sostenibles. Para mantener tu bajo impacto, considera:
        - Optimizar tu consumo: Revisa los productos que consumes y prioriza aquellos locales y de bajo impacto ambiental.
        - Continuar con la movilidad sostenible: Si es posible, sigue usando transporte público o bicicleta y evita el coche.
        - Maximizar el reciclaje: Asegúrate de reciclar adecuadamente y busca reducir aún más el uso de productos desechables.
        """)
    elif 7 <= st.session_state.puntaje_total <= 12:
        st.write("""
        ### Huella ecológica moderada
        Vas por buen camino, pero aún puedes hacer algunos ajustes para reducir tu huella. Prueba lo siguiente:
        - Reducir el consumo de carne: Considera reducir el consumo de carne a 1-2 veces por semana y explora proteínas vegetales.
        - Mejorar la eficiencia energética en el hogar: Cambia a bombillas LED, desconecta aparatos cuando no los uses, e intenta usar energías renovables.
        - Comprar a granel y evitar empaques: Lleva tus bolsas o frascos al hacer compras para reducir residuos.
        - Optar por menos vuelos: Si es posible, considera opciones de viaje menos intensivas en carbono o intenta agrupar tus vuelos para reducir la frecuencia anual.
        """)
    elif 13 <= st.session_state.puntaje_total <= 18:
        st.write("""
        ### Huella ecológica alta
        Tienes una huella ecológica considerable, y hay varias maneras de mejorar:
        - Reevaluar el transporte: Reduce el uso del coche o moto en la medida de lo posible. Opta por transporte público, bicicleta o caminar.
        - Ajustar la dieta: Intenta reducir tu consumo de productos de origen animal y explora opciones más vegetales.
        - Disminuir el consumo de productos envasados: Limita los productos procesados y prefiere comprar fresco y a granel.
        - Incrementar tus hábitos de reciclaje: Aprende a reciclar correctamente y asegúrate de separar tus residuos.
        """)
    else:
        st.write("""
        ### Huella ecológica muy alta
        Tienes un alto impacto ambiental y podrías reducir significativamente tu huella. Considera:
        - Cambiar hábitos de transporte: Usa transporte público, comparte coche o utiliza alternativas como la bicicleta.
        - Revisar tu consumo de energía: Si puedes, realiza una auditoría energética en casa y cambia a fuentes de energía renovables.
        - Reducir el consumo de carne y productos animales: Una dieta basada en plantas reduce drásticamente la huella ecológica.
        - Evitar productos de un solo uso: Sustituye los artículos desechables por opciones reutilizables y reduce tu producción de residuos.
        - Viajar menos en avión: Considera solo los viajes aéreos esenciales y, cuando sea posible, opta por trenes o buses.
        """)

    st.write("Cada cambio suma y ayuda a reducir tu huella ambiental. ¡Gracias por participar!")
