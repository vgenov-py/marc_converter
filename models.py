query_create_geo = f'''
    CREATE TABLE IF NOT EXISTS geo (
        id TEXT PRIMARY KEY,
        t_001 TEXT,
        t_024 TEXT,
        t_034 TEXT,
        t_080 TEXT,
        t_151 TEXT,
        t_451 TEXT,
        t_510 TEXT,
        t_550 TEXT,
        t_551 TEXT,
        t_667 TEXT,
        t_670 TEXT,
        t_781 TEXT,
        otros_identificadores TEXT,
        coordenadas_lat_lng TEXT,
        CDU TEXT,
        nombre_de_lugar TEXT,
        otros_nombres_de_lugar TEXT,
        entidad_relacionada TEXT,
        materia_relacionada TEXT,
        lugar_relacionado TEXT,
        nota_general TEXT,
        fuentes_de_informacion TEXT,
        lugar_jerarquico TEXT,
        obras_relacionadas_en_el_catalogo_BNE TEXT
    );
'''

query_create_per = f'''
    CREATE TABLE IF NOT EXISTS per (
    id TEXT PRIMARY KEY,
    t_001 TEXT,
    t_024 TEXT,
    t_046 TEXT,
    t_100 TEXT,
    t_368 TEXT,
    t_370 TEXT,
    t_372 TEXT,
    t_373 TEXT,
    t_374 TEXT,
    t_375 TEXT,
    t_377 TEXT,
    t_400 TEXT,
    t_500 TEXT,
    t_510 TEXT,
    t_670 TEXT,
    otros_identificadores TEXT,
    fecha_nacimiento TEXT,
    fecha_muerte TEXT,
    nombre_de_persona TEXT,
    otros_atributos_persona TEXT,
    lugar_nacimiento TEXT,
    lugar_muerte TEXT,
    pais_relacionado TEXT,
    otros_lugares_relacionados TEXT,
    lugar_residencia TEXT,
    campo_actividad TEXT,
    grupo_o_entidad_relacionada TEXT,
    ocupacion TEXT,
    genero TEXT,
    lengua TEXT,
    otros_nombres TEXT,
    persona_relacionada TEXT,
    fuentes_de_informacion TEXT,
    obras_relacionadas_en_el_catalogo_BNE TEXT
    );
'''

query_create_mon = f'''
    CREATE TABLE IF NOT EXISTS mon (
    id TEXT PRIMARY KEY,
    t_001 TEXT,
    t_005 TEXT,
    t_007 TEXT,
    t_008 TEXT,
    t_017 TEXT,
    t_020 TEXT,
    t_024 TEXT,
    t_041 TEXT,
    t_080 TEXT,
    t_100 TEXT,
    t_110 TEXT,
    t_245 TEXT,
    t_246 TEXT,
    t_250 TEXT,
    t_260 TEXT,
    t_264 TEXT,
    t_300 TEXT,
    t_440 TEXT,
    t_490 TEXT,
    t_500 TEXT,
    t_504 TEXT,
    t_505 TEXT,
    t_546 TEXT,
    t_561 TEXT,
    t_563 TEXT,
    t_586 TEXT,
    t_594 TEXT,
    t_600 TEXT,
    t_610 TEXT,
    t_611 TEXT,
    t_630 TEXT,
    t_650 TEXT,
    t_651 TEXT,
    t_653 TEXT,
    t_655 TEXT,
    t_700 TEXT,
    t_710 TEXT,
    t_740 TEXT,
    t_752 TEXT,
    t_770 TEXT,
    t_772 TEXT,
    t_773 TEXT,
    t_774 TEXT,
    t_775 TEXT,
    t_776 TEXT,
    t_777 TEXT,
    t_787 TEXT,
    t_800 TEXT,
    t_810 TEXT,
    t_811 TEXT,
    t_830 TEXT,
    t_980 TEXT,
    t_994 TEXT,
    per_id TEXT,
    pais_de_publicacion TEXT,
    lengua_principal TEXT,
    otras_lenguas TEXT,
    lengua_original TEXT,
    fecha_de_publicacion TEXT,
    decada TEXT,
    siglo TEXT,
    deposito_legal TEXT,
    isbn TEXT,
    nipo TEXT,
    cdu TEXT,
    autores TEXT,
    titulo TEXT,
    mencion_de_autores TEXT,
    otros_titulos TEXT,
    edicion TEXT,
    lugar_de_publicacion TEXT,
    editorial TEXT,
    extension TEXT,
    otras_caracteristicas_fisicas TEXT,
    dimensiones TEXT,
    material_anejo TEXT,
    serie TEXT,
    nota_de_contenido TEXT,
    notas TEXT,
    procedencia TEXT,
    premios TEXT,
    tema TEXT,
    genero_forma TEXT,
    tipo_de_documento TEXT
    );
'''

query_create_moa = f'''
    CREATE TABLE IF NOT EXISTS moa (
    id TEXT PRIMARY KEY,
    t_001 TEXT,
    t_005 TEXT,
    t_008 TEXT,
    t_041 TEXT,
    t_080 TEXT,
    t_100 TEXT,
    t_110 TEXT,
    t_245 TEXT,
    t_246 TEXT,
    t_250 TEXT,
    t_260 TEXT,
    t_264 TEXT,
    t_300 TEXT,
    t_440 TEXT,
    t_490 TEXT,
    t_500 TEXT,
    t_505 TEXT,
    t_510 TEXT,
    t_529 TEXT,
    t_546 TEXT,
    t_561 TEXT,
    t_593 TEXT,
    t_594 TEXT,
    t_595 TEXT,
    t_597 TEXT,
    t_599 TEXT,
    t_600 TEXT,
    t_610 TEXT,
    t_611 TEXT,
    t_630 TEXT,
    t_650 TEXT,
    t_651 TEXT,
    t_653 TEXT,
    t_655 TEXT,
    t_700 TEXT,
    t_710 TEXT,
    t_740 TEXT,
    t_752 TEXT,
    t_856 TEXT,
    t_881 TEXT,
    t_994 TEXT,
    per_id TEXT,
    pais_de_publicacion TEXT,
    lengua_principal TEXT,
    otras_lenguas TEXT,
    lengua_original TEXT,
    fecha_de_publicacion TEXT,
    decada TEXT,
    siglo TEXT,
    cdu TEXT,
    autores TEXT,
    titulo TEXT,
    mencion_de_autores TEXT,
    otros_titulos TEXT,
    edicion TEXT,
    lugar_de_publicacion TEXT,
    editor_impresor TEXT,
    extension TEXT,
    otras_caracteristicas_fisicas TEXT,
    dimensiones TEXT,
    material_anejo TEXT,
    serie TEXT,
    nota_de_contenido TEXT,
    notas TEXT,
    transcripcion_incipit_explicit TEXT,
    procedencia TEXT,
    cita TEXT,
    tema TEXT,
    genero_forma TEXT,
    lugar_relacionado TEXT,
    url TEXT,
    tipo_de_documento TEXT
    );
'''

query_create_ent = '''
CREATE TABLE IF NOT EXISTS ent (
            id TEXT,
            t_001 TEXT,
            t_024 TEXT,
            t_046 TEXT,
            t_110 TEXT,
            t_368 TEXT,
            t_370 TEXT,
            t_372 TEXT,
            t_377 TEXT,
            t_410 TEXT,
            t_500 TEXT,
            t_510 TEXT,
            t_663 TEXT,
            t_665 TEXT,
            t_667 TEXT,
            t_670 TEXT,
            t_678 TEXT,
            otros_identificadores TEXT,
            fecha_establecimiento TEXT,
            fecha_finalizacion TEXT,
            nombre_de_entidad TEXT,
            tipo_entidad TEXT,
            pais TEXT,
            sede TEXT,
            campo_actividad TEXT,
            lengua TEXT,
            otros_nombres TEXT,
            persona_relacionada TEXT,
            grupo_o_entidad_relacionada TEXT,
            nota_de_relacion TEXT,
            otros_datos_historicos TEXT,
            nota_general TEXT,
            fuentes_de_informacion TEXT
            );
'''

query_create_queries = '''
    CREATE VIRTUAL TABLE queries_fts USING FTS5 (id, query, length, date, dataset, time, is_from_web, error);    
'''

query_create_geo_fts ='''
    CREATE VIRTUAL TABLE IF NOT EXISTS geo_fts USING FTS5(
        id,
        t_001,
        t_024,
        t_034,
        t_080,
        t_151,
        t_451,
        t_510,
        t_550,
        t_551,
        t_667,
        t_670,
        t_781,
        otros_identificadores,
        coordenadas_lat_lng,
        CDU,
        nombre_de_lugar,
        otros_nombres_de_lugar,
        entidad_relacionada,
        materia_relacionada,
        lugar_relacionado,
        nota_general,
        fuentes_de_informacion,
        lugar_jerarquico,
        obras_relacionadas_en_el_catalogo_BNE
    );
'''

query_create_per_fts ='''
    CREATE VIRTUAL TABLE IF NOT EXISTS per_fts USING FTS5(
    id,
    t_001,
    t_024,
    t_046,
    t_100,
    t_368,
    t_370,
    t_372,
    t_373,
    t_374,
    t_375,
    t_377,
    t_400,
    t_500,
    t_510,
    t_670,
    otros_identificadores,
    fecha_nacimiento,
    fecha_muerte,
    nombre_de_persona,
    otros_atributos_persona,
    lugar_nacimiento,
    lugar_muerte,
    pais_relacionado,
    otros_lugares_relacionados,
    lugar_residencia,
    campo_actividad,
    grupo_o_entidad_relacionada,
    ocupacion,
    genero,
    lengua,
    otros_nombres,
    persona_relacionada,
    fuentes_de_informacion,
    obras_relacionadas_en_el_catalogo_BNE
    );
'''

query_create_mon_fts ='''
CREATE VIRTUAL TABLE IF NOT EXISTS mon_fts USING FTS5(
    id,
    t_001,
    t_005,
    t_007,
    t_008,
    t_017,
    t_020,
    t_024,
    t_041,
    t_080,
    t_100,
    t_110,
    t_245,
    t_246,
    t_250,
    t_260,
    t_264,
    t_300,
    t_440,
    t_490,
    t_500,
    t_504,
    t_505,
    t_546,
    t_561,
    t_563,
    t_586,
    t_594,
    t_600,
    t_610,
    t_611,
    t_630,
    t_650,
    t_651,
    t_653,
    t_655,
    t_700,
    t_710,
    t_740,
    t_752,
    t_770,
    t_772,
    t_773,
    t_774,
    t_775,
    t_776,
    t_777,
    t_787,
    t_800,
    t_810,
    t_811,
    t_830,
    t_980,
    t_994,
    per_id,
    pais_de_publicacion,
    lengua_principal,
    otras_lenguas,
    lengua_original,
    fecha_de_publicacion,
    decada,
    siglo,
    deposito_legal,
    isbn,
    nipo,
    cdu,
    autores,
    titulo,
    mencion_de_autores,
    otros_titulos,
    edicion,
    lugar_de_publicacion,
    editorial,
    extension,
    otras_caracteristicas_fisicas,
    dimensiones,
    material_anejo,
    serie,
    nota_de_contenido,
    notas,
    procedencia,
    premios,
    tema,
    genero_forma,
    tipo_de_documento
    );
'''

query_create_moa_fts = f'''
    CREATE VIRTUAL TABLE IF NOT EXISTS moa_fts USING FTS5(
    id,
    t_001,
    t_005,
    t_008,
    t_041,
    t_080,
    t_100,
    t_110,
    t_245,
    t_246,
    t_250,
    t_260,
    t_264,
    t_300,
    t_440,
    t_490,
    t_500,
    t_505,
    t_510,
    t_529,
    t_546,
    t_561,
    t_593,
    t_594,
    t_595,
    t_597,
    t_599,
    t_600,
    t_610,
    t_611,
    t_630,
    t_650,
    t_651,
    t_653,
    t_655,
    t_700,
    t_710,
    t_740,
    t_752,
    t_856,
    t_881,
    t_994,
    per_id,
    pais_de_publicacion,
    lengua_principal,
    otras_lenguas,
    lengua_original,
    fecha_de_publicacion,
    decada,
    siglo,
    cdu,
    autores,
    titulo,
    mencion_de_autores,
    otros_titulos,
    edicion,
    lugar_de_publicacion,
    editor_impresor,
    extension,
    otras_caracteristicas_fisicas,
    dimensiones,
    material_anejo,
    serie,
    nota_de_contenido,
    notas,
    transcripcion_incipit_explicit,
    procedencia,
    cita,
    tema,
    genero_forma,
    lugar_relacionado,
    url,
    tipo_de_documento
    );
'''

query_create_ent_fts ='''
CREATE VIRTUAL TABLE IF NOT EXISTS ent_fts USING FTS5(
            id,
            t_001,
            t_024,
            t_046,
            t_110,
            t_368,
            t_370,
            t_372,
            t_377,
            t_410,
            t_500,
            t_510,
            t_663,
            t_665,
            t_667,
            t_670,
            t_678,
            otros_identificadores,
            fecha_establecimiento,
            fecha_finalizacion,
            nombre_de_entidad,
            tipo_entidad,
            pais,
            sede,
            campo_actividad,
            lengua,
            otros_nombres,
            persona_relacionada,
            grupo_o_entidad_relacionada,
            nota_de_relacion,
            otros_datos_historicos,
            nota_general,
            fuentes_de_informacion
            );
'''

query_create_ser_fts ='''
    CREATE VIRTUAL TABLE IF NOT EXISTS ser_fts USING FTS5(
        id,
        t_001,
        t_008,
        t_017,
        t_022,
        t_024,
        t_041,
        t_080,
        t_100,
        t_222,
        t_245,
        t_246,
        t_260,
        t_264,
        t_300,
        t_310,
        t_362,
        t_440,
        t_490,
        t_500,
        t_504,
        t_505,
        t_546,
        t_561,
        t_563,
        t_586,
        t_594,
        t_600,
        t_610,
        t_611,
        t_630,
        t_650,
        t_651,
        t_653,
        t_655,
        t_700,
        t_740,
        pais_de_publicacion,
        lengua_principal,
        otras_lenguas,
        lengua_original,
        fecha_de_publicacion,
        decada,
        siglo,
        deposito_legal,
        issn,
        nipo,
        cdu,
        autores,
        titulo_clave,
        titulo,
        mencion_de_autores,
        otros_titulos,
        lugar_de_publicacion,
        editorial,
        extension,
        otras_caracteristicas_fisicas,
        dimensiones,
        material_anejo,
        periocidad,
        fechas_y_numeracion,
        serie,
        nota_de_contenido,
        notas,
        procedencia,
        tema,
        genero_forma

    );
'''

create_statements = {
    "per": query_create_per, 
    "geo": query_create_geo, 
    "mon": query_create_mon, 
    "moa": query_create_moa, 
    "ent": query_create_ent,
    "per_fts": query_create_per_fts, 
    "geo_fts": query_create_geo_fts, 
    "mon_fts": query_create_mon_fts, 
    "moa_fts": query_create_moa_fts, 
    "ent_fts": query_create_ent_fts,
    "ser_fts":query_create_ser_fts
    }