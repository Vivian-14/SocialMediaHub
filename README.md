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

