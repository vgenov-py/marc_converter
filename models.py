query_create_queries = '''
    CREATE VIRTUAL TABLE IF NOT EXISTS queries USING FTS5 (id, query, length, date, dataset, time, is_from_web, error);    
'''

query_create_geo ='''
    CREATE VIRTUAL TABLE IF NOT EXISTS geo USING FTS5(
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

query_create_per ='''
    CREATE VIRTUAL TABLE IF NOT EXISTS per USING FTS5(
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
    t_663,
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

query_create_mon ='''
CREATE VIRTUAL TABLE IF NOT EXISTS mon USING FTS5(
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
    t_240,
    t_243,
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
    t_856,
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
    tipo_de_documento,
    url
    );
'''

query_create_moa = f'''
    CREATE VIRTUAL TABLE IF NOT EXISTS moa USING FTS5(
    id,
    t_001,
    t_005,
    t_008,
    t_041,
    t_080,
    t_100,
    t_110,
    t_240,
    t_243,
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
    t_881,
    t_994,
    t_856,
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
    tipo_de_documento
    url,
    );
'''

query_create_ent ='''
CREATE VIRTUAL TABLE IF NOT EXISTS ent USING FTS5(
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

query_create_son = '''
CREATE VIRTUAL TABLE IF NOT EXISTS son USING FTS5(
        id,
        t_001,
        t_007,
        t_008,
        t_015,
        t_017,
        t_020,
        t_024,
        t_028,
        t_040,
        t_041,
        t_080,
        t_084,
        t_100,
        t_110,
        t_111,
        t_130,
        t_240,
        t_243,
        t_245,
        t_246,
        t_250,
        t_260,
        t_264,
        t_300,
        t_336,
        t_337,
        t_338,
        t_344,
        t_347,
        t_382,
        t_440,
        t_490,
        t_500,
        t_505,
        t_508,
        t_510,
        t_511,
        t_518,
        t_520,
        t_521,
        t_530,
        t_533,
        t_538,
        t_540,
        t_546,
        t_561,
        t_586,
        t_593,
        t_594,
        t_595,
        t_596,
        t_597,
        t_600,
        t_610,
        t_630,
        t_650,
        t_651,
        t_653,
        t_655,
        t_700,
        t_710,
        t_740,
        t_856,
        soporte,
        velocidad,
        canales,
        material,
        pais_de_publicacion,
        lengua_principal,
        lengua_libreto,
        otras_lenguas,
        lengua_original,
        fecha_de_publicacion,
        decada_publicacion,
        siglo_publicacion,
        deposito_legal,
        isbn,
        numero_de_editor,
        cdu,
        responsables_e_interpretes,
        nombre_de_congreso,
        titulo,
        otros_titulos,
        edicion,
        lugar_de_publicacion,
        editorial,
        extension,
        otras_caracteristicas_fisicas,
        dimensiones,
        material_anejo,
        tipo_de_contenido,
        tipo_de_medio,
        tipo_de_soporte,
        caracteristicas_archivo_digital,
        sonido,
        medio_interpretacion,
        equipo,
        interpretes,
        fecha_lugar_grabacion,
        contenido,
        serie,
        notas,
        tema,
        genero_forma,
        url
    );
'''

query_create_ser ='''
    CREATE VIRTUAL TABLE IF NOT EXISTS ser USING FTS5(
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
        t_856,
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
        genero_forma,
        url
    );
'''

query_create_mss = '''
    CREATE VIRTUAL TABLE IF NOT EXISTS mss USING FTS5(
        id,
        t_001,
        t_008,
        t_017,
        t_041,
        t_080,
        t_100,
        t_245,
        t_246,
        t_260,
        t_264,
        t_300,
        t_440,
        t_490,
        t_500,
        t_504,
        t_505,
        t_520,
        t_529,
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
        t_856,
        pais_de_publicacion,
        lengua_principal,
        otras_lenguas,
        lengua_original,
        fecha_de_publicacion,
        decada,
        siglo,
        deposito_legal,
        CDU,
        autores,
        titulo,
        mencion_de_autores,
        otros_titulos,
        lugar_de_produccion,
        extension,
        otras_caracteristicas_fisicas,
        dimensiones,
        material_anejo,
        serie,
        nota_de_contenido,
        notas,
        procedencia,
        premios,
        incipit_explicit,
        tema,
        genero_forma,
        url
    );
'''

query_create_vid = '''
CREATE VIRTUAL TABLE IF NOT EXISTS vid USING FTS5(
    id,
    t_001,
    t_007,
    t_008,
    t_017,
    t_020,
    t_024,
    t_028,
    t_041,
    t_080,
    t_100,
    t_110,
    t_130,
    t_240,
    t_245,
    t_246,
    t_250,
    t_260,
    t_264,
    t_300,
    t_337,
    t_338,
    t_344,
    t_345,
    t_346,
    t_440,
    t_490,
    t_500,
    t_505,
    t_508,
    t_511,
    t_518,
    t_520,
    t_521,
    t_530,
    t_546,
    t_586,
    t_590,
    t_594,
    t_597,
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
    t_856,
    pais_de_publicacion,
    lengua_principal,
    lengua_subtitulos,
    otras_lenguas,
    lengua_original,
    soporte,
    color,
    sonido,
    fecha_de_publicacion,
    decada_publicacion,
    siglo_publicacion,
    deposito_legal,
    isbn,
    otros_identificadores,
    cdu,
    responsables_e_interpretes,
    titulo_normalizado,
    titulo,
    otros_titulos,
    edicion,
    lugar_de_publicacion,
    editorial,
    extension,
    otras_caracteristicas_fisicas,
    dimensiones,
    material_anejo,
    tipo_de_medio,
    tipo_de_soporte,
    sonido_vid,
    imagen_video,
    equipo,
    interpretes,
    fecha_lugar_de_grabacion,
    resumen,
    publico,
    contenido,
    serie,
    notas,
    tema,
    genero_forma,
    url
    );
'''

query_create_par = '''
    CREATE VIRTUAL TABLE IF NOT EXISTS par USING FTS5(
        id,
        t_001,
        t_008,
        t_015,
        t_016,
        t_017,
        t_020,
        t_024,
        t_035,
        t_040,
        t_041,
        t_080,
        t_084,
        t_100,
        t_245,
        t_246,
        t_254,
        t_260,
        t_264,
        t_300,
        t_336,
        t_337,
        t_348,
        t_382,
        t_440,
        t_490,
        t_500,
        t_504,
        t_505,
        t_520,
        t_529,
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
        t_856,
        pais_de_publicacion,
        lengua_principal,
        otras_lenguas,
        lengua_original,
        fecha_de_publicacion,
        decada_publicacion,
        siglo_publicacion,
        deposito_legal,
        isbn,
        otros_identificadores,
        numero_de_control_del_sistema,
        cdu,
        autores,
        titulo_normalizado,
        titulo,
        otros_titulos,
        edicion,
        lugar_de_publicacion,
        editorial,
        extension,
        otras_caracteristicas_fisicas,
        dimensiones,
        material_anejo,
        tipo_de_contenido,
        tipo_de_medio,
        tipo_de_soporte,
        equipo,
        formato_partitura,
        forma_partitura,
        medio_interpretacion,
        interpretes,
        fecha_lugar_grabacion,
        resumen,
        publico,
        contenido,
        serie,
        notas,
        tema,
        genero_forma,
        url
    );
'''

query_create_ele = '''
    CREATE VIRTUAL TABLE IF NOT EXISTS ele USING FTS5 (
        id,
        t_001,
        t_007,
        t_008,
        t_015,
        t_016,
        t_017,
        t_020,
        t_024,
        t_035,
        t_040,
        t_041,
        t_080,
        t_084,
        t_100,
        t_110,
        t_111,
        t_130,
        t_245,
        t_246,
        t_250,
        t_256,
        t_260,
        t_264,
        t_300,
        t_336,
        t_337,
        t_338,
        t_347,
        t_440,
        t_490,
        t_500,
        t_504,
        t_505,
        t_520,
        t_521,
        t_529,
        t_538,
        t_540,
        t_546,
        t_561,
        t_563,
        t_586,
        t_594,
        t_597,
        t_600,
        t_610,
        t_611,
        t_630,
        t_650,
        t_651,
        t_653,
        t_655,
        t_710,
        t_856,
        numero_de_bibliografia_nacional,
        pais_de_publicacion,
        lengua_principal,
        otras_lenguas,
        lengua_original,
        fecha_de_publicacion,
        decada_publicacion,
        siglo_publicacion,
        deposito_legal,
        isbn,
        numero_de_control_del_sistema,
        cdu,
        autores,
        nombre_de_congreso,
        titulo_normalizado,
        titulo,
        otros_titulos,
        edicion,
        caracteristicas_del_archivo,
        lugar_de_publicacion,
        editorial,
        extension,
        otras_caracteristicas_fisicas,
        dimensiones,
        material_anejo,
        tipo_de_contenido,
        tipo_de_medio,
        tipo_de_soporte,
        sonido,
        imagen_video,
        equipo,
        interpretes,
        fecha_lugar_grabacion,
        resumen,
        publico,
        contenido,
        serie,
        notas,
        tema,
        genero_forma,
        url
    );
'''

query_create_gra = '''
CREATE VIRTUAL TABLE IF NOT EXISTS gra USING FTS5(
        id,
        t_001,
        t_007,
        t_008,
        t_015,
        t_016,
        t_017,
        t_020,
        t_024,
        t_028,
        t_035,
        t_040,
        t_041,
        t_080,
        t_084,
        t_100,
        t_110,
        t_111,
        t_130,
        t_240,
        t_243,
        t_245,
        t_246,
        t_250,
        t_255,
        t_256,
        t_260,
        t_264,
        t_300,
        t_336,
        t_337,
        t_440,
        t_490,
        t_500,
        t_501,
        t_505,
        t_507,
        t_510,
        t_518,
        t_520,
        t_530,
        t_540,
        t_541,
        t_546,
        t_561,
        t_580,
        t_585,
        t_593,
        t_594,
        t_595,
        t_596,
        t_597,
        t_598,
        t_600,
        t_610,
        t_611,
        t_630,
        t_650,
        t_651,
        t_653,
        t_655,
        t_662,
        t_700,
        t_710,
        t_740,
        t_773,
        t_856,
        numero_de_bibliografia_nacional,
        pais_de_publicacion,
        lengua_principal,
        otras_lenguas,
        lengua_original,
        fecha_de_publicacion,
        decada_publicacio,
        siglo_publicacion,
        agencia_bibliografica_nacional,
        deposito_legal,
        isbn,
        numero_de_editor,
        numero_de_control_del_sistema,
        cdu,
        autores,
        nombre_de_congreso,
        titulo_normalizado,
        titulo_colectivo,
        titulo,
        otros_titulos,
        edicion,
        datos_matematicos_cartograficos,
        caracteristicas_del_archivo,
        lugar_de_publicacion,
        editorial,
        extension,
        otras_caracteristicas_fisicas,
        dimensiones,
        material_anejo,
        tipo_de_contenido,
        tipo_de_medio,
        equipo,
        interpretes,
        fecha_lugar_grabacion,
        resumen,
        publico,
        contenido,
        serie,
        notas,
        tema,
        genero_forma,
        url
    );
'''


create_statements = {
    "per": query_create_per, 
    "geo": query_create_geo, 
    "mon": query_create_mon, 
    "moa": query_create_moa, 
    "ent": query_create_ent,
    "ser":query_create_ser,
    "mss": query_create_mss,
    "vid": query_create_vid,
    "par": query_create_par,
    "ele": query_create_ele,
    "son": query_create_son,
    "gra": query_create_gra,
    "queries": query_create_queries
    # "per_fts": query_create_per_fts, 
    # "geo_fts": query_create_geo_fts, 
    # "mon_fts": query_create_mon_fts, 
    # "moa_fts": query_create_moa_fts, 
    # "ent_fts": query_create_ent_fts,
    }
