# SOCIAL_MEDIA HUB

El objetivo principal de esta aplicación es desarrollar una plataforma web robusta utilizando **Python** y **Flask** que funcione como un orquestador de microservicios, integrando múltiples APIs externas para la visualización de datos dinámicos en tiempo real.

## Metas Específicas

La aplicación demuestra la capacidad de consumir servicios web heterogéneos y presentarlos en una interfaz unificada, amigable y responsiva, simulando un ecosistema digital que integra:

* **Publicaciones Dinámicas:** Simulación de un feed de red social mediante el consumo de JSON estructurado.
* **Inteligencia Meteorológica:** Visualización de condiciones climáticas actuales con procesamiento de datos en tiempo real.
* **Actualidad Informativa:** Despliegue de titulares de noticias de última hora mediante filtrado parametrizado.
<br>
  
---

### Integrantes 
Hernández Torrez Alondra Vianney-1224100684 

Silva Solano Maria Gabriela-1224100716 

---

<br>

# Integración de APIs

Esta aplicación consume tres fuentes de datos externas para proporcionar una experiencia enriquecida y funcional.

---

### 1. API de Red Social (DummyJSON)
Se utiliza para simular el ecosistema de una red social dentro de la interfaz.

* **URL Base:** `https://dummyjson.com`
* **Endpoint:** `/posts`
* **Función:** Simular publicaciones y actividad de usuarios.
* **Utilidad en la App:**
    * Generación de un **feed dinámico**.
    * Visualización de títulos, contenido y reacciones.
    * Prototipado de experiencia de usuario con datos realistas.

### 2. API de Clima (OpenWeather)
Proporciona datos meteorológicos en tiempo real basados en la ubicación.

* **Endpoint:** `/data/2.5/weather`
* **Autenticación:** Requiere `API Key`.
* **Datos extraídos:**
    *  Temperatura actual.
    *  Humedad.
    *  Descripción climática.
* **Utilidad en la App:** Aporta información contextual útil y personalizada para el usuario.

### 3. API de Noticias (NewsAPI)
Mantiene la plataforma actualizada con las últimas novedades globales.

* **Endpoint:** `/v2/everything`
* **Autenticación:** Requiere `API Key`.
* **Configuración:** Filtrado de noticias actuales en **español**.
* **Datos mostrados:**
    * Título y descripción breve.
    * Enlace directo a la fuente original.
* **Utilidad en la App:** Ofrecer contenido relevante y veraz de diversas fuentes informativas.
---
<br>
<br>
# Codificación
## Services 
Esta carpeta organiza diferentes integraciones de APIs externas mediante una arquitectura de servicios modulares en Python.

### Estructura del Directorio

El proyecto separa las responsabilidades en el paquete `/services`:
- `__init__.py`: Inicializa la carpeta como un paquete de Python.
- `news_api.py`: (Pendiente) Módulo para servicios de noticias.
- `social_api.py`: Gestiona la conexión con la API de redes sociales (DummyJSON).
- `weather_api.py`: (Pendiente) Módulo para servicios meteorológicos.

### News API Service 

El archivo `news_api.py` se encarga de la integración con **NewsAPI** para obtener los titulares más relevantes de México utilizando una autenticación segura mediante variables de entorno.

```env
import requests
import os
from dotenv import load_dotenv

# Carga de variables de entorno
load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")
BASE_URL = "[https://newsapi.org/v2/top-headlines](https://newsapi.org/v2/top-headlines)"

def get_news():
    #Consulta las noticias principales de México.
    #Retorna: list de objetos 'articles'.
    params = {
        "country": "mx",
        "apiKey": API_KEY
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()["articles"]
```
### Implementación de Social API

El archivo `social_api.py` contiene la lógica para recuperar publicaciones de forma eficiente:
```python
import requests

# Configuración global
BASE_URL = "[https://dummyjson.com](https://dummyjson.com)"

def get_posts():
    #Realiza una petición GET a la API y devuelve la lista de posts.
    #Retorna: list de diccionarios con los datos de las publicaciones.
    
    response = requests.get(f"{BASE_URL}/posts")
    return response.json()["posts"]
```
### Weather API Service 

El archivo `weather_api.py`se encarga de la integración con **OpenWeatherMap** para obtener datos climáticos en tiempo real de forma segura y personalizada.
```python
import requests
import os
from dotenv import load_dotenv

# Inicialización de entorno
load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "[https://api.openweathermap.org/data/2.5/weather](https://api.openweathermap.org/data/2.5/weather)"

def get_weather(city="Guadalajara"):
   # Consulta el clima actual de una ciudad específica.
   # Argumentos: city (str) - Nombre de la ciudad.
   # Retorna: dict con la respuesta completa de la API.
    
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()
```

## Templates 
Esta carpeta contiene las vistas de la aplicación. Se utiliza un motor de plantillas (como Jinja2) para renderizar dinámicamente los datos obtenidos de los servicios de API.

### Estructura 
- **`base.html`**: Es la plantilla maestra. Contiene las etiquetas `<html>`, `<head>`, la importación de CSS y la estructura del menú de navegación. Define bloques (`blocks`) donde las otras páginas insertarán su contenido.
- **`index.html`**: Página de inicio. Renderiza la lista de publicaciones obtenidas a través de `social_api.py`.
- **`news.html`**: Vista dedicada a las noticias. Formatea y muestra los artículos recuperados por `news_api.py`.
- **`weather.html`**: Interfaz meteorológica. Muestra los datos de temperatura y estado del clima procesados por `weather_api.py`.

### Plantilla principal 
El archivo `base.html` es el núcleo visual de la aplicación. Utiliza el motor de plantillas de **Flask** para implementar una arquitectura de diseño consistente en todo el sitio.
```python
# Este archivo define el diseño global de la aplicación SocialMedia Hub.
# Funciona como un esqueleto que hereda sus elementos a las demás páginas
# (index, news, weather) para evitar la duplicación de código.

<!DOCTYPE html>
<html lang="es">
<head>
    {# Configuración técnica: Juego de caracteres y escalado para dispositivos móviles #}
    <meta charset="UTF-8">
    <title>SocialMedia Hub</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    # VINCULACIÓN DINÁMICA DE ESTILOS:
    # Se usa url_for de Flask para buscar 'styles.css' dentro de la carpeta /static/css.
    # Esto asegura que el diseño cargue correctamente sin importar la ruta actual. 
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>

<header>
    # Encabezado principal y Logotipo del sitio 
    <h1> SocialMedia Hub</h1>
    
    #   BARRA DE NAVEGACIÓN:
    #   Define el acceso a los tres servicios principales del proyecto:
    #   - Inicio: Muestra publicaciones (social_api.py)
    #   - Clima: Muestra el tiempo (weather_api.py)
    #   - Noticias: Muestra titulares (news_api.py)
    
    <nav>
        <a href="/">Inicio</a>
        <a href="/weather">Clima</a>
        <a href="/news">Noticias</a>
    </nav>
</header>

<main>
      # BLOQUE DE CONTENIDO DINÁMICO:
      # Esta es la parte más importante. La etiqueta {% block content %} actúa como 
      # un "espacio reservado" donde se inyectará el HTML específico de cada página 
      # hija que use la instrucción 'extends'.
    
    {% block content %}{% endblock %}
</main>

</body>
</html>
```
### Vista de Inicio 
El archivo `index.html` e encarga de renderizar el "Feed" de noticias sociales consumido desde la API externa.
```python

{% extends "base.html" %}
{% block content %}
{# Encabezado de la sección #}
<h2>Publicaciones</h2>

  # CONTENEDOR GRID:
  # Organiza las publicaciones en una cuadrícula. 
  # Depende de las reglas definidas en styles.css para el diseño de tarjetas.
<div class="grid">

      # CICLO DINÁMICO:
      # Itera sobre la variable 'posts' enviada por el controlador de Flask 
      # (proveniente de social_api.py).
    
    {% for post in posts %}
        <div class="card">
            {# Muestra el título de la publicación #}
            <h3>{{ post.title }}</h3>
            
            #  MANIPULACIÓN DE TEXTO:
            #  Muestra solo los primeros 100 caracteres del cuerpo del post 
            #  Seguido de puntos suspensivos para mantener un diseño uniforme.
            
            <p>{{ post.body[:100] }}...</p>
            
            # Muestra los metadatos de interacción 
            <p> Likes: {{ post.reactions }}</p>
        </div>
    {% endfor %}
</div>

{% endblock %}
```
### Vista de Noticias
El archivo ` news.html` es la interfaz de usuario para el consumo de información de actualidad, conectada directamente con el módulo de NewsAPI.
```python
{% extends "base.html" %}

{% block content %}

<h2>Noticias en México</h2>

 
#   CONTENEDOR GRID:
#   Aprovecha las clases de CSS globales para mostrar los artículos 
#   en un formato de rejilla responsiva. 

<div class="grid">
    
    #   ITERACIÓN DE ARTÍCULOS:
    #   Recorre la variable 'news' enviada desde el backend. 
    #   Cada 'article' contiene la información procesada de NewsAPI.
    
    {% for article in news %}
        <div class="card">
            {# Renderiza el título original de la noticia #}
            <h3>{{ article.title }}</h3>
            
            #   DESCRIPCIÓN:
            #   Muestra el resumen o abstract proporcionado por la fuente 
            #   periodística para dar contexto al usuario.
            
            <p>{{ article.description }}</p>
            
            #   ENLACE EXTERNO:
            #  El atributo target="_blank" es una buena práctica aquí para 
            #  que el usuario no pierda su sesión en SocialMedia Hub al 
            #   ir a leer la noticia completa.

            <a href="{{ article.url }}" target="_blank">Leer más</a>
        </div>
    {% endfor %}
</div>

{% endblock %}
```
### Vista de Clima
El archivo `weather.html` es la interfaz de usuario para el servicio meteorológico de OpenWeatherMap, diseñada para ser robusta y limpia.
```python
{% extends "base.html" %}

{% block content %}

<h2>🌤 Clima Actual</h2>

<div class="card">
    {# Muestra el nombre de la ciudad consultada (ej. Guadalajara) #}
    <h3>{{ weather.name }}</h3>

    
    #   CONTROL DE ERRORES:
    #   Verifica si el objeto 'weather' contiene la llave 'main'. 
    #   Si la API de OpenWeather no encontró la ciudad o falló, 
    #   evitamos errores de renderizado mostrando el bloque 'else'.
    
    {% if weather.main %}
        {# Acceso a datos anidados: temperatura y humedad #}
        <p>🌡 Temperatura: {{ weather.main.temp }} °C</p>
        <p>💧 Humedad: {{ weather.main.humidity }}%</p>
        
        #   DESCRIPCIÓN DEL CIELO:
        #   Accede al primer elemento de la lista 'weather' para obtener 
        #   la descripción en español (ej. "nubes dispersas").
        
        <p>☁ Estado: {{ weather.weather[0].description }}</p>
    {% else %}

        # Mensaje de fallback en caso de error en la respuesta de la API

        <p>Error al cargar datos del clima.</p>
    {% endif %}
</div>

{% endblock %}
```
