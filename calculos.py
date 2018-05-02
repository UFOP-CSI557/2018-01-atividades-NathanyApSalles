import numpy
import statistics

Blend = [3.5130831577134813E-10, 5.671498826131938E-10, 3.364751854917358E-8, 1.0234870728709211E-9, 4.694491071433049E-7, 5.426770144367765E-12, 1.7989876255342097E-10, 8.827090169916119E-9, 2.1832669006016658E-10, 5.242915435133E-8, 3.8342662378454406E-11, 4.606198089618374E-9, 3.7626790572176105E-11, 4.844155299110753E-9, 7.217337838483218E-12, 3.1572629310971934E-7, 2.1191759458361048E-10, 3.661302372393038E-10, 1.617017630906048E-11, 1.3011067778734287E-9, 3.4225777767460386E-10, 1.7128209606198652E-7, 4.125779220487402E-7, 3.2803715299678515E-9, 2.5277557824665564E-12, 1.5827583510485965E-7, 8.254197325641144E-11, 1.845300801051053E-9, 4.616844477922655E-5, 0.15870707178511445]
TempoBlend = [457.0, 326.0, 315.0, 314.0, 303.0, 349.0, 476.0, 301.0, 264.0, 269.0, 266.0, 270.0, 272.0, 280.0, 263.0, 282.0, 270.0, 268.0, 269.0, 271.0, 270.0, 278.0, 280.0, 273.0, 259.0, 278.0, 271.0, 284.0, 282.0, 307.0]
Dois_pontos = [1.8579805489693513E-5, 1.48911993846923E-11, 2.155307043949506E-10, 1.9601876203978463E-5, 2.2423911616442638E-9, 1.3394032549740587E-9, 1.0231815394945443E-12, 1.3150209989733401, 1.2888357048268517E-10, 3.8689051962137455E-11, 5.24095966625282E-9, 5.899867261405234E-10, 4.912692475045333E-11, 1.073557243103096E-9, 2.383305286457471E-8, 1.5407330221961502E-4, 5.583478230875016E-7, 1.0568871491852612, 5.329070518200751E-15, 4.338751580235112E-11, 0.0063644711570933765, 1.7831648335686623E-7, 1.1702631416449307, 2.4139623633345764E-10, 8.746781077206833E-12, 4.191207381154527E-10, 0.004335392309483765, 7.762821496726247E-10, 1.1866063687193673E-12, 3.2673172025710073E-6]
TempoDois_pontos = [193.0, 51.0, 39.0, 45.0, 34.0, 37.0, 37.0, 42.0, 41.0, 33.0, 34.0, 33.0, 42.0, 35.0, 34.0, 30.0, 32.0, 33.0, 31.0, 30.0, 31.0, 30.0, 29.0, 31.0, 30.0, 41.0, 30.0, 31.0, 31.0, 30.0]

mediaBlend = 0.0
mediaDoisPontos = 0.0
mediaTempoBlend = 0.0
mediaTempoDois_pontos = 0.0

for x in range(0,len(Blend)):
	mediaTempoBlend += TempoBlend[x]
	mediaTempoDois_pontos += TempoDois_pontos[x]

mediaBlend = mediaBlend/len(Blend)
mediaTempoBlend = mediaTempoBlend/len(TempoBlend)
mediaDoisPontos = mediaTempoDois_pontos/len(TempoDois_pontos)

print('Blend:')
print('Desvio padrao: ' + str(statistics.pstdev(Blend)))
print('Media do tempo: ' + str(mediaTempoBlend))

print('\nDois_pontos:')
print('Desvio padrao: ' + str(statistics.pstdev(Dois_pontos)))
print('Media do tempo:' + str(mediaTempoDois_pontos))	