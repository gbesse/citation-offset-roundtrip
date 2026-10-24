# citation-offset-roundtrip

## Français

Détecter les citations décalées entre octets UTF-8 et unités UTF-16.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m citation_offset_roundtrip examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Convertit les intervalles de citation entre points Unicode, octets UTF-8 et unités UTF-16, puis vérifie le texte cité sans normalisation. Un témoin rend visibles les coupures de caractère et pertes d’annotation.

### Limites

Offsets et texte fournis ; aucune preuve de véracité, d’authenticité ou de disponibilité de la source. Les caractères combinés restent distincts et les données utilisateur inchangées.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Detect citation offsets shifted between UTF-8 bytes and UTF-16 units.

Synthetic data; no network access or secret required.

```sh
python -m citation_offset_roundtrip examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Converts citation intervals between Unicode code points, UTF-8 bytes and UTF-16 units, then checks quoted text without normalization. Witnesses expose split characters and annotation drift.

### Limits

Supplied offsets and text; no proof of factual truth, authenticity or source availability. Combining characters remain distinct and user data unchanged.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Detectar citas desplazadas entre bytes UTF-8 y unidades UTF-16.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m citation_offset_roundtrip examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Convierte intervalos de citas entre puntos Unicode, bytes UTF-8 y unidades UTF-16 y comprueba el texto sin normalizar. Los testigos muestran caracteres cortados y desplazamientos de anotación.

### Límites

Offsets y texto suministrados; sin prueba de veracidad, autenticidad o disponibilidad de fuente. Los caracteres combinados siguen separados y los datos sin cambios.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/pydantic/magpie/issues/3455
- https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/
