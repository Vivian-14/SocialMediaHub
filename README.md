## Integración de APIs

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


## Codificación
