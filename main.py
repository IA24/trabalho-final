from localizacao.mapa import Mapa
from localizacao.pais import Pais
from localizacao.coneccao import Coneccao


def cria_coneccoes(localizacao):
    coneccoes = []
    av_con1 = Coneccao(localizacao.aveiro, localizacao.porto, 68)
    av_con2 = Coneccao(localizacao.aveiro, localizacao.viseu, 95)
    av_con3 = Coneccao(localizacao.aveiro, localizacao.coimbra, 68)
    av_con4 = Coneccao(localizacao.aveiro, localizacao.leiria, 115)
    bg_con1 = Coneccao(localizacao.braga, localizacao.viana_castelo, 48)
    bg_con2 = Coneccao(localizacao.braga, localizacao.vila_real, 106)
    bg_con3 = Coneccao(localizacao.braga, localizacao.porto, 53)
    bc_con1 = Coneccao(localizacao.braganca, localizacao.vila_real, 137)
    bc_con2 = Coneccao(localizacao.braganca, localizacao.guarda, 202)
    bj_con1 = Coneccao(localizacao.beja, localizacao.evora, 78)
    bj_con2 = Coneccao(localizacao.beja, localizacao.faro, 152)
    bj_con3 = Coneccao(localizacao.beja, localizacao.setubal, 142)
    cb_con1 = Coneccao(localizacao.castelo_branco, localizacao.coimbra, 159)
    cb_con2 = Coneccao(localizacao.castelo_branco, localizacao.guarda, 106)
    cb_con3 = Coneccao(localizacao.castelo_branco, localizacao.portalegre, 80)
    cb_con4 = Coneccao(localizacao.castelo_branco, localizacao.evora, 203)
    co_con1 = Coneccao(localizacao.coimbra, localizacao.viseu, 96)
    co_con2 = Coneccao(localizacao.coimbra, localizacao.leiria, 67)
    ev_con1 = Coneccao(localizacao.evora, localizacao.lisboa, 150)
    ev_con2 = Coneccao(localizacao.evora, localizacao.santarem, 117)
    ev_con3 = Coneccao(localizacao.evora, localizacao.portalegre, 131)
    ev_con4 = Coneccao(localizacao.evora, localizacao.setubal, 103)
    fr_con1 = Coneccao(localizacao.faro, localizacao.setubal, 249)
    fr_con2 = Coneccao(localizacao.faro, localizacao.lisboa, 299)
    gr_con1 = Coneccao(localizacao.guarda, localizacao.vila_real, 157)
    gr_con2 = Coneccao(localizacao.guarda, localizacao.viseu, 85)
    lr_con1 = Coneccao(localizacao.leiria, localizacao.lisboa, 129)
    lr_con2 = Coneccao(localizacao.leiria, localizacao.santarem, 70)
    ls_con1 = Coneccao(localizacao.lisboa, localizacao.santarem, 78)
    ls_con2 = Coneccao(localizacao.lisboa, localizacao.setubal, 50)
    pt_con1 = Coneccao(localizacao.porto, localizacao.viana_castelo, 71)
    pt_con2 = Coneccao(localizacao.porto, localizacao.vila_real, 116)
    pt_con3 = Coneccao(localizacao.porto, localizacao.viseu, 133)
    vr_con1 = Coneccao(localizacao.vila_real, localizacao.viseu, 110)

    coneccoes.extend(
        [av_con1, av_con2, av_con3, av_con4, bg_con1, bg_con2, bg_con3, bc_con1, bc_con2, bj_con1, bj_con2, bj_con3,
         cb_con1, cb_con2, cb_con3, cb_con4, co_con1, co_con2, ev_con1, ev_con2, ev_con3, ev_con4, fr_con1, fr_con2,
         gr_con1, gr_con2, lr_con1, lr_con2, ls_con1, ls_con2, pt_con1, pt_con2, pt_con3, vr_con1])

    return coneccoes

def main():
    localizacoes = []

    #mapa
    viana_castelo = Mapa("Viana do Castelo", "41.69176464830859, -8.837342672018432")
    braga = Mapa("Braga", "41.545616009067736, -8.426544588389985")
    viseu = Mapa("Viseu", "40.65518424265567, -7.913034512029738")
    vila_real = Mapa("Vila Real", "41.30018979714653, -7.744974733107544")
    braganca = Mapa("Bragança", "41.805632079045566, -6.758492397885592")
    guarda = Mapa("Guarda", "40.5378694275615, -7.266307005126826")
    porto = Mapa("Porto", "41.156668077578296, -8.633019410120614")
    coimbra = Mapa("Coimbra", "40.20295117346438, -8.411485350849919")
    evora = Mapa("Évora", "38.571009088176744, -7.9142525391775385")
    lisboa = Mapa("Lisboa", "38.72093191367713, -9.141214253651464")
    setubal = Mapa("Setúbal", "38.52520112996708, -8.889525470060148")
    santarem = Mapa("Santarém", "39.2356911662872, -8.687002065758271")
    portalegre = Mapa("Portalegre", "39.29714869270152, -7.43334346478745")
    leiria = Mapa("Leiria", "39.74813842092515, -8.808722919076098")
    faro = Mapa("Faro", "37.01714339877875, -7.9303356741666455")
    beja = Mapa("Beja", "38.01701878223444, -7.860143593090843")
    castelo_branco = Mapa("Castelo Branco", "39.81878454648081, -7.498830240065927")
    aveiro = Mapa("Aveiro", "40.640144141268536, -8.653567888787443")

    localizacoes.extend(
        [viana_castelo, braga, viseu, vila_real, braganca, guarda, porto, coimbra, evora, lisboa, setubal, santarem,
         portalegre, leiria, faro, beja, castelo_branco, aveiro])

    pais = Pais("Portugal", localizacoes)
    pais.display()

    #cria_coneccoes(localizacoes)



main()
