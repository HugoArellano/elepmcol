"""
THIS SET OF FUNCTIONS HELPS TO DEVELOP THE VOTE MAPS
"""

def get_mydict_varlist(sel_election, selected):
    """This function write dictionary and list for every map selection"""

    my_dict = {}
    varlist = []

    if sel_election == "Proyecciones 2024":

        my_dict = {"seccion": "Sección: ",
                   "tipo": "tipo seccion: ",
                   "Xto": "Turnout esperado 2024 %: ",
                   "Xln": "Lista Nominal esperada 2024: ",
                   "Xvt": "Votos totales esperados 2024: ",
                   "votos_perf5_morena_pna": "Voto meta ajust. 5 cand: ",
                   'perf5_morena_pna_pct': "Voto meta ajust. 5 cand %: "
                   }
        varlist = list(my_dict.keys())[2:]

    elif sel_election == "Elecciones PM Colima 2021" and selected == "Totales":
        my_dict = {'contienda': 'Tipo de contienda: ',
                   'anio': "Año:",
                   'seccion': "Sección: ",
                   'winner_cand': "Candidato ganador 2021: ",
                   'winner_part': "Partido con más votos 2021: ",
                   'morena_pna': "Morena-PNA: ",
                   'tc_pan_pri_prd': "Cand.PAN-PRI-PRD: ",
                   "pan": "PAN",
                   "pri": "PRI",
                   "prd": "PRD",
                   'pvem': "PVEM: ",
                   'pt': "PT: ",
                   'mc': "MC: ",
                   'pes': "PES: ",
                   'rsp': "RSP: ",
                   'fxm': "FXM: ",
                   "turnout": "Turnout %: ",
                   }
        varlist = list(my_dict.keys())[5:-1]

    elif sel_election == "Elecciones PM Colima 2021" and selected == "Porcentajes":
        my_dict = {'contienda': 'Tipo de contienda:',
                   'anio': "Año:",
                   'seccion': "Sección: ",
                   'winner_cand': "Candidato ganador 2021: ",
                   'winner_part': "Partido con más votos 2021: ",
                   'morena_pna_pct': "Morena_PNA %: ",
                   'tc_pan_pri_prd_pct': "Cand.PAN-PRI-PRD %: ",
                   'pan_pct': "PAN %: ",
                   'pri_pct': "PRI %: ",
                   'prd_pct': "PRD %: ",
                   'pvem_pct': "PVEM %: ",
                   'pt_pct': "PT %: ",
                   'mc_pct': "MC %: ",
                   'pes_pct': "PES %: ",
                   'rsp_pct': "RSP %: ",
                   'fxm_pct': "FXM %: ",
                   "turnout": "Turnout %: "
                   }
        varlist = list(my_dict.keys())[5:-1]

    elif sel_election == "Datos socidemográficos":
        my_dict = {"seccion": "Seccion",
                   'winner_cand': "Candidato ganador 2021: ",
                   'winner_part': "Partido con más votos 2021: ",
                   'pobfem_pct': "Población femenina %: ",
                   'pob0_14_pct': "Población 0-14 años %: ",
                   'pob15_64_pct': "Población 15-64 años %: ",
                   'pob65_mas_pct': "Población 65+ años %: ",
                   "pea_pct": "Población económicamente activa (mayores 12 años) % :",
                   "pea_f_pct": "PEA femenina sobre total mujeres (mayores 12 años) %:",
                   "pcon_disc_pct": "Población con discapacidad %:",
                   'p18ym_pb_pct': "Población con educación postbásica (mayores 18 años) %:",
                   "contrans_pct": "Viviendas particulares hábitadas con auto, moto o camioneta %:"
                   }

        varlist = list(my_dict.keys())[3:]

    return my_dict, varlist



