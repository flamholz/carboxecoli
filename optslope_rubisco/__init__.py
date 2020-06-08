CARBON_SOURCES_LIST = [
    ('glc__D', ),
    #('glc_DASH_D_ex', ),
    ('fru', ),
    ('6pgc', ),
    ('r5p', ),
    ('succ', ),
    ('xu5p__D', ),
    #('xu5p_DASH_D_ex', ),
    ('2pg', ),
    ('ac', ),
    ('dhap', ),
]

# NOTE: the pipe symbol "|" is an "or" and denotes that either of the two genes
# can be knocked out because they are equivalent from a central-metabolic
# perspective. e.g. EDD and EDA both ablate the Entner-Duodoroff pathway. 
SINGLE_KOS = [
    'GLCpts',
    'PGI',
    'PFK',
    'FBP',
    'FBA',
    'TPI',
    'GAPD|PGK',
    'PGM',
    'ENO',
    'PYK',
    'PPS',
    'PDH',
    'PFL',
    'G6PDH2r|PGL',
    'GND',
    'EDD|EDA',
    'RPE',
    'RPI',
    'TKT1|TKT2',
    'TALA',
    'PPC',
    'PPCK',
    'ICL',
    'MALS',
    'CS',
    'ACONTa|ACONTb',
    'ALCD2x',
    'ACALD',
]

TARGET_REACTION = 'RBC'

WILDTYPE_MODEL = "core_model_with_rpp.xml"
#WILDTYPE_MODEL = "EcoliCore2_with_rpp.xml"
